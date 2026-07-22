#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
errors = []

class RefParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        for key in ('href', 'src'):
            if key in data:
                self.refs.append((tag, key, data[key]))

for html in [root / 'index.html']:
    parser = RefParser()
    parser.feed(html.read_text(encoding='utf-8'))
    for tag, key, value in parser.refs:
        if value.startswith(('http://', 'https://', 'mailto:', '#', '{{')):
            continue
        path = (html.parent / value).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            errors.append(f'{html.relative_to(root)}: {key} escapes repo: {value}')
            continue
        if not path.exists():
            errors.append(f'{html.relative_to(root)}: missing {key}: {value}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Validated GitHub Pages local references.')
