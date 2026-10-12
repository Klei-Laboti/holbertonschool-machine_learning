#!/usr/bin/env python3
"""Sorts a DataFrame by the High price in descending order."""


def high(df):
    """Return df sorted by High, highest first."""
    return df.sort_values("High", ascending=False)
