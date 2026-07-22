# Roadmap

> Public release boundary: this repository documents engineering methodology, sanitized evidence references, benchmark interpretation, and executive reporting. GPUValidator is proprietary software. No source code, product internals, API contracts, database schemas, authentication/RBAC design, agent protocol, customer data, private URLs, secrets, or production screenshots are included.

## Near Term

- Add provider-approved raw outputs for AllGather, ReduceScatter, Broadcast, Reduce, AllToAll, and SendRecv only after public-release approval.
- Add sanitized topology evidence from `nvidia-smi topo -m` only if hostnames, bus IDs, UUIDs, and provider identifiers are approved or redacted.
- Add screenshot provenance notes for any future public visuals.
- Extend release automation after additional public evidence is approved.

## Medium Term

- Add multi-node NCCL methodology once real multi-node evidence is available and approved.
- Add HPL, HPL-AI, HPCG, OSU MPI, fio, or iperf3 sections only when real output and constraints are documented.
- Add a signed evidence manifest for formal customer/public portfolio use.

## Long Term

- Publish additional case studies for GPU troubleshooting, scheduler-aware validation, and enterprise acceptance workflows without revealing proprietary implementation.
- Create a talk or webinar based on the public methodology and lessons learned.
