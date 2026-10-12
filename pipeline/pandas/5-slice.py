#!/usr/bin/env python3
"""Extracts selected columns and every 60th row."""


def slice(df):
    """Return High, Low, Close, Volume_(BTC); every 60th row."""
    df = df[["High", "Low", "Close", "Volume_(BTC)"]]
    return df.iloc[::60]
