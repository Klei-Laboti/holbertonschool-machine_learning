#!/usr/bin/env python3
"""Module që transpozon një matricë 2D."""


def matrix_transpose(matrix):
    """Kthen transpozimin e një matrice 2D (rreshtat bëhen kolona)."""
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]
