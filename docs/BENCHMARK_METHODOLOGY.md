# Benchmark Methodology

> Evidence policy: this public repository contains documentation, sanitized evidence references, screenshots, and report examples only. GPUValidator is a proprietary internal enterprise platform and remains private. No GPUValidator source code, backend, frontend, authentication, agent implementation, APIs, business logic, or enterprise architecture is included.


## Principles

1. Evidence first: every numeric claim must link to raw output.
2. Safe execution: commands should be bounded and approved.
3. Reproducibility: record command shape, GPU count, runtime versions, and output files.
4. Separation of concerns: public documentation describes methodology, not proprietary implementation.
5. No invented metrics: absent data is documented as absent.

## Standard NCCL Command Shape

The exact command path can vary by installation, but NCCL Tests commonly follow this pattern:

```bash
./build/all_reduce_perf -b 8M -e 8G -f 2 -g 4 -w 5 -n 20
```

The included AllReduce evidence reports equivalent parameters in its header:

```text
# nThread 1 nGpus 4 minBytes 8388608 maxBytes 8589934592 step: 2(factor) warmup iters: 5 iters: 20 validation: 1
```

## Evidence Capture Checklist

- Command name
- NCCL version
- CUDA version
- Driver version
- GPU count/model
- Message-size range
- Warmup iterations
- Measured iterations
- Validation/correctness status
- Raw output file path
- Screenshot reference, if available

## Collective Coverage

Detailed benchmark explanations are in [Benchmark results](BENCHMARK_RESULTS.md).
