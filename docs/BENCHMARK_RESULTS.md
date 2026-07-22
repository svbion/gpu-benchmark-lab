# Benchmark Results

> Public release boundary: this repository documents engineering methodology, sanitized evidence references, benchmark interpretation, and executive reporting. GPUValidator is proprietary software. No source code, product internals, API contracts, database schemas, authentication/RBAC design, agent protocol, customer data, private URLs, secrets, or production screenshots are included.


## Evidence Manifest

| Artifact | Type | Public status | Notes |
| :--- | :--- | :--- | :--- |
| [redacted-real-nccl-all-reduce.txt](../evidence/raw/nccl/redacted-real-nccl-all-reduce.txt) | NCCL Tests text fixture | Redacted real-format fixture | Preserves output structure and selected non-sensitive values; must not be represented as customer evidence |
| [benchmark-lab-overview.svg](../assets/public/benchmark-lab-overview.svg) | Conceptual visual | Public-safe illustration | Replaces production screenshots |
| [evidence-to-report.svg](../assets/public/evidence-to-report.svg) | Conceptual visual | Public-safe illustration | Shows documentation flow only |
| [gpuvalidator-boundary.svg](../assets/public/gpuvalidator-boundary.svg) | Conceptual visual | Public-safe illustration | Shows public/private boundary only |

## AllReduce

### Purpose

AllReduce combines values from every GPU rank and returns the reduced result to every rank.

### Communication Pattern

Every rank contributes data; every rank receives the reduced result.

### Typical AI Use Case

Distributed data-parallel training gradient synchronization.

### Command Shape

```bash
./build/all_reduce_perf -b 8M -e 8G -f 2 -g 4 -w 5 -n 20
```

### Evidence

Fixture: [redacted-real-nccl-all-reduce.txt](../evidence/raw/nccl/redacted-real-nccl-all-reduce.txt)

Important limitation: this is a redacted real-format fixture, not customer evidence and not a complete certification artifact.

### Quoted Fixture Rows

| Size bytes | Count | Type | Reduction | Time | Alg BW | Bus BW | Wrong |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| 8388608 | 2097152 | float | sum | 315.2 | 26.61 | 39.91 | 0 |
| 67108864 | 16777216 | float | sum | 720.1 | 93.19 | 139.78 | 0 |
| 1073741824 | 268435456 | float | sum | 6941.0 | 154.69 | 185.67 | 0 |
| 8589934592 | 2147483648 | float | sum | 47000 | 182.76 | 185.67 | 0 |

Raw footer:

```text
# Avg bus bandwidth    : 37.3098
# Out of bounds values : 0 OK
```

### Lessons Learned

- Correctness matters as much as throughput; the quoted rows show `#wrong` as `0`.
- Larger payloads in the fixture report higher bandwidth than small payloads, consistent with bandwidth-sensitive scaling.
- The fixture is useful for methodology and interpretation, but publication-quality customer acceptance would require approved raw evidence, topology context, and provenance.

## Methodology-Only Benchmarks

| Benchmark | Purpose | Public status | Publication rule |
| :--- | :--- | :--- | :--- |
| AllGather | Gather rank-local tensors from all GPUs to all GPUs | Methodology only | Add metrics only after approved raw output exists |
| ReduceScatter | Reduce across ranks and scatter result shards | Methodology only | Add metrics only after approved raw output exists |
| Broadcast | Send one root tensor to every rank | Methodology only | Add metrics only after approved raw output exists |
| Reduce | Reduce all ranks to one root rank | Methodology only | Add metrics only after approved raw output exists |
| AllToAll | Exchange unique shards between all ranks | Methodology only | Add metrics only after approved raw output exists |
| SendRecv | Point-to-point pair communication | Methodology only | Add metrics only after approved raw output exists |

## Executive Interpretation

The public artifact demonstrates benchmark literacy, evidence discipline, and communication quality. It does not certify a customer cluster or disclose proprietary benchmark orchestration.
