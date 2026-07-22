# Interview Guide

> Public release boundary: this repository documents engineering methodology, sanitized evidence references, benchmark interpretation, and executive reporting. GPUValidator is proprietary software. No source code, product internals, API contracts, database schemas, authentication/RBAC design, agent protocol, customer data, private URLs, secrets, or production screenshots are included.

## Elevator Pitch

I engineered a public-safe GPU benchmarking and validation case study around a RunPod A100 SXM environment. The work shows how I validate Linux GPU infrastructure, reason about CUDA/NCCL, preserve evidence, interpret benchmark output, and translate technical findings into executive and customer-facing reports while protecting proprietary platform IP.

## Senior AI Compute Talking Points

- Established a bounded validation scope before interpreting results.
- Tracked GPU count/model, driver version, CUDA/NCCL runtime context, command shape, iterations, correctness, and evidence status.
- Used NCCL AllReduce as the first public benchmark because it maps directly to data-parallel training gradient synchronization.
- Explicitly labeled other collectives as methodology-only until approved raw output exists.
- Removed production screenshots during RC1 because public release requires IP/security discipline.

## Deep-Dive Prompts

### Why NCCL?

NCCL is central to distributed GPU workloads. It exposes practical issues around GPU visibility, runtime compatibility, topology, collective communication, correctness, and performance scaling.

### Why AllReduce first?

AllReduce is common in distributed training and easy to explain to technical and non-technical stakeholders: every rank contributes, every rank receives the reduced result.

### How do you avoid benchmark marketing fluff?

I quote only evidence-linked metrics, preserve raw or sanitized output, state limitations, avoid extrapolating beyond the scope, and separate methodology from claims.

### How do you talk about GPUValidator publicly?

GPUValidator is proprietary software. Publicly, I describe the problem it solves and the high-level capabilities it provides, but not implementation, APIs, schemas, authentication, RBAC, agent protocols, or source code.

### What would you improve next?

I would add approved raw output for more collectives, approved topology evidence, signed manifests, and CI-based documentation validation.
