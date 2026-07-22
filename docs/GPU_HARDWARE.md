# GPU Hardware

> Evidence policy: this public repository contains documentation, sanitized evidence references, screenshots, and report examples only. GPUValidator is a proprietary internal enterprise platform and remains private. No GPUValidator source code, backend, frontend, authentication, agent implementation, APIs, business logic, or enterprise architecture is included.


## Public Hardware Summary

| Field | Value |
| :--- | :--- |
| GPU count | 4 |
| GPU class | NVIDIA A100 SXM |
| Raw evidence model string | NVIDIA A100-SXM4-80GB |
| Deployment | RunPod single node |
| Topology scope | Single-node multi-GPU |

## Evidence

The included AllReduce output records:

```text
# GPUs: 4 x NVIDIA A100-SXM4-80GB
```

Source: [redacted-real-nccl-all-reduce.txt](../evidence/raw/nccl/redacted-real-nccl-all-reduce.txt).

## Engineering Relevance

A100 SXM systems are used for high-throughput AI training and inference workloads where GPU-to-GPU communication can dominate application performance. A portfolio-quality validation workflow must therefore verify not only GPU presence, but communication behavior under representative collective operations.

## Inventory Checklist

- GPU count visible in `nvidia-smi -L`
- GPU model captured without exposing UUIDs
- Driver version captured
- CUDA runtime compatibility captured
- Topology captured when safe to publish
- NCCL communication validated with raw output evidence
