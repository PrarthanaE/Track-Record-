"""
Data contract and schema definitions for rail telemetry ingestion.
Enforces physical boundaries defined in AS 7635:2020 and Aurizon documentation.
"""

import pandera.polars as pa
import polars as pl


class RailGeometryIngestionContract(pa.DataFrameModel):
    # Temporal and Linear Referencing Keys
    timestamp: pl.Datetime = pa.Field(nullable=False)
    line_code: pl.String = pa.Field(nullable=False)
    track_id: pl.String = pa.Field(nullable=False)
    chainage_kp: pl.Float64 = pa.Field(ge=0.0, le=3000.0, nullable=False)

    # Track Geometry Deviations (AS 7635 / SAF-STD-0077-CIV-NET Module 9 Limits)
    gauge_mm: pl.Float64 = pa.Field(ge=1040.0, le=1100.0)
    top_vertical_profile_mm: pl.Float64 = pa.Field(ge=-50.0, le=50.0)
    twist_short_base_mm: pl.Float64 = pa.Field(ge=-40.0, le=40.0)
    twist_long_base_mm: pl.Float64 = pa.Field(ge=-50.0, le=50.0)
    versine_alignment_mm: pl.Float64 = pa.Field(ge=-60.0, le=60.0)
    cant_superelevation_mm: pl.Float64 = pa.Field(ge=-100.0, le=200.0)

    # Audit and Data Quality Metadata
    acquisition_latency_sec: pl.Float64 = pa.Field(ge=0.0)
    quality_flag: pl.Int32 = pa.Field(isin=[0, 1, 2])  # 0: Valid, 1: Interpolated, 2: Degraded

    class Config:
        strict = True
        coerce = True
