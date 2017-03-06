import random

from typing import List


def crossover(chromosomes: List[List[int]], chromosome_length: int):
    chromosomes_number = len(chromosomes)
    children = []
    for i in range(chromosomes_number - 1):
        for j in range(i + 1, chromosomes_number):
            first = chromosomes[i]
            second = chromosomes[j]
            child = []
            different_elements = []

            # Fill common elements and mark others with a sentinel value
            for k in range(chromosome_length):
                if first[k] == second[k]:
                    child.append(first[k])
                else:
                    child.append(-1)
                    different_elements.append(first[k])
            random.shuffle(different_elements)

            # Fill shuffled remaining elements
            for k in range(chromosome_length):
                if child[k] == -1:
                    child[k] = different_elements.pop()

            children.append(child)
    return children


def gemmation(chromosomes: List[List[int]], chromosome_length: int):
    children = []
    for chromosome in chromosomes:
        child = chromosome.copy()
        i, j = random.randrange(chromosome_length), random.randrange(chromosome_length)
        child[i], child[j] = child[j], child[i]
        children.append(child)
    return children


def get_crossover_function(name):
    return ({
        'crossover': crossover,
        'gemmation': gemmation,
        'default': crossover
    }).get(name, crossover)
