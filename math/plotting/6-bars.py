#!/usr/bin/env python3
"""Plots a stacked bar graph of fruit per person."""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """Plot the number of each fruit per person as stacked bars."""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    people = ["Farrah", "Fred", "Felicia"]
    colors = ["red", "yellow", "#ff8000", "#ffe5b4"]
    labels = ["apples", "bananas", "oranges", "peaches"]
    width = 0.5

    bottom = np.zeros(3)
    for i in range(4):
        plt.bar(people, fruit[i], width=width, color=colors[i],
                label=labels[i], bottom=bottom)
        bottom += fruit[i]

    plt.ylabel("Quantity of Fruit")
    plt.title("Number of Fruit per Person")
    plt.ylim(0, 80)
    plt.yticks(range(0, 81, 10))
    plt.legend()
    plt.show()
