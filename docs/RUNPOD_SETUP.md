# RunPod Setup

> Public release boundary: this repository documents engineering methodology, sanitized evidence references, benchmark interpretation, and executive reporting. GPUValidator is proprietary software. No source code, product internals, API contracts, database schemas, authentication/RBAC design, agent protocol, customer data, private URLs, secrets, or production screenshots are included.


## Scope

This document explains the public benchmark-lab setup at an engineering-method level. It does not document proprietary deployment, application, automation, or agent internals.

## Environment

| Area | Public description |
| :--- | :--- |
| Provider | RunPod |
| Shape | Single GPU node |
| GPU class | NVIDIA A100 SXM class |
| GPU count | Four GPUs in the sanitized NCCL fixture header |
| Operating model | Authorized Linux shell access through provider-approved paths |
| Benchmark focus | NCCL Tests collective communication |

## Setup Flow

1. Provision or access an authorized RunPod node with the intended GPU class.
2. Confirm the lab session is permitted for benchmark execution and evidence capture.
3. Record the validation scope: provider, node shape, GPU class, runtime versions, command family, and evidence limitations.
4. Capture passive host/GPU evidence through approved commands.
5. Run bounded NCCL Tests commands that match the published methodology.
6. Preserve raw output, sanitize sensitive identifiers, and document limitations before publication.

## Operational Guardrails

- Use only authorized provider access paths.
- Do not publish tokens, SSH material, private hostnames, raw GPU UUIDs, private URLs, or customer identifiers.
- Do not run destructive diagnostics, stress tests, service restarts, or privileged changes unless the environment owner explicitly approves them.
- Do not claim a benchmark was executed unless its output exists and is linked.
- Treat provider session expiration and billing constraints as part of the engineering record.

## Public Visuals

Production product screenshots were removed for RC1. Public visuals are conceptual placeholders under `assets/public/` and are safe for portfolio use.
