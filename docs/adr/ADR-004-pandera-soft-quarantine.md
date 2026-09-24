# ADR-004: Soft Quarantine Dead-Letter Routing over Execution Abortion

## Status
Accepted

## Context
Track geometry cars capture millions of readings. Aborting batch jobs on a single corrupted reading causes unnecessary failures for multi-kilometre inspection runs.

## Decision
Enforce schema checks with Pandera. Divert invalid records to an S3 quarantine prefix with diagnostic bitmasks (`quality_flag: 1=Interpolated, 2=Degraded`), allowing clean rows to continue processing.

## Consequences
- Protects downstream metrics while keeping pipeline execution uninterrupted.
- Requires downstream modules to filter or account for quality bitmasks.
