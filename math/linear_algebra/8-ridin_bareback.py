#!/usr/bin/env python3
"""Module që bën shumëzimin e dy matricave."""


def mat_mul(mat1, mat2):
    """Shumëzon dy matrica.

    Kthen një matricë të re, ose None nëse kolonat e mat1
    s'barazohen me rreshtat e mat2.
    """
    if len(mat1[0]) != len(mat2):
        return None
    rows_a, cols_a = len(mat1), len(mat1[0])
    cols_b = len(mat2[0])
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += mat1[i][k] * mat2[k][j]
            result[i][j] = total
    return result
