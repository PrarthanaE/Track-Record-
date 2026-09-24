# ADR-001: Unified Python Pipeline Container over Microservice Images

## Status
Accepted

## Context
The rail data pipeline has four processing stages. Running them as isolated Docker images in SageMaker causes container cold-start delays and increases hourly runtime costs.

## Decision
Package all modular sub-packages (`ingest_validator`, `lrs_resampler`, `temporal_reconciler`, and `metric_engine`) into a single Docker image deployed as an AWS SageMaker `ScriptProcessor` job.

## Consequences
- Eliminates repeated startup latency and stays within the ~$114.50 AUD budget.
- Limits the ability to scale individual stages on separate instance types within a single batch pass.
