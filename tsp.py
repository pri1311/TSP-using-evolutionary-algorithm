import random
import itertools
import matplotlib.pyplot as plt
import time
import numpy as np
from usa_data import USA_map

from helper import (
    getX, getY, distance, getCities, tourLength, shortestTour, allTours, reverse_segment_if_better, lines, Coordinate_map, read_cities, tspPlot, all_segments, performancePlot,
)

from GAhelper import (createInitialPopulation, orderCrossover, partiallyMappedCrossover, cycleCrossover,
                      generateOffspring, createCandidates, tournamentSelection, mutate, getSelectionType, getMutationType)

city = complex


def nearestNeighbor(cities, start=None):
    n = len(cities)
    citiesList = list(cities)
    if start is None:
        start = citiesList[0]
    shortesttour = [start]
    citiesList.remove(start)
    c = shortesttour[0]

    while len(shortesttour) != n:
        cost = 100000000
        best = None
        for ci in citiesList:
            if distance(c, ci) < cost:
                cost = distance(c, ci)
                best = ci
        shortesttour.append(best)
        citiesList.remove(best)
        c = best

    return shortesttour


def repeatedNearestNeighbor(cities):
    cost = 100000000
    tour = None
    performance = []
    plt.rcParams["figure.figsize"] = (12, 5)
    plt.tight_layout()

    for c in cities:
        temptour = nearestNeighbor(cities, c)
        tempcost = tourLength(temptour)
        performance.append(tempcost)
        if tempcost < cost:
            cost = tempcost
            tour = temptour
        plt.pause(0.05)
        plt.clf()
        performancePlot(performance)

        tspPlot(temptour)

    plt.show()

    return tour


def alter_tour(tour):
    original_length = tourLength(tour)
    for (start, end) in all_segments(len(tour)):
        reverse_segment_if_better(tour, start, end)

    if tourLength(tour) < original_length:
        return alter_tour(tour)
    return tour


def geneticAlgorithm(cities, iterations=2000, num_candidates=200, mutation_rate=0.05, num_elite=20, greedy_seed=10, selection_type=1, mutation_type=1):
    file = open("output.txt", "a")
    candidates = createInitialPopulation(
        cities, num_candidates, greedy_seed)
    bestSolution = shortestTour(candidates)
    bestCost = tourLength(bestSolution)
    sorted(candidates, key=tourLength)

    fitness = []
    plt.rcParams["figure.figsize"] = (15, 5)
    plt.tight_layout()

    n = 0

    while n <= iterations:
        elite = candidates[:num_elite]
        offsprings = generateOffspring(
            tours=candidates, num_offsprings=num_candidates - num_elite, selection_type=seletion_type)
        mutate(offsprings=offsprings, n=len(bestSolution),
               mutation_rate=mutation_rate, mutation_type=mutation_type)

        candidates = offsprings + elite

        tempBest = shortestTour(candidates)
        tempCost = tourLength(tempBest)
        fitness.append(tempCost)
        if tempCost < bestCost:
            plt.pause(0.05)
            bestSolution = tempBest
            bestCost = tempCost
            file.write(
                f"Generation: {n} Minimum Tour Length: {round(tempCost,4)}\n")

        plt.pause(0.05)
        plt.clf()
        performancePlot(fitness)

        tspPlot(tour=tempBest, subplot=True, iteration=n)

        n += 1

    plt.show()
    file.close()

    return bestSolution


if __name__ == "__main__":
    print("1. Generate Random Cities")
    print("2. USA Map")
    print("3. Run on Test Case")
    choice = int(input())

    if choice == 1:
        print("Enter the number of cities: ", end="")
        num_cities = int(input())

        cities = getCities(num_cities)

    elif choice == 2:
        cities = USA_map

    else:
        cities = read_cities(64)

    iterations = int(input("Number of Iterations: "))
    num_candidates = int(input("Population Size: "))
    elite = int(input("Number of Elite Parents: "))
    greedy_seed = int(input("Number of Greedy Seed: "))
    mutation_rate = float(input("Mutation Rate: "))
    seletion_type = getSelectionType()
    mutation_type = getMutationType()

    plt.rcParams["figure.figsize"] = (5, 5)
    tspPlot(list(cities), subplot=False,
            title="Initial Tour with tour length " + str(round(tourLength(list(cities)), 4)))
    plt.savefig('initial tour.png')

    plt.rcParams["figure.figsize"] = (15, 5)
    shortesttour = geneticAlgorithm(cities=cities, iterations=iterations, num_candidates=num_candidates,
                                    num_elite=elite, mutation_rate=mutation_rate, greedy_seed=greedy_seed, selection_type=seletion_type, mutation_type=mutation_type)

    print("Solution found with length: ", end="")
    print(tourLength(shortesttour))

    plt.rcParams["figure.figsize"] = (5, 5)
    tspPlot(shortesttour, subplot=False, title="Optimized Tour with tour length " +
            str(round(tourLength(shortesttour), 4)))
    plt.show()
