# Benchmark Methodology

> Public release boundary: this repository documents engineering methodology, sanitized evidence references, benchmark interpretation, and executive reporting. GPUValidator is proprietary software. No source code, product internals, API contracts, database schemas, authentication/RBAC design, agent protocol, customer data, private URLs, secrets, or production screenshots are included.

## Principles

1. Evidence first: every numeric claim must link to a public artifact.
2. Safe execution: commands should be bounded, approved, and non-destructive.
3. Reproducibility: record command shape, GPU count, runtime versions, message range, iteration counts, and output location.
4. Correctness: treat validation failures and `#wrong` values as first-class findings.
5. Separation of concerns: public docs explain method and interpretation, not proprietary implementation.
6. Honesty: absent evidence is documented as absent.

## Standard NCCL Command Shape

The command path can vary by installation, but NCCL Tests commonly follow this pattern:

```bash
./build/all_reduce_perf -b 8M -e 8G -f 2 -g 4 -w 5 -n 20
```

The included fixture reports equivalent parameters:

```text
# nThread 1 nGpus 4 minBytes 8388608 maxBytes 8589934592 step: 2(factor) warmup iters: 5 iters: 20 validation: 1
```

## Evidence Capture Checklist

| Evidence item | Why it matters |
| :--- | :--- |
| Command name and arguments | Reproducibility and scope |
| NCCL/CUDA/driver versions | Runtime compatibility |
| GPU count and model | Hardware scope |
| Message-size range | Performance interpretation |
| Warmup/measured iterations | Methodology quality |
| Validation/correctness status | Acceptance confidence |
| Raw output or fixture status | Claim provenance |
| Redaction record | Public-release safety |

## Benchmark Interpretation

- Algorithm bandwidth describes useful data movement reported by the benchmark.
- Bus bandwidth is an NCCL-derived communication-efficiency view and should not be overgeneralized without topology context.
- Message-size scaling is expected; small messages are often latency-sensitive and large messages are often bandwidth-sensitive.
- A result with `#wrong = 0` is a correctness signal, not a complete hardware-health certification.

## Collective Coverage

Detailed benchmark explanations are in [Benchmark results](BENCHMARK_RESULTS.md).
