# System Architecture

> Evidence policy: this public repository contains documentation, sanitized evidence references, screenshots, and report examples only. GPUValidator is a proprietary internal enterprise platform and remains private. No GPUValidator source code, backend, frontend, authentication, agent implementation, APIs, business logic, or enterprise architecture is included.


## Public Benchmark Lab Architecture

```mermaid
flowchart TD
    RP[RunPod GPU Instance] --> HW[4 x NVIDIA A100 SXM GPUs]
    HW --> LINUX[Linux Host Environment]
    LINUX --> CUDA[NVIDIA Driver + CUDA Runtime]
    CUDA --> NCCL[NCCL Tests]
    NCCL --> BENCH[Collective Benchmarks]
    BENCH --> RAW[Raw Output Evidence]
    RAW --> DOCS[Portfolio Documentation]
    DOCS --> RESUME[Resume + Interview Materials]
```

## Evidence-to-Report Architecture

```mermaid
flowchart LR
    RAW[Raw Benchmark Output] --> PARSE[Evidence Review]
    PARSE --> FINDINGS[Technical Findings]
    FINDINGS --> RISK[Operational Meaning]
    RISK --> REPORTS[Executive and Technical Reports]
    REPORTS --> AUDIENCE[Engineering, Management, Customer Review]
```

## Proprietary Boundary

```mermaid
flowchart TD
    GV[GPUValidator proprietary internal platform] --> BE[Benchmark Engine]
    BE --> EC[Evidence Collection]
    EC --> RG[Reports]
    RG --> PUB[Sanitized public documentation]

    subgraph Excluded from this repository
      SRC[Source code]
      API[APIs]
      AUTH[Authentication]
      FE[Frontend]
      BCK[Backend]
      LOGIC[Business logic]
      AGENT[Agent implementation]
    end

    SRC -. excluded .-> PUB
    API -. excluded .-> PUB
    AUTH -. excluded .-> PUB
    FE -. excluded .-> PUB
    BCK -. excluded .-> PUB
    LOGIC -. excluded .-> PUB
    AGENT -. excluded .-> PUB
```
