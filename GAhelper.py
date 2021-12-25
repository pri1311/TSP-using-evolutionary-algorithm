import random
from helper import tourLength, reverse_segment_if_better, distance


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


def greedyCandidates(cities, greedy_seed):
    candidates = []
    for i in range(0, greedy_seed):
        startCity = random.choice(list(cities))
        candidates.append(nearestNeighbor(cities, startCity))

    return candidates


def createInitialPopulation(cities, num_candidates, greedy_seed):
    candidates = createCandidates(cities, num_candidates - greedy_seed)
    candidates.extend(greedyCandidates(cities, greedy_seed))
    return candidates


def orderCrossover(p1, p2):
    n = len(p1)
    a, b = random.randint(0, n - 1), random.randint(0, n - 1)

    if a > b:
        a, b = b, a

    c1 = p1[a:b+1]
    c2 = p2[a:b+1]

    c1 = list(set(c1).union(set(p2)))
    c2 = list(set(c2).union(set(p1)))

    return c1, c2


def partiallyMappedCrossover(p1, p2):
    n = len(p1)
    a, b = random.randint(0, n - 1), random.randint(0, n - 1)
    if a > b:
        a, b = b, a

    c1 = [None for i in range(0, n)]
    c2 = [None for i in range(0, n)]
    set1 = {}
    set2 = {}

    for i in range(a, b + 1):
        c1[i] = p1[i]
        set1[p1[i]] = p2[i]
        set2[p2[i]] = p1[i]
        c2[i] = p2[i]

    for i in range(0, a):
        if p1[i] not in c2:
            c2[i] = p1[i]

        if p2[i] not in c1:
            c1[i] = p2[i]

    for i in range(b + 1, n):
        if p1[i] not in c2:
            c2[i] = p1[i]

        if p2[i] not in c1:
            c1[i] = p2[i]

    for i in range(0, n):
        if c1[i] is None:
            x = set1[p2[i]]
            while x in c1:
                x = set1[x]
            c1[i] = x

        if c2[i] is None:
            x = set2[p1[i]]
            while x in c2:
                x = set2[x]
            c2[i] = x

    return c1, c2


def cycleCrossover(tours):
    pass


def tournamentSelection(tours, n, k):
    newTours = []
    for i in range(0, int(n / 2)):
        parentCandidates = sorted([random.choice(tours)
                                  for i in range(0, k)], key=tourLength)
        p1, p2 = parentCandidates[0], parentCandidates[1]
        c1, c2 = partiallyMappedCrossover(p1, p2)
        newTours.append(c1)
        newTours.append(c2)

    return newTours


def randomSelection(tours, n):
    newTours = []
    for i in range(0, int(n / 2)):
        p1, p2 = random.choice(tours), random.choice(tours)
        c1, c2 = partiallyMappedCrossover(p1, p2)
        newTours.append(c1)
        newTours.append(c2)

    return newTours


def rouletteWheelSelection(tours, n):

    pass


def rankSelection(tours, n):
    sorted(tours, key=tourLength)
    i = 0
    newTours = []
    while i < n:
        c1, c2 = partiallyMappedCrossover(tours[i], tours[i + 1])
        newTours.append(c1)
        newTours.append(c2)

        i += 2

    return newTours


def generateOffspring(tours, num_offsprings=180,  selection_type=3, tournament_k=4):
    newTours = []
    n = len(tours)
    if selection_type == 1:
        newTours = rankSelection(tours, n)

    elif selection_type == 2:
        newTours = randomSelection(tours, num_offsprings)

    elif selection_type == 3:
        newTours = tournamentSelection(tours, num_offsprings, tournament_k)

    newTours = sorted(newTours, key=tourLength)
    return newTours[: num_offsprings]


def createCandidates(citiesSet, num_candidates=200):
    cities = list(citiesSet)
    return [random.sample(cities, len(cities)) for i in range(0, num_candidates)]


def swapEdgeMutation(tour, i, j):
    reverse_segment_if_better(tour, i, j)


def swapMutation(tour, i, j):
    newTour = tour.copy()
    newTour[i], newTour[j] = newTour[j], newTour[i]
    if tourLength(newTour) < tourLength(tour):
        return newTour

    return tour


def scrambleMutation(tour, i, j):
    oldTour = tour.copy()
    newTour = oldTour[i:j+1]
    random.shuffle(newTour)
    oldTour[i:j+1] = newTour

    if tourLength(oldTour) < tourLength(tour):
        return oldTour
    else:
        return tour


def inversionMutation(tour, i, j):
    oldTour = tour.copy()
    newTour = oldTour[i:j+1]
    newTour.reverse()
    oldTour[i:j+1] = newTour

    if tourLength(oldTour) < tourLength(tour):
        return oldTour
    else:
        return tour


def generateRandomAB(n):
    a, b = random.randint(0, n - 1), random.randint(0, n - 1)
    a, b = min(a, b), max(a, b)
    return a, b


def mutate(offsprings, n, mutation_rate=0.05, mutation_type=1):
    j = -1
    for i in range(0, int(len(offsprings) * mutation_rate)):
        a, b = generateRandomAB(n)
        if mutation_type == 1:
            swapMutation(offsprings[i], a, b)
        if mutation_type == 2:
            swapEdgeMutation(offsprings[i], a, b)
        elif mutation_type == 3:
            offsprings[i] = scrambleMutation(offsprings[i], a, b)
        else:
            offsprings[i] = inversionMutation(offsprings[i], a, b)

        j -= 1


def getSelectionType():
    print("Select Selection Type: ")

    print("1. Rank Selection")
    print("2. Random Selection")
    print("3. Tournament Selection")

    choice = int(input())
    return choice


def getMutationType():
    print("Select Mutation Type: ")
    print("1. Swap Mutation")
    print("2. Swap Edge Mutation")
    print("3. Scramble Mutation")
    print("4. Inversion Mutation")

    choice = int(input())
    return choice
