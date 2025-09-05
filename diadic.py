#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:21:45 2025

@author: vishweshpalani
"""

import matplotlib.pyplot as plt
import itertools
import math

def generate_dyadic(b):
    exp = 2**b
    points = []
    for i in range(1, exp+1):
        points.append((i/exp, b))
    return points

def plot_n(n):
    points = []
    for b in range(1, n+1):
        points += generate_dyadic(b)
    # Sort by x, then by y (to group duplicates and find min y)
    coordinates_sorted = sorted(points, key=lambda t: (t[0], t[1]))
    filtered_sorted = [next(group) for _, group in itertools.groupby(coordinates_sorted, key=lambda t: t[0])]

    x, y = zip(*filtered_sorted)
    plt.plot(x, y, 'x', color='red', markersize=3)  # Alternative using plot with markers

    # Add labels/title
    plt.xlabel('Fraction')
    plt.ylabel('Bits')
    plt.title('Plotting Unordered (x, y) Tuples')
    plt.legend()
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    n = 3
    plot_n(n)
    
        
    