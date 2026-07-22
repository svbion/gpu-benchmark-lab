# NCCL

> Evidence policy: this public repository contains documentation, sanitized evidence references, screenshots, and report examples only. GPUValidator is a proprietary internal enterprise platform and remains private. No GPUValidator source code, backend, frontend, authentication, agent implementation, APIs, business logic, or enterprise architecture is included.


## Documented NCCL Evidence

The included raw file reports:

```text
NCCL version 2.25.1+cuda12.8
```

Source: [redacted-real-nccl-all-reduce.txt](../evidence/raw/nccl/redacted-real-nccl-all-reduce.txt).

## Why NCCL Matters

NCCL is the communication substrate commonly used by distributed AI frameworks for GPU collectives. Even on a single node, multi-GPU training depends on reliable collective behavior for gradient synchronization, tensor gathering, model/pipeline parallel communication, and distributed optimizer traffic.

## Collective Operations Covered

- AllReduce
- AllGather
- ReduceScatter
- Broadcast
- Reduce
- AllToAll
- SendRecv

See [Benchmark methodology](BENCHMARK_METHODOLOGY.md) and [Benchmark results](BENCHMARK_RESULTS.md).
