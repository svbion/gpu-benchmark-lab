# Benchmark Package Specification v0.1

The GPU Benchmark Package Specification defines a public-safe, evidence-first benchmark package for GPU Benchmark Lab and GPUValidator ingestion.

## Required top-level files

```text
benchmark-package/
├── metadata.json
├── manifest.json
├── benchmark-summary.json
├── README.md
├── evidence/
├── parsed/
├── reports/
├── lessons/
├── charts/
├── artifacts/
├── FILE-INVENTORY.txt
└── SHA256SUMS
```

## Evidence rules

- Public packages contain sanitized logs and derived artifacts only.
- RAW/private archives remain local-only and must not be committed.
- Do not redistribute NVIDIA proprietary binaries or compiled NCCL Tests binaries.
- Unknown fields must be null, omitted, or marked not available; do not fabricate values.

## Licensing and attribution

Project-authored code and documentation follow the repository license. Benchmark outputs, NVIDIA tool output, NCCL Tests references, provider names, and trademarks are attributed to their respective owners and are included for evidence/education, not as a transfer of ownership.

Schemas live in `schemas/benchmark-package/v0.1/` and use JSON Schema Draft 2020-12.
