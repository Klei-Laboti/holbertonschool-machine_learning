#!/usr/bin/env python3
"""Module që llogarit shape-in (përmasat) e një matrice."""


def matrix_shape(matrix):
    """Kthen shape-in e një matrice si listë numrash të plotë."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
