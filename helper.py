import random
import itertools
from typing import Iterator
import matplotlib.pyplot as plt
import time
import csv
import numpy as np

city = complex


def getX(A):
    return A.real


def getY(A):
    return A.imag


def distance(A, B):
    return abs(A - B)


def getCities(n, a=200, b=200):
    return {city(random.randrange(0, a), random.randrange(0, b)) for i in range(0, n)}


def tourLength(tour):
    return sum(distance(tour[i], tour[i-1]) for i in range(len(tour)))


def shortestTour(tours):
    return min(tours, key=tourLength)


def reverse_segment_if_better(tour, i, j):
    try:
        A, B, C, D = tour[i-1], tour[i], tour[j-1], tour[j % len(tour)]
        if distance(A, B) + distance(C, D) > distance(A, C) + distance(B, D):
            tour[i:j] = reversed(tour[i:j])
    except:
        pass


def lines(text): return text.strip().splitlines()


def Coordinate_map(lines, delimiter=' ', lat_col=1, long_col=2, lat_scale=69, long_scale=-48):
    return set(city(long_scale * float(row[long_col]),
                    lat_scale * float(row[lat_col]))
               for row in csv.reader(lines, delimiter=delimiter, skipinitialspace=True))


def read_cities(size):
    cities = []
    with open(f'test_data/cities_{size}.data', 'r') as handle:
        lines = handle.readlines()
        for line in lines:
            x, y = map(float, line.split())
            cities.append(city(x, y))
    return set(cities)


def allTours(cities):
    return itertools.permutations(cities)


def all_segments(N):
    return [(start, start + length)
            for length in range(N, 2-1, -1)
            for start in range(N - length + 1)]


def tspPlot(tour, subplot=True, iteration=1, title=""):
    x = [getX(i) for i in tour]
    y = [getY(i) for i in tour]

    x.append(x[0])
    y.append(y[0])

    if subplot:
        plt.subplot(1, 2, 1)

    plt.plot(x, y, marker='o', color='c', lw=1)
    plt.xlabel("X - axis")
    plt.ylabel("Y - axis")

    if len(tour) < 50:

        # zip joins x and y coordinates in pairs
        for a, b in zip(x, y):

            label = f"({a},{b})"

            plt.annotate(label,  # this is the text
                         (a, b),  # these are the coordinates to position the label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, 5),  # distance from text to points (x,y)
                         fontsize=10)

    if subplot:
        axes = plt.gca()
        y_min, y_max = axes.get_ylim()
        x_min, x_max = axes.get_xlim()

        label = f"Distance: {round(tourLength(tour),2)}"
        generation = f"Generation: {iteration}"
        plt.text(x_min + abs(x_max / 25), y_min + y_max / 25, label)
        plt.text(x_min + abs(x_max / 25), y_min + (2 * y_max) / 25, generation)
        plt.title(f"TSP visualization")

    else:
        plt.title(title)

    # if iteration % 250 == 0:
    #     name = f"fig{iteration / 250}.png"
    #     plt.savefig(name)


def performancePlot(a):
    plt.subplot(1, 2, 2)
    x = range(0, len(a))
    y = a

    plt.xlabel("Number of Iteration")
    plt.ylabel("Best tour length")
    plt.title("GA Performance")

    plt.plot(x, y, color='c', lw=1)
