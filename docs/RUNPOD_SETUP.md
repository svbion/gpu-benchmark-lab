# RunPod Setup

> Evidence policy: this public repository contains documentation, sanitized evidence references, screenshots, and report examples only. GPUValidator is a proprietary internal enterprise platform and remains private. No GPUValidator source code, backend, frontend, authentication, agent implementation, APIs, business logic, or enterprise architecture is included.


## Scope

This document describes the public portfolio setup for a RunPod single-node multi-GPU benchmark lab. It intentionally avoids proprietary deployment internals.

## Environment

| Component | Value |
| :--- | :--- |
| Provider | RunPod |
| Node | Single GPU node |
| GPU count | 4 |
| GPU class | NVIDIA A100 SXM |
| Benchmark focus | NCCL collective communication |

## Setup Flow

1. Provision or access an authorized RunPod node with four NVIDIA A100 SXM GPUs.
2. Confirm Linux shell access through approved RunPod terminal or SSH workflow.
3. Capture basic host evidence:
   - `hostname`
   - `uname -a`
   - `python3 --version`
   - `nvidia-smi`
   - `nvidia-smi -L`
   - `nvidia-smi topo -m`
4. Confirm NCCL Tests availability.
5. Execute approved NCCL collective benchmarks.
6. Preserve raw output files in an evidence folder.
7. Generate documentation and reports from sanitized evidence.

## Operational Guardrails

- Use only authorized RunPod access paths.
- Do not place tokens or keys in screenshots.
- Do not publish raw hostnames, GPU UUIDs, internal URLs, or customer identifiers.
- Do not claim a benchmark was executed unless its output exists and is referenced.

## Screenshots

- [RunPod agent online](../assets/screenshots/runpod/runpod-agent-online.png)
- [GPU inventory](../assets/screenshots/runpod/runpod-gpu-inventory.png)
- [Hardware validation](../assets/screenshots/runpod/runpod-hardware-validation.png)
- [Validation results](../assets/screenshots/runpod/runpod-validation-results.png)
