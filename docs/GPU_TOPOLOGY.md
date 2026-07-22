# GPU Topology

> Evidence policy: this public repository contains documentation, sanitized evidence references, screenshots, and report examples only. GPUValidator is a proprietary internal enterprise platform and remains private. No GPUValidator source code, backend, frontend, authentication, agent implementation, APIs, business logic, or enterprise architecture is included.


## Purpose

GPU topology explains how GPUs are connected within the node and affects expected communication behavior.

## Evidence Status

This public repository includes screenshots and NCCL AllReduce output, but it does not include a raw sanitized `nvidia-smi topo -m` text artifact. Therefore no specific NVLink, PCIe, NUMA, or fabric topology matrix is claimed here.

## Recommended Evidence

When approved for public release, add:

```bash
nvidia-smi topo -m > evidence/raw/gpu/topology.txt
nvidia-smi nvlink --status > evidence/raw/gpu/nvlink-status.txt
```

Remove or redact host identifiers as needed, then link those files from this document.
