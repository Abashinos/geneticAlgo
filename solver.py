from typing import List, Tuple
from crossover import get_crossover_function

import argparser
import random

class Solver:

    def __init__(self, args: dict = vars(argparser.parse_args())):
        self.board_size = args['board_size']
        self.initial_population_size = max(args['initial_population'], self.board_size)
        self.max_population_size = args['population_size'] if args.get('population_size') else 0
        self.generation_limit = args['generation_limit']
        self.mutation_chance = args.get('mutation_chance', 0.0)
        self.crossover = get_crossover_function(args.get('crossover_type'))
        self.crossover_strategy = max(min(args.get('crossover_strategy'), 1), 0.01)
        self.selection_percent = max(min(args['selection'], 1), 0.01) if args.get('selection') else 1
        self.population = []

    @staticmethod
    def gene_error(gene, chromosome):
        return len(
            list(
                filter(
                    lambda other_gene: other_gene[0] == gene[0] or
                                       other_gene[1] == gene[1] or
                                       abs(other_gene[0] - gene[0]) == abs(other_gene[1] - gene[1]), chromosome)
            )
        ) - 1

    @staticmethod
    def _fitness(chromosome: List):
        return sum(map(lambda gene: Solver.gene_error(gene, chromosome), chromosome)) / 2

    @staticmethod
    def fitness(chromosome: List[int]):
        return Solver._fitness(list(enumerate(chromosome)))

    @staticmethod
    def population_fitness(chromosomes: List[List]):
        return list(map(Solver.fitness, chromosomes))

    def generate_population(self):
        self.population = [
            sorted(list(range(self.board_size)), key=lambda k: random.random())
            for _ in range(self.initial_population_size)
        ]

    def test(self):
        chromosomes = [[1, 3, 0, 2], [0, 1, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
        fitness = Solver.population_fitness(chromosomes)
        assert fitness == [0, 2, 4, 6]

        crossover_chromosomes = [[3, 0, 1, 2, 4], [3, 2, 1, 4, 0]]
        child = get_crossover_function('crossover')(crossover_chromosomes)[0]
        print(child)
        assert (child[0], child[2]) == (3, 1)

    def run(self):
        self.generate_population()
        selected_population_count = round(len(self.population) * self.selection_percent)
        print(selected_population_count)
        print("{0} {1}\nPopulation: {2}".format(self.board_size, self.mutation_chance, self.population))


if __name__ == "__main__":
    solver = Solver()
    solver.test()
    solver.run()
