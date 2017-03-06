import random

from typing import List


def mutate(chromosomes: List[List[int]], chromosome_length: int, probability: float):

    def mutate_many(chromosome: List[int]):
        for i in range(chromosome_length):
            if random.random() < probability:
                j = random.randrange(chromosome_length)
                chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
        return chromosome

    def mutate_one(chromosome: List[int]):
        if random.random() < probability:
            i, j = random.randrange(chromosome_length), random.randrange(chromosome_length)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
        return chromosome

    return [mutate_one(chromosome) for chromosome in chromosomes]
