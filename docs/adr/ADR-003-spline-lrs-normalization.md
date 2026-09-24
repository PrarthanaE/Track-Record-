# ADR-003: Spline-Based Linear Chainage Resampling over Map-Matching

## Status
Accepted

## Context
Track maintenance systems index assets strictly along linear chainage (Line ID, Track ID, Kilometre Post). Raw distance sensor pings arrive at irregular intervals due to train speed changes and wheel slip.

## Decision
Use SciPy 1D cubic spline interpolation along recorded chainage to resample data into uniform 0.25 m increments.

## Consequences
- Operates directly within the civil engineering coordinate frame (AS 7635 / QR standards).
- Requires pre-assigned track identifiers; does not infer track switches from 2D coordinates.
