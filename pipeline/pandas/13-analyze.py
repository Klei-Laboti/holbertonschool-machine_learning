#!/usr/bin/env python3
"""Computes descriptive statistics for all columns but Timestamp."""


def analyze(df):
    """Return describe() for every column except Timestamp."""
    return df.drop(columns=["Timestamp"]).describe()
