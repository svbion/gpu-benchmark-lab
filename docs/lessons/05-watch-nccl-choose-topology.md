# Lesson 5: Watch NCCL Choose Topology

## Objective

Use captured H200 evidence to see how NCCL discovers topology, imports network information, and selects available transports without inventing missing graph details.

## Hardware used

- Provider: RunPod
- Visible GPUs: 5 x NVIDIA H200
- Peer topology: NV18 between every visible GPU pair
- P2P: NVLink/read/write/atomic matrices report OK

## Commands used

- `nvidia-smi -L`
- `nvidia-smi topo -m`
- `nvidia-smi topo -p2p n|r|w|a`
- `nvidia-smi nvlink --status`
- `NCCL_DEBUG=INFO NCCL_TOPO_DUMP_FILE=nccl-topology.xml ./all_reduce_perf ...`

## Evidence excerpts

Benchmark header shows five ranks on sanitized host labels and NVIDIA H200 devices. Topology evidence shows NV18 for every GPU-to-GPU off-diagonal pair. NVLink status reports 18 links per visible GPU at 26.562 GB/s. Debug logs include NCCL topology import and Socket transport fallback lines after `libnccl-net.so`/`libibverbs` were unavailable in the environment.

## Rings, trees, and channels

NCCL may build rings, trees, and channels during graph search. This lesson only reports rings/trees/channels when explicit lines appear in the captured debug logs. See `parsed/nccl-graph.json`; missing fields are limitations, not hidden assumptions.

## Troubleshooting comparison: SYS vs NVLink

A common managed-cloud failure mode is active NVLink-capable hardware with `SYS` peer topology and `NS` P2P NVLink status for the allocated pair. GPU fabric validation treats that as WARNING, not PASS, because physical link activity alone does not prove peer-visible NVLink connectivity.

## Interview Q&A

Q: Is H200 model name enough to claim NVLink?
A: No. Use topology and P2P matrices as decisive evidence.

Q: Can a log line mentioning Socket mean GPU collectives used only Ethernet?
A: Not by itself. NCCL may initialize network transports even for single-node runs. Interpret it with topology, P2P, XML, and benchmark context.

Q: Should you infer NVSwitch from NV18?
A: You can describe a fully connected logical NVLink fabric and discuss NVSwitch only when evidence supports it. Do not draw an exact physical switch layout from `topo -m` alone.
