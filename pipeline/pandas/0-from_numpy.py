#!/usr/bin/env python3
"""Creates a pd.DataFrame from a np.ndarray."""
import pandas as pd


def from_numpy(array):
    """Return a pd.DataFrame with capitalized alphabetical column labels."""
    columns = [chr(65 + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=columns)
