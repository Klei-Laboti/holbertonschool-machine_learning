#!/usr/bin/env python3
"""Plots a histogram of student grades for Project A."""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Plot a histogram of grades with bins every 10 units."""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    plt.hist(student_grades, bins=bins, edgecolor="black")
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title("Project A")
    plt.axis([0, 100, 0, 30])
    plt.show()
