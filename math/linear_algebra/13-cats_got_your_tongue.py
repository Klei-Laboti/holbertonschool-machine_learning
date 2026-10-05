#!/usr/bin/env python3
"""Module që bashkon dy array NumPy përgjatë një aksi."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Bashkon dy array NumPy përgjatë axis-it të dhënë."""
    return np.concatenate((mat1, mat2), axis=axis)
