# Interview Guide

> Evidence policy: this public repository contains documentation, sanitized evidence references, screenshots, and report examples only. GPUValidator is a proprietary internal enterprise platform and remains private. No GPUValidator source code, backend, frontend, authentication, agent implementation, APIs, business logic, or enterprise architecture is included.


## Elevator Pitch

I built and documented a GPU benchmarking lab around a RunPod A100 SXM multi-GPU environment. The project demonstrates how to validate Linux GPU infrastructure, run and interpret NCCL collective benchmarks, preserve raw evidence, and translate engineering output into executive-ready documentation while maintaining a clean boundary around proprietary platform code.

## Senior Engineer Talking Points

- Designed an evidence-first validation workflow for AI compute infrastructure.
- Worked with NVIDIA A100 SXM GPUs, CUDA, NCCL, and Linux host validation.
- Connected benchmark evidence to business-facing readiness narratives.
- Preserved proprietary boundaries by publishing methodology and sanitized artifacts only.
- Treated missing evidence as a documented limitation instead of inventing metrics.

## Deep-Dive Prompts

### Why NCCL?

NCCL collectives are core to distributed AI training. They validate whether GPUs can communicate efficiently for common patterns such as gradient synchronization, tensor gathering, and sharded reduction.

### Why AllReduce first?

AllReduce maps directly to gradient synchronization and is one of the most common bottlenecks in multi-GPU training.

### How do you prevent benchmark documentation from becoming marketing fluff?

Every numeric statement links to raw output. Missing outputs are explicitly marked as not included.

### How do you talk about GPUValidator publicly?

GPUValidator is referenced only as a proprietary internal platform that generated and organized evidence. The public repository demonstrates engineering methodology, not private implementation.
