#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / 'benchmarks'
SECRET_PATTERNS = {
    'gpu_uuid': re.compile(r'GPU-(?!REDACTED\b)[0-9a-fA-F-]{8,}'),
    'private_ipv4': re.compile(r'(?<![0-9])(?:10\.|172\.(?:1[6-9]|2[0-9]|3[0-1])\.|192\.168\.|127\.|169\.254\.)\d{1,3}\.\d{1,3}\.\d{1,3}(?![0-9])'),
    'mac': re.compile(r'(?i)(?:[0-9a-f]{2}:){5}[0-9a-f]{2}'),
    'secret_assignment': re.compile(r'(?i)(api[_-]?key|access[_-]?token|secret|password)\s*[:=]\s*[^\s]+'),
    'home_path': re.compile(r'/(?:home|Users)/[^/\s]+'),
}
def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024), b''): h.update(b)
    return h.hexdigest()
def validate_json(path: Path) -> None:
    json.loads(path.read_text(encoding='utf-8'))
def validate_checksums(pkg: Path) -> list[str]:
    errors=[]; sums=pkg/'SHA256SUMS'
    if not sums.exists(): return [f'{pkg}: SHA256SUMS missing']
    for raw in sums.read_text().splitlines():
        if not raw.strip(): continue
        digest, rel = raw.split(None, 1); rel=rel.strip().lstrip('*')
        target=pkg/rel
        if not target.exists(): errors.append(f'{pkg}: missing checksum target {rel}')
        elif sha256(target)!=digest: errors.append(f'{pkg}: checksum mismatch {rel}')
    return errors
def scan_secrets(pkg: Path) -> list[str]:
    findings=[]
    for path in pkg.rglob('*'):
        if not path.is_file() or path.suffix.lower() in {'.png','.jpg','.jpeg','.gif','.pdf'}: continue
        text=path.read_text(encoding='utf-8', errors='ignore')
        for name,rx in SECRET_PATTERNS.items():
            if rx.search(text): findings.append(f'{name}: {path.relative_to(ROOT)}')
    return findings
def main() -> int:
    errors=[]
    for p in list(ROOT.glob('schemas/**/*.json')) + list(BENCH.glob('**/*.json')):
        validate_json(p)
    index=json.loads((BENCH/'index.json').read_text())
    for entry in index.get('benchmarks',[]):
        pkg=ROOT/entry['path']
        if not pkg.exists(): errors.append(f'missing benchmark package {pkg}')
        else:
            for req in ['metadata.json','manifest.json','benchmark-summary.json','FILE-INVENTORY.txt','SHA256SUMS']:
                if not (pkg/req).exists(): errors.append(f'{pkg}: missing {req}')
            errors += validate_checksums(pkg)
            errors += scan_secrets(pkg)
    if errors:
        print('\n'.join(errors), file=sys.stderr); return 1
    print('benchmark package validation passed')
    return 0
if __name__ == '__main__': raise SystemExit(main())
