# Track-Record-
Capstone Project | Automated Rail Telemetry Ingestion Pipeline &amp; Metric Validation Architecture for Queensland Heavy-Haul Networks

# Rail Telemetry Ingestion Pipeline & Metric Validation Architecture

A cloud-based rail data ingestion pipeline and condition metric validation engine for the Central Queensland Coal Network (CQCN).

## Pipeline Architecture
1. **`ingest_validator`:** Programmatic schema enforcement with Pandera; soft-quarantines anomalous rows with diagnostic bitmasks.
2. **`lrs_resampler`:** Linear Referencing System (LRS) alignment and 1D cubic spline spatial resampling to uniform 0.25 m increments.
3. **`temporal_reconciler`:** Micro-batch packet reordering by event time and distance; bounded spline interpolation for telemetry dropouts (< 5 m).
4. **`metric_engine`:** Standard deviation calculation, 100 m segment TCI computation, corridor OTCI aggregation, and localized defect masking filters.

## Documentation
- [Project Proposal](docs/proposal.md)
- [Architectural Decision Records (ADRs)](docs/adr/)
