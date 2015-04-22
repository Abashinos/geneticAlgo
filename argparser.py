# coding=utf-8
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='N queens')

    parser.add_argument('-N', action='store', type=int, dest='board_size', required=True, help='Board size')
    parser.add_argument('-L', action='store', type=long, dest='limit', required=True, help='Population limit')
    parser.add_argument('-M', action='store', type=int, dest='mutation', help='Mutation chance percent')
    parser.add_argument('-R', action='store', type=int, dest='retries', help='Retries limit')

    return parser.parse_args()