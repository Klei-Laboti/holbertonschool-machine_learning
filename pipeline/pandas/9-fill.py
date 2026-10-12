#!/usr/bin/env python3
"""Cleans missing values across several columns."""


def fill(df):
    """Drop Weighted_Price; fill Close, OHL, and volumes as specified."""
    df = df.drop(columns=["Weighted_Price"])
    df["Close"] = df["Close"].ffill()
    for col in ["High", "Low", "Open"]:
        df[col] = df[col].fillna(df["Close"])
    for col in ["Volume_(BTC)", "Volume_(Currency)"]:
        df[col] = df[col].fillna(0)
    return df
