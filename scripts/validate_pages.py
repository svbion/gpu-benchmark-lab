#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []

REPOSITORY_URL = 'https://github.com/svbion/gpu-benchmark-lab'
PAGES_URL = 'https://svbion.github.io/gpu-benchmark-lab/'
PLACEHOLDERS = (
    '<YOUR_USERNAME>',
    'github.com/placeholder',
    'example.com',
    'site.repository_url',
    'site.profile.website_url',
    'site.profile.linkedin_url',
    'site.profile.email_url',
)

class RefParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.anchors = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if 'id' in data:
            self.anchors.add(data['id'])
        if tag == 'a':
            self.links.append(data)
        for key in ('href', 'src', 'content'):
            if key in data:
                self.refs.append((tag, key, data[key]))

def local_path(source, value):
    path_part = value.split('#', 1)[0]
    if not path_part:
        return None
    return (source.parent / path_part).resolve()

def validate_url(source, tag, key, value, parser):
    label = f'{source.relative_to(root)}: {tag} {key}'
    if value is None or value.strip() == '':
        errors.append(f'{label} is empty')
        return
    if value == '#':
        errors.append(f'{label} uses placeholder href="#"')
        return
    if '{{' in value or '}}' in value:
        errors.append(f'{label} contains unrendered Liquid placeholder: {value}')
        return
    for placeholder in PLACEHOLDERS:
        if placeholder.lower() in value.lower():
            errors.append(f'{label} contains placeholder URL/text: {value}')
    parsed = urlparse(value)
    if parsed.scheme in ('http', 'https'):
        if not parsed.netloc or ' ' in value:
            errors.append(f'{label} is malformed: {value}')
        if 'github.com' in parsed.netloc:
            if parsed.netloc != 'github.com':
                errors.append(f'{label} has malformed GitHub host: {value}')
            if value.startswith('https://github.com/placeholder'):
                errors.append(f'{label} uses placeholder GitHub URL: {value}')
        return
    if parsed.scheme == 'mailto':
        if '@' not in parsed.path:
            errors.append(f'{label} has malformed mailto URL: {value}')
        return
    if parsed.scheme:
        errors.append(f'{label} uses unsupported URL scheme: {value}')
        return
    if value.startswith('#'):
        anchor = value[1:]
        if anchor not in parser.anchors:
            errors.append(f'{label} targets missing anchor: {value}')
        return
    if value.startswith('github.com/') or value.startswith('www.github.com/'):
        errors.append(f'{label} is a relative GitHub URL; use https://github.com/: {value}')
        return
    path = local_path(source, value)
    if path is None:
        errors.append(f'{label} has no local path or anchor target: {value}')
        return
    try:
        path.relative_to(root)
    except ValueError:
        errors.append(f'{label} escapes repo: {value}')
        return
    if not path.exists():
        errors.append(f'{label} missing local target: {value}')
        return
    if '#' in value:
        anchor_source = path.read_text(encoding='utf-8', errors='ignore')
        frag = value.split('#', 1)[1]
        if path.suffix == '.html' and f'id="{frag}"' not in anchor_source and f"id='{frag}'" not in anchor_source:
            errors.append(f'{label} targets missing local HTML anchor: {value}')

for html in [root / 'index.html', root / '404.html']:
    parser = RefParser()
    text = html.read_text(encoding='utf-8')
    parser.feed(text)
    for placeholder in PLACEHOLDERS:
        if placeholder.lower() in text.lower():
            errors.append(f'{html.relative_to(root)}: placeholder remains: {placeholder}')
    for tag, key, value in parser.refs:
        if key == 'content' and not value.startswith(('http://', 'https://')):
            continue
        validate_url(html, tag, key, value, parser)
    for link in parser.links:
        href = link.get('href', '')
        if href.startswith(('http://', 'https://')):
            if link.get('target') == '_blank' and link.get('rel') != 'noopener noreferrer':
                errors.append(f'{html.relative_to(root)}: external link missing rel="noopener noreferrer": {href}')
            if not link.get('aria-label') and not re.search(r'>\s*\S+', text):
                errors.append(f'{html.relative_to(root)}: external link may lack accessible label: {href}')

index = (root / 'index.html').read_text(encoding='utf-8')
if f'<link rel="canonical" href="{PAGES_URL}">' not in index:
    errors.append(f'index.html: canonical URL must be exactly {PAGES_URL}')
if f'<meta property="og:url" content="{PAGES_URL}">' not in index:
    errors.append(f'index.html: og:url must be exactly {PAGES_URL}')
if f'class="nav-cta" href="{REPOSITORY_URL}"' not in index:
    errors.append(f'index.html: top-right GitHub button must use exactly {REPOSITORY_URL}')
if index.count(f'href="{REPOSITORY_URL}"') < 2:
    errors.append(f'index.html: expected repository links to use exactly {REPOSITORY_URL}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Validated GitHub Pages local references, anchors, external links, and canonical repository/site URLs.')
