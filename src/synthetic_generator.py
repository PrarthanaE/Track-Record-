"""
Synthetic rail geometry generator.
Simulates track runs with nominal 1067 mm gauge, track curves, and realistic noise.
Rough draft needs to be revised.
"""

from datetime import datetime, timedelta
import numpy as np
import polars as pl


def generate_synthetic_run(
    km_length: float = 10.0,
    nominal_spacing_m: float = 0.25,
    noise_level: float = 0.5,
    seed: int = 42,
) -> pl.DataFrame:
    np.random.seed(seed)
    total_points = int((km_length * 1000.0) / nominal_spacing_m)

    # Base chainage and timestamps
    chainage_kp = np.linspace(0.0, km_length, total_points)
    start_time = datetime(2026, 9, 1, 8, 0, 0)
    timestamps = [start_time + timedelta(seconds=i * 0.05) for i in range(total_points)]

    # Gauge around nominal 1067 mm (Queensland narrow gauge)
    gauge_mm = 1067.0 + np.random.normal(0.0, noise_level, total_points)

    # Smooth curve and track profile deviations
    spatial_freq = np.linspace(0, 10 * np.pi, total_points)
    top_vertical_profile_mm = 3.0 * np.sin(spatial_freq) + np.random.normal(0, 0.3, total_points)
    twist_short_base_mm = 1.5 * np.cos(spatial_freq * 1.5) + np.random.normal(0, 0.2, total_points)
    twist_long_base_mm = twist_short_base_mm * 1.2
    versine_alignment_mm = 4.0 * np.sin(spatial_freq * 0.5) + np.random.normal(0, 0.4, total_points)
    cant_superelevation_mm = 25.0 * np.sin(spatial_freq * 0.2)

    # Quality flag: 0 = Valid
    quality_flag = np.zeros(total_points, dtype=np.int32)
    latency_sec = np.random.exponential(scale=0.1, size=total_points)

    return pl.DataFrame({
        "timestamp": timestamps,
        "line_code": ["CQCN_BLACKWATER"] * total_points,
        "track_id": ["MAIN_UP"] * total_points,
        "chainage_kp": chainage_kp,
        "gauge_mm": gauge_mm,
        "top_vertical_profile_mm": top_vertical_profile_mm,
        "twist_short_base_mm": twist_short_base_mm,
        "twist_long_base_mm": twist_long_base_mm,
        "versine_alignment_mm": versine_alignment_mm,
        "cant_superelevation_mm": cant_superelevation_mm,
        "acquisition_latency_sec": latency_sec,
        "quality_flag": quality_flag,
    })


if __name__ == "__main__":
    df = generate_synthetic_run(km_length=5.0)
    print(f"Generated {df.height} synthetic inspection rows.")
    print(df.head(5))
