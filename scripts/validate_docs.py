#!/usr/bin/env python3
from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
errors = []
for md in sorted(root.rglob('*.md')):
    text = md.read_text(encoding='utf-8')
    for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)|(?<!!)(?<!\])\[[^\]]+\]\(([^)]+)\)', text):
        target = m.group(1) or m.group(2)
        if '://' in target or target.startswith('#') or target.startswith('mailto:'):
            continue
        path_part, _, frag = target.partition('#')
        if not path_part:
            continue
        path = (md.parent / path_part).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            errors.append(f'{md.relative_to(root)}: link escapes repo: {target}')
            continue
        if not path.exists():
            errors.append(f'{md.relative_to(root)}: missing link target: {target}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Validated markdown links and image references.')
