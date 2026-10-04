#!/usr/bin/env python3
"""Module që bashkon dy matrica 2D përgjatë një aksi."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Bashkon dy matrica 2D përgjatë axis-it të dhënë.

    axis=0 shton rreshta, axis=1 shton kolona.
    Kthen None nëse shape-et s'përputhen për atë aks.
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [mat1[i] + mat2[i] for i in range(len(mat1))]
    return None
