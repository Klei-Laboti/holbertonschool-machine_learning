#!/usr/bin/env python3
"""Plots two exponential-decay curves on the same figure."""
import numpy as np
import matplotlib.pyplot as plt


def two():
    """Plot C-14 (dashed red) and Ra-226 (solid green) decay."""
    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(x, y1, "r--", label="C-14")      # vija e kuqe e ndërprerë
    plt.plot(x, y2, "g-", label="Ra-226")     # vija jeshile e plotë
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.title("Exponential Decay of Radioactive Elements")
    plt.xlim(0, 20000)                        # boshti x: 0–20000
    plt.ylim(0, 1)                            # boshti y: 0–1
    plt.legend(loc="upper right")             # legjenda lart-djathtas
    plt.show()
