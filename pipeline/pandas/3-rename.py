#!/usr/bin/env python3
"""Renames the Timestamp column to Datetime and formats it."""
import pandas as pd


def rename(df):
    """Rename Timestamp to Datetime; keep only Datetime and Close."""
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    return df[["Datetime", "Close"]]
