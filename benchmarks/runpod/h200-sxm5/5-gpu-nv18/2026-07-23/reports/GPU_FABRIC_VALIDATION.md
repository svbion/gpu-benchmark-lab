# GPU Fabric Validation

Result: PASS

Fully connected peer-visible NVLink fabric verified for the visible GPU set.

## Evidence-backed findings

- Visible GPU count: 5
- GPU models: NVIDIA H200
- Active NVLink links per GPU: {"GPU0": 18, "GPU1": 18, "GPU2": 18, "GPU3": 18, "GPU4": 18}
- Reported per-link rates: 26.562 GB/s
- Topology classification: fully connected NVLink fabric
- P2P read/write/atomic: PASS / PASS / PASS

This validation distinguishes NVLink-capable hardware, active physical interfaces, peer-visible topology, and P2P capabilities. It does not infer physical switch architecture beyond the captured topology/P2P evidence.
