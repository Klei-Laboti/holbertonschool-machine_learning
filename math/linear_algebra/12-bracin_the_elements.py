#!/usr/bin/env python3
"""Module për operacione element-për-element në NumPy."""


def np_elementwise(mat1, mat2):
    """Kthen tuple: shuma, diferenca, prodhimi, pjesëtimi (element-wise)."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
