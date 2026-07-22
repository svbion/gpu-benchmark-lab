# Contributing

> Public release boundary: this repository documents engineering methodology, sanitized evidence references, benchmark interpretation, and executive reporting. GPUValidator is proprietary software. No source code, product internals, API contracts, database schemas, authentication/RBAC design, agent protocol, customer data, private URLs, secrets, or production screenshots are included.


This repository is public-facing documentation only. Contributions must strengthen the story of engineering an enterprise GPU benchmarking and validation environment while preserving IP boundaries.

## Rules

- Do not add GPUValidator source code or product internals.
- Do not add API endpoints, database schemas, auth/RBAC design, agent protocol details, message formats, directory structures from the private platform, secrets, hostnames, tokens, UUIDs, private URLs, customer names, or production screenshots.
- Do not invent benchmark results or imply that methodology-only benchmarks were executed.
- Do not add raw provider/customer evidence unless it is explicitly approved for public release and sanitized.
- Prefer high-level engineering descriptions tied to public evidence.

## Documentation Standards

- Lead with the business problem, then explain the engineering method.
- Separate facts, assumptions, limitations, and future work.
- Link numeric claims to evidence.
- Use consistent language: GPUValidator is proprietary software; this repository documents methodology, benchmarking, validation, and reporting.
- Validate links and images with `python3 scripts/validate_docs.py` before committing.
