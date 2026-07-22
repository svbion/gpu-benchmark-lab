#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
warnings = []
md_files = sorted(p for p in root.rglob('*.md') if '.git' not in p.parts)

def iter_non_code_lines(text):
    in_fence = False
    for idx, line in enumerate(text.splitlines(), 1):
        if line.startswith('```'):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield idx, line

slug_counts_by_file = {}
for md in md_files:
    text = md.read_text(encoding='utf-8')
    slugs = {}
    for _, line in iter_non_code_lines(text):
        if line.startswith('#'):
            title = line.lstrip('#').strip()
            slug = re.sub(r'[^a-z0-9 -]', '', title.lower()).replace(' ', '-')
            slug = re.sub(r'-+', '-', slug).strip('-')
            count = slugs.get(slug, 0)
            slugs[slug] = count + 1
            if count:
                slugs[f'{slug}-{count}'] = 1
    slug_counts_by_file[md] = set(slugs)

link_re = re.compile(r'!\[[^\]]*\]\(([^)]+)\)|(?<!!)(?<!\])\[[^\]]+\]\(([^)]+)\)')
for md in md_files:
    text = md.read_text(encoding='utf-8')
    for match in link_re.finditer(text):
        target = match.group(1) or match.group(2)
        if target.startswith(('http://', 'https://', 'mailto:')):
            continue
        path_part, _, frag = target.partition('#')
        if path_part:
            path = (md.parent / path_part).resolve()
            try:
                path.relative_to(root)
            except ValueError:
                errors.append(f'{md.relative_to(root)}: link escapes repo: {target}')
                continue
            if not path.exists():
                errors.append(f'{md.relative_to(root)}: missing link target: {target}')
                continue
        else:
            path = md
        if frag and frag not in slug_counts_by_file.get(path, set()):
            warnings.append(f'{md.relative_to(root)}: unchecked or missing anchor #{frag} in {target}')

    if text.count('```') % 2:
        errors.append(f'{md.relative_to(root)}: unbalanced fenced code blocks')

    prev = 0
    for idx, line in iter_non_code_lines(text):
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            if prev and level > prev + 1:
                warnings.append(f'{md.relative_to(root)}:{idx}: heading jumps from H{prev} to H{level}')
            prev = level

for html in [root / 'index.html']:
    if html.exists():
        text = html.read_text(encoding='utf-8')
        for src in re.findall(r'(?:src|href)="([^"]+)"', text):
            if src.startswith(('http://', 'https://', 'mailto:')) or src.startswith('#'):
                continue
            path = (html.parent / src).resolve()
            if not path.exists():
                errors.append(f'{html.relative_to(root)}: missing target: {src}')

sensitive_patterns = {
    'uuid': r'(?<!fixture-)(?<!REDACTED-GPU-)\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b',
    'token_assignment': r'(?i)(token|secret|api[_ -]?key)\s*[:=]\s*[^\s`]+',
    'private_path': r'/Users/[^\s)`]+',
    'raw_hostname': r'\b(runpod-node-\d+|AI-CLUSTER-\d+)\b',
}
for p in list(md_files) + [root/'index.html', root/'style.css']:
    if not p.exists():
        continue
    text = p.read_text(encoding='utf-8')
    for name, pattern in sensitive_patterns.items():
        for m in re.finditer(pattern, text):
            errors.append(f'{p.relative_to(root)}: sensitive pattern {name}: {m.group(0)[:80]}')

for img in (root/'assets/public').glob('*'):
    if img.stat().st_size == 0:
        errors.append(f'{img.relative_to(root)}: empty public asset')

if warnings:
    print('Warnings:')
    print('\n'.join(warnings))
if errors:
    print('Errors:')
    print('\n'.join(errors))
    sys.exit(1)
print(f'Validated {len(md_files)} markdown files, local links, image references, Mermaid fences, headings, and sensitive-text patterns.')
