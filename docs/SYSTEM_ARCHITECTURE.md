# System Architecture

> Public release boundary: this repository documents engineering methodology, sanitized evidence references, benchmark interpretation, and executive reporting. GPUValidator is proprietary software. No source code, product internals, API contracts, database schemas, authentication/RBAC design, agent protocol, customer data, private URLs, secrets, or production screenshots are included.


## Public Benchmark Lab Architecture

```mermaid
flowchart TD
    RP[Authorized RunPod GPU lab] --> LINUX[Linux host validation]
    LINUX --> GPU[NVIDIA GPU inventory]
    GPU --> RUNTIME[Driver, CUDA, and NCCL evidence]
    RUNTIME --> TESTS[NCCL Tests]
    TESTS --> OUTPUT[Sanitized output fixture]
    OUTPUT --> ANALYSIS[Benchmark interpretation]
    ANALYSIS --> DOCS[Public documentation and reports]
```

## Evidence-to-Report Architecture

```mermaid
flowchart LR
    RAW[Raw or sanitized evidence] --> REVIEW[Evidence review]
    REVIEW --> FINDINGS[Technical findings]
    FINDINGS --> RISK[Operational risk and readiness meaning]
    RISK --> REPORTS[Executive, customer, and management reports]
    REPORTS --> PORTFOLIO[Portfolio, resume, and interview artifacts]
```

## Proprietary Boundary

```mermaid
flowchart TD
    subgraph PUB[Public Repository]
      METHOD[Engineering methodology]
      SAFE[Sanitized evidence references]
      NARRATIVE[Public report narratives]
      LANDING[Portfolio landing page]
    end

    subgraph PRIV[Proprietary Software Boundary]
      GV[GPUValidator]
      INTERNAL[Implementation details withheld]
    end

    GV -. named only at high level .-> METHOD
    INTERNAL -. not included .-> METHOD
```

## What Is Intentionally Not Published

- Source code or directory structures from GPUValidator.
- API endpoints, database schemas, authentication/RBAC design, agent protocols, message formats, deployment topology, secrets, hostnames, or customer data.
- Production product screenshots.
- Benchmark metrics without public evidence.
