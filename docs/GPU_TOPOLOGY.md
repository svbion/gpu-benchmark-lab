# GPU Topology

> Public release boundary: this repository documents engineering methodology, sanitized evidence references, benchmark interpretation, and executive reporting. GPUValidator is proprietary software. No source code, product internals, API contracts, database schemas, authentication/RBAC design, agent protocol, customer data, private URLs, secrets, or production screenshots are included.

## Purpose

GPU topology affects collective communication performance, NUMA behavior, peer-to-peer paths, and expected NCCL bandwidth. Topology review is part of enterprise GPU acceptance because not all multi-GPU nodes behave the same.

## Evidence Status

This public RC1 does not publish a raw `nvidia-smi topo -m` matrix. Therefore no specific NVLink, PCIe, NUMA, InfiniBand, or fabric topology matrix is claimed here.

## Recommended Evidence for Future Publication

- Sanitized `nvidia-smi topo -m` output.
- GPU count/model summary with UUIDs removed.
- Driver/runtime versions.
- NCCL command and output provenance.
- Clear limitations if topology tools are unavailable or redaction prevents publication.

## Public Interpretation Rule

Discuss topology as methodology unless approved raw topology evidence is present. Do not infer interconnect details from GPU model alone.
