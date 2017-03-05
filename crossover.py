import random

from typing import List


def crossover(chromosomes: List[List[int]]):
    children = []
    for i in range(len(chromosomes) - 1):
        for j in range(i + 1, len(chromosomes)):
            first = chromosomes[i]
            second = chromosomes[j]
            child = []
            different_elements = []

            # Fill common elements and mark others with a sentinel value
            for k in range(len(first)):
                if first[k] == second[k]:
                    child.append(first[k])
                else:
                    child.append(-1)
                    different_elements.append(first[k])
            random.shuffle(different_elements)

            # Fill shuffled remaining elements
            for k in range(len(first)):
                if child[k] == -1:
                    child[k] = different_elements.pop()

            children.append(child)
    return children


def gemmation(chromosomes: List[List[int]]):
    return None  # TODO


def get_crossover_function(name):
    return ({
        'crossover': crossover,
        'gemmation': gemmation,
        'default': crossover
    }).get(name, crossover)
