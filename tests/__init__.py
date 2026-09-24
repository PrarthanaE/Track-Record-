"""Sample tests for synthetic data generation and schema contract compliance."""

from contracts.rail_geometry import RailGeometryIngestionContract
from src.synthetic_generator import generate_synthetic_run


def test_synthetic_data_schema_compliance():
    df = generate_synthetic_run(km_length=2.0)
    # Validates DataFrame directly against the Pandera contract
    validated_df = RailGeometryIngestionContract.validate(df)
    assert validated_df.height > 0
    assert "gauge_mm" in validated_df.columns
    assert "chainage_kp" in validated_df.columns


def test_gauge_narrow_gauge_bounds():
    df = generate_synthetic_run(km_length=1.0)
    # AS 7635 physical boundaries
    assert df["gauge_mm"].min() >= 1040.0
    assert df["gauge_mm"].max() <= 1100.0
