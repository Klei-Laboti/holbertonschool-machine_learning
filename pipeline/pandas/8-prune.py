#!/usr/bin/env python3
"""Removes rows where Close has NaN values."""


def prune(df):
    """Return df with rows dropped where Close is NaN."""
    return df.dropna(subset=["Close"])
