#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess
import sys

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    out = root / '.cache-docs' / 'mermaid'
    out.mkdir(parents=True, exist_ok=True)
    puppeteer_config = out / 'puppeteer-config.json'
    puppeteer_config.write_text('{"args":["--no-sandbox","--disable-setuid-sandbox"]}\n', encoding='utf-8')
    diagrams = []
    for md in sorted(root.rglob('*.md')):
        if '.git' in md.parts or '.cache-docs' in md.parts:
            continue
        text = md.read_text(encoding='utf-8')
        for idx, block in enumerate(re.findall(r'```mermaid\n(.*?)\n```', text, re.S), 1):
            diagrams.append((md, idx, block))
    for mmd in sorted((root / 'assets' / 'diagrams').glob('*.mmd')):
        diagrams.append((mmd, 1, mmd.read_text(encoding='utf-8')))
    if not diagrams:
        print('No Mermaid diagrams found.')
        return 0
    for source, idx, block in diagrams:
        safe_name = f'{source.relative_to(root).as_posix().replace("/", "__")}-{idx}'
        in_file = out / f'{safe_name}.mmd'
        out_file = out / f'{safe_name}.svg'
        in_file.write_text(block, encoding='utf-8')
        subprocess.run([
            'npx', '--yes', '@mermaid-js/mermaid-cli',
            '-p', str(puppeteer_config),
            '-i', str(in_file),
            '-o', str(out_file),
        ], check=True)
    print(f'Rendered {len(diagrams)} Mermaid diagrams.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
