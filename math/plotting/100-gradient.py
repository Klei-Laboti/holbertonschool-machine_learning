#!/usr/bin/env python3
"""Plots a scatter of sampled elevations on a mountain with a colorbar."""
import numpy as np
import matplotlib.pyplot as plt


def gradient():
    """Scatter x vs y, colored by elevation z, with a labeled colorbar."""
    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))
    plt.figure(figsize=(6.4, 4.8))

    plt.scatter(x, y, c=z)              # ngjyra sipas lartësisë z
    plt.colorbar(label="elevation (m)")  # colorbar me etiketë
    plt.xlabel("x coordinate (m)")
    plt.ylabel("y coordinate (m)")
    plt.title("Mountain Elevation")
    plt.show()
