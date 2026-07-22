# NCCL

> Public release boundary: this repository documents engineering methodology, sanitized evidence references, benchmark interpretation, and executive reporting. GPUValidator is proprietary software. No source code, product internals, API contracts, database schemas, authentication/RBAC design, agent protocol, customer data, private URLs, secrets, or production screenshots are included.

## Documented NCCL Evidence

The included fixture reports:

```text
NCCL version 2.25.1+cuda12.8
```

All numeric NCCL claims in this repository are limited to the fixture rows in [Benchmark results](BENCHMARK_RESULTS.md).

## Why NCCL Matters

NCCL is the communication layer commonly used by distributed AI frameworks for GPU collectives. Multi-GPU training and inference systems depend on reliable communication for gradient synchronization, activation movement, parameter distribution, and rank-to-rank tensor exchange.

## Collective Operations Covered

| Collective | Public status | Infrastructure relevance |
| :--- | :--- | :--- |
| AllReduce | Fixture rows included | Gradient synchronization and replicated reduction |
| AllGather | Methodology only | Gathering rank-local shards to all ranks |
| ReduceScatter | Methodology only | Sharded reduction and optimizer efficiency |
| Broadcast | Methodology only | Root-to-rank distribution |
| Reduce | Methodology only | Root-centric aggregation |
| AllToAll | Methodology only | Expert-parallel and transpose-style exchange |
| SendRecv | Methodology only | Targeted point-to-point data movement |

## Troubleshooting Signals

A senior GPU infrastructure review should consider launch failures, missing GPUs, driver/runtime mismatch, degraded fabric, out-of-bounds correctness failures, low bandwidth relative to topology, and missing provenance. This repository discusses those concepts without publishing private incident data.
