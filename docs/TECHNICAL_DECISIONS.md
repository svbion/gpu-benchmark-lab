# Technical Decisions

> Public release boundary: this repository documents engineering methodology, sanitized evidence references, benchmark interpretation, and executive reporting. GPUValidator is proprietary software. No source code, product internals, API contracts, database schemas, authentication/RBAC design, agent protocol, customer data, private URLs, secrets, or production screenshots are included.

## Decision 1: Use a Separate Public Repository

A separate repository protects the proprietary GPUValidator platform and keeps the public artifact focused on methodology, evidence discipline, and communication quality.

## Decision 2: Reframe the Story Around Enterprise Validation

The repository was reframed from simple GPU benchmarking to engineering an enterprise GPU benchmarking and validation environment. This better reflects the real work: lab setup, validation scope, evidence capture, benchmark interpretation, reporting, and risk communication.

## Decision 3: Quote Only Evidence-Linked Metrics

Numeric benchmark values are quoted only from the included sanitized fixture. Methodology-only benchmarks are explicitly labeled as not having public output.

## Decision 4: Replace Production Screenshots

Production application screenshots were removed for RC1 because they exposed UI surfaces, user names, cluster labels, report controls, status panels, and implementation-adjacent details. They were replaced with conceptual public-safe visuals.

## Decision 5: Describe GPUValidator at a Commercial Boundary

GPUValidator is described as proprietary software with high-level capabilities. Implementation, APIs, database design, auth/RBAC, agent protocols, and source code remain private.

## Decision 6: Optimize for Three Readers

Docs are structured for recruiters, AI compute engineering interviewers, and enterprise/investor readers. Each page reinforces the same narrative without overstating evidence.
