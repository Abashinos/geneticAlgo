import random

from typing import List


def mutate(chromosomes: List[List[int]], probability: float):

    def mutate_one(chromosome: List[int]):
        for i in range(len(chromosome)):
            if random.random() < probability:
                j = chromosome.index(i)
                chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
        return chromosome

    return [mutate_one(chromosome) for chromosome in chromosomes]
