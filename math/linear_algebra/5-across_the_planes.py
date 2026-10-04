#!/usr/bin/env python3
"""Module që mbledh dy matrica 2D element-për-element."""


def add_matrices2D(mat1, mat2):
    """Mbledh dy matrica 2D element-për-element.

    Kthen një matricë të re, ose None nëse shape-et ndryshojnë.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
            for i in range(len(mat1))]
