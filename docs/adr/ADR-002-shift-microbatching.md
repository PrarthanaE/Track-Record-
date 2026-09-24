# ADR-002: Shift-Based Micro-Batch Ingestion over Real-Time Streaming

## Status
Accepted

## Context
Cellular connectivity is sparse across rural Central Queensland track networks, preventing reliable real-time streaming (Kafka/Kinesis) from moving track cars.

## Decision
Buffer readings on vehicle storage during inspection runs and upload batch archives to Amazon S3 Bronze upon arrival at network-enabled depots.

## Consequences
- Prevents failures caused by rural connectivity dropouts.
- Precludes instant in-cab alerts because processing occurs post-run.
