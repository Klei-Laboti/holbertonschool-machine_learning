#!/usr/bin/env python3
"""Module që mbledh dy arrays element-për-element."""


def add_arrays(arr1, arr2):
    """Mbledh dy arrays 1D element-për-element.

    Kthen një listë të re me shumat, ose None nëse gjatësitë ndryshojnë.
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
