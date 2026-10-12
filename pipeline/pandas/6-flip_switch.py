#!/usr/bin/env python3
"""Sorts in reverse chronological order and transposes."""


def flip_switch(df):
    """Sort rows reverse-chronologically, then transpose the frame."""
    return df.sort_values("Timestamp", ascending=False).transpose()
