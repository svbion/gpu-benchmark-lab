# Technical Decisions

> Evidence policy: this public repository contains documentation, sanitized evidence references, screenshots, and report examples only. GPUValidator is a proprietary internal enterprise platform and remains private. No GPUValidator source code, backend, frontend, authentication, agent implementation, APIs, business logic, or enterprise architecture is included.


## Decision 1: Separate Public Repository

A separate repository prevents accidental modification or exposure of GPUValidator source code and keeps the public artifact focused on portfolio documentation.

## Decision 2: Evidence-Linked Claims Only

Numeric benchmark results are quoted only from included raw output files. Missing output is documented as missing.

## Decision 3: High-Level GPUValidator References

GPUValidator is named only as a proprietary internal enterprise platform. Implementation details, APIs, backend, frontend, authentication, validation logic, reporting code, benchmark engine code, and agent code are excluded.

## Decision 4: Mermaid for Architecture

Mermaid diagrams keep architecture readable, text-based, reviewable, and GitHub-friendly.

## Decision 5: Report Narratives Without Private Export Code

Report documentation describes report types and evidence transformation. It does not publish proprietary generation logic.
