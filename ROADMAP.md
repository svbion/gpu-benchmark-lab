# Roadmap

> Evidence policy: this public repository contains documentation, sanitized evidence references, screenshots, and report examples only. GPUValidator is a proprietary internal enterprise platform and remains private. No GPUValidator source code, backend, frontend, authentication, agent implementation, APIs, business logic, or enterprise architecture is included.


## Near Term

- Add customer-approved raw output files for all NCCL collectives beyond AllReduce.
- Add sanitized GPU topology output from `nvidia-smi topo -m` when approved for public release.
- Add a public evidence manifest with checksums for each raw artifact and screenshot.
- Add GitHub Actions for markdown link validation.

## Medium Term

- Add multi-node methodology documentation for NCCL once real multi-node evidence is available.
- Add HPL methodology and evidence only after approved real output exists.
- Add DCGM diagnostic workflow documentation with explicit approval boundaries.
- Add report templates that map technical findings to executive risk categories.

## Long Term

- Publish a companion blog post explaining enterprise AI compute acceptance testing.
- Add portfolio video walkthrough and annotated architecture diagrams.
- Add sanitized before/after report examples for executive, infrastructure, GPU inventory, and management audiences.
