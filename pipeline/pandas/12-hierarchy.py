#!/usr/bin/env python3
"""Builds a MultiIndex with Timestamp as the first level."""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Concat bitstamp & coinbase over a timestamp range, Timestamp first."""
    df1 = index(df1)
    df2 = index(df2)
    df1 = df1.loc[1417411980:1417417980]
    df2 = df2.loc[1417411980:1417417980]
    df = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
    df = df.reorder_levels([1, 0])
    return df.sort_index()
