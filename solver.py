from functools import partial
from typing import List
from crossover import get_crossover_function
from mutation import mutate

import argparser
import random


class Solver:

    def __init__(self, args: dict = None):
        if not args:
            args = vars(argparser.parse_args())

        self.board_size = args['board_size']
        self.initial_population_size = max(args['initial_population'], self.board_size)
        self.max_population_size = args['max_population'] if args.get('max_population') else 0
        self.generation_limit = args['generation_limit']
        self.mutate = mutate
        self.mutation_chance = args.get('mutation_chance', 0.0)
        self.crossover = partial(get_crossover_function(args.get('crossover_type')), chromosome_length=self.board_size)
        self.crossover_percent = max(min(args.get('crossover_percent'), 1), 0.01)
        self.selection_percent = max(min(args.get('selection'), 1), 0.01) if args.get('selection') else 1
        self.verbose = args['verbose']

        self.population = []
        self.current_generation = 0

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
        return sum(map(lambda gene: Solver.gene_error(gene, chromosome), chromosome)) // 2

    @staticmethod
    def fitness(chromosome: List[int]):
        return Solver._fitness(list(enumerate(chromosome)))

    def map_population_with_fitness(self, population, sort=True):
        mapped_population = [(candidate, self.fitness(candidate)) for candidate in population]
        return sorted(mapped_population, key=lambda k: k[1]) if sort else mapped_population

    def set_population(self, population: List[List[int]]):
        self.population = self.map_population_with_fitness(population)

    def add_to_population(self, new_candidates: List[List[int]]):
        self.population = sorted(self.population + self.map_population_with_fitness(new_candidates, sort=False), key=lambda k: k[1])

    def generate_population(self):
        self.set_population([
            sorted(list(range(self.board_size)), key=lambda k: random.random())
            for _ in range(self.initial_population_size)
        ])

    def print_current_status(self, step=""):
        print("\n{0}\nCurrent status\nGeneration #{1}\nPopulation size: {2}\nPopulation sorted by fitness:\n{3}"
              .format(step, self.current_generation, len(self.population), self.population))

    def test(self):
        pass

    def run(self):
        # Generate initial population
        self.generate_population()
        # TODO: print initial data

        self.current_generation = 0
        while self.current_generation <= self.generation_limit or self.generation_limit == 0:
            if self.verbose:
                self.print_current_status("New generation step")

            # Add crossover results to population
            crossover_participants_count = round(len(self.population) * self.crossover_percent)
            self.add_to_population(self.crossover([candidate[0] for candidate in self.population[:crossover_participants_count]]))

            # Find best candidate
            best_candidate = self.population[0]
            self.current_generation += 1

            if self.verbose:
                self.print_current_status("Crossover step")

            if best_candidate[1] == 0:
                print("We have a winner: {0}".format(best_candidate[0]))
                break
            else:
                print("The closest we've got is: {0}. Candidate: {1}".format(best_candidate[1], best_candidate[0]))
                if self.current_generation >= self.generation_limit != 0:
                    break

            # Mutate population
            self.set_population(self.mutate([candidate[0] for candidate in self.population],
                                            self.board_size,
                                            self.mutation_chance))
            if self.verbose:
                self.print_current_status("Mutation step")

            # Filter best candidates for the new generation
            if self.max_population_size <= 0:
                selected_population_count = round(len(self.population) * self.selection_percent)
                self.population = self.population[:selected_population_count]
            else:
                self.population = self.population[:self.max_population_size]

            if self.verbose:
                self.print_current_status("Selection step")


if __name__ == "__main__":
    solver = Solver()
    solver.test()
    solver.run()
