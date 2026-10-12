#!/usr/bin/env python3
"""Sets the Timestamp column as the index."""


def index(df):
    """Return df indexed by the Timestamp column."""
    return df.set_index("Timestamp")
