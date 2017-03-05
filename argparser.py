# coding=utf-8
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='N queens problem')

    parser.add_argument('-n', '-N', '--size', type=int, dest='board_size', required=True,
                        help='Board size')
    parser.add_argument('-p', '--initial_population', type=int, dest='initial_population',
                        help='Initial population size', default=0)
    parser.add_argument('-g', '-G', '--generations', type=int, dest='generation_limit',
                        help='Generation limit', default=100)
    parser.add_argument('-m', '-M', '--mutation_chance', type=float, dest='mutation_chance',
                        help='Mutation chance percent', default=0.0)
    parser.add_argument('-c', '--crossover_type', type=str, dest='crossover_type',
                        help='Crossover type', default='')
    parser.add_argument('-C', '--crossover_strategy', type=float, dest='crossover_strategy',
                        help='Fraction of population participating in crossover', default=0.5)
    parser.add_argument('-v', '-V', '--verbose', dest='verbose', action='store_true',
                        help='Flag which determines if every step should be printed')

    exclusive_group = parser.add_mutually_exclusive_group()
    exclusive_group.add_argument('-P', '--max_population', type=int, dest='population_size',
                        help='Max population size', default=0)
    exclusive_group.add_argument('-s', '-S', '--selection', type=float, dest='selection',
                        help='Fraction of selected population after each epoch', default=0.5)

    return parser.parse_args()
