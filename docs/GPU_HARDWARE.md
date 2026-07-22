# GPU Hardware

> Public release boundary: this repository documents engineering methodology, sanitized evidence references, benchmark interpretation, and executive reporting. GPUValidator is proprietary software. No source code, product internals, API contracts, database schemas, authentication/RBAC design, agent protocol, customer data, private URLs, secrets, or production screenshots are included.


## Public Hardware Summary

| Field | Publicly documented value |
| :--- | :--- |
| Provider | RunPod |
| Node scope | Single node |
| GPU count | 4 in sanitized fixture header |
| GPU model string | NVIDIA A100-SXM4-80GB |
| Driver evidence | 580.126.16 in sanitized fixture header |
| Topology evidence | Methodology documented; raw topology matrix not published |

## Evidence

The included NCCL fixture header contains:

```text
# GPUs: 4 x NVIDIA A100-SXM4-80GB
# Driver Version: 580.126.16
```

Source: [redacted-real-nccl-all-reduce.txt](../evidence/raw/nccl/redacted-real-nccl-all-reduce.txt).

## Engineering Relevance

Hardware validation is not just inventory. For enterprise AI infrastructure, engineers need to verify visibility, runtime compatibility, topology assumptions, benchmark correctness, and evidence provenance before recommending acceptance.

## Inventory Checklist

- GPU count and model recorded.
- Driver version recorded.
- CUDA/NCCL version linked to benchmark output.
- GPU UUIDs and provider-specific identifiers redacted or withheld.
- Topology evidence published only when approved.
- Public statements distinguish evidence, methodology, and future work.
