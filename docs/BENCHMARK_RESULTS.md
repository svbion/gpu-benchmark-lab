# Benchmark Results

> Evidence policy: this public repository contains documentation, sanitized evidence references, screenshots, and report examples only. GPUValidator is a proprietary internal enterprise platform and remains private. No GPUValidator source code, backend, frontend, authentication, agent implementation, APIs, business logic, or enterprise architecture is included.


## Evidence Manifest

| Artifact | Type | Source Status | Notes |
| :--- | :--- | :--- | :--- |
| [redacted-real-nccl-all-reduce.txt](../evidence/raw/nccl/redacted-real-nccl-all-reduce.txt) | NCCL output | Redacted real-format fixture | Preserves real NCCL Tests output structure; must not be represented as customer evidence |
| [runpod-agent-online.png](../assets/screenshots/runpod/runpod-agent-online.png) | Screenshot | Supplied screenshot | Online RunPod evidence screen |
| [runpod-gpu-inventory.png](../assets/screenshots/runpod/runpod-gpu-inventory.png) | Screenshot | Supplied screenshot | GPU inventory screen |
| [runpod-hardware-validation.png](../assets/screenshots/runpod/runpod-hardware-validation.png) | Screenshot | Supplied screenshot | Hardware validation screen |
| [runpod-validation-results.png](../assets/screenshots/runpod/runpod-validation-results.png) | Screenshot | Supplied screenshot | Validation results screen |

## AllReduce

### Purpose

AllReduce combines values from every GPU rank and returns the reduced result to every rank.

### Communication Pattern

Every rank contributes data; every rank receives the final reduced data.

### Typical AI Use Case

Distributed data-parallel training gradient synchronization.

### Command

```bash
./build/all_reduce_perf -b 8M -e 8G -f 2 -g 4 -w 5 -n 20
```

### Evidence

Raw output: [redacted-real-nccl-all-reduce.txt](../evidence/raw/nccl/redacted-real-nccl-all-reduce.txt)

### Output

| Size Bytes | Count | Type | Reduction | Time | Alg BW | Bus BW | Wrong |
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

- Correctness matters as much as throughput; `#wrong` remained `0` in the included rows.
- Larger payloads exposed higher reported bus bandwidth in the raw output.
- The public repository preserves the raw output rather than restating unsupported conclusions.

## AllGather

### Purpose

AllGather collects data from every rank and makes the concatenated result available to every rank.

### Communication Pattern

Each GPU contributes a shard; all GPUs receive all shards.

### Typical AI Use Case

Tensor/model-parallel workloads that need to materialize distributed activations or parameters.

### Command

```bash
./build/all_gather_perf -b 8M -e 8G -f 2 -g 4 -w 5 -n 20
```

### Evidence

No raw public AllGather output is included in this repository. No AllGather metrics are claimed.

### Lessons Learned

Documenting the command and purpose is useful, but portfolio-grade performance claims require raw output before publication.

## ReduceScatter

### Purpose

ReduceScatter reduces values across ranks and distributes distinct output shards back to ranks.

### Communication Pattern

All ranks contribute; each rank receives a reduced shard.

### Typical AI Use Case

Distributed optimizer sharding and memory-efficient gradient reduction.

### Command

```bash
./build/reduce_scatter_perf -b 8M -e 8G -f 2 -g 4 -w 5 -n 20
```

### Evidence

No raw public ReduceScatter output is included in this repository. No ReduceScatter metrics are claimed.

### Lessons Learned

ReduceScatter is critical for scalable training, but raw evidence must be added before asserting performance.

## Broadcast

### Purpose

Broadcast sends data from one root rank to all other ranks.

### Communication Pattern

One root GPU sends; all other GPUs receive.

### Typical AI Use Case

Model weight initialization, configuration distribution, checkpoint parameter broadcast.

### Command

```bash
./build/broadcast_perf -b 8M -e 8G -f 2 -g 4 -w 5 -n 20
```

### Evidence

No raw public Broadcast output is included in this repository. No Broadcast metrics are claimed.

### Lessons Learned

Broadcast validates root-to-peer propagation behavior but should not be summarized numerically without raw output.

## Reduce

### Purpose

Reduce combines data from all ranks and returns the reduced result to one root rank.

### Communication Pattern

Many-to-one reduction.

### Typical AI Use Case

Metric aggregation, loss/statistics aggregation, rank-root summaries.

### Command

```bash
./build/reduce_perf -b 8M -e 8G -f 2 -g 4 -w 5 -n 20
```

### Evidence

No raw public Reduce output is included in this repository. No Reduce metrics are claimed.

### Lessons Learned

Reduce is useful for root-centric aggregation workflows; raw output is required for any bandwidth claim.

## AllToAll

### Purpose

AllToAll exchanges unique data blocks between every pair of ranks.

### Communication Pattern

Every rank sends distinct shards to every other rank and receives distinct shards from every other rank.

### Typical AI Use Case

Mixture-of-experts token dispatch, distributed transpose, expert parallel routing.

### Command

```bash
./build/alltoall_perf -b 8M -e 8G -f 2 -g 4 -w 5 -n 20
```

### Evidence

No raw public AllToAll output is included in this repository. No AllToAll metrics are claimed.

### Lessons Learned

AllToAll is often stress-heavy and workload-dependent; publish only with raw evidence and context.

## SendRecv

### Purpose

SendRecv measures point-to-point communication between rank pairs.

### Communication Pattern

Rank-to-rank send and receive traffic.

### Typical AI Use Case

Pipeline parallel stage transfer, custom distributed protocols, targeted tensor exchange.

### Command

```bash
./build/sendrecv_perf -b 8M -e 8G -f 2 -g 4 -w 5 -n 20
```

### Evidence

No raw public SendRecv output is included in this repository. No SendRecv metrics are claimed.

### Lessons Learned

Point-to-point evidence complements collective tests, but it needs raw output before performance conclusions.
