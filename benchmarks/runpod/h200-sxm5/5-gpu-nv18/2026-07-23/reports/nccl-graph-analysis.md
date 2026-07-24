# NCCL Graph Analysis

Benchmark: runpod-h200-sxm5-5gpu-nv18-20260723

## Evidence used

- NCCL topology XML: `evidence/nccl/nccl-topology.xml`
- NCCL debug logs: `evidence/nccl/nccl-debug.HOST-REDACTED.*.log`
- nvidia-smi topology: `evidence/topology/topology-matrix.txt`
- P2P matrices: `evidence/nvlink/p2p-*.txt`
- NVLink status: `evidence/nvlink/nvlink-status.txt`

## What NCCL exposed

- NCCL version: 2.25.1+cuda12.8
- Visible ranks: 5, from benchmark headers.
- Topology discovery includes GPU bus IDs: not available.
- Network plugin evidence includes Socket fallback lines and missing external plugin/libibverbs lines in the captured debug log.
- Explicit channel identifiers found: 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23.

## Interpretation

The H200 dataset shows all visible GPU pairs as NV18 in `nvidia-smi topo -m`, all peer matrices report OK, and every visible GPU reports 18 active NVLink links at 26.562 GB/s. NCCL debug evidence shows topology import and transport selection lines. Ring, tree, and channel claims are limited to explicit debug lines captured in `parsed/nccl-graph.json`; no missing graph details are inferred.

## Limitations

This report does not claim an exact physical switch layout. The logical fabric label is based on peer-visible topology and P2P/NVLink evidence.
