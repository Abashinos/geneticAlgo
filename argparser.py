# coding=utf-8
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='N queens')

    parser.add_argument('-N', action='store', type=int, dest='size', required=True, help='Board size')
    parser.add_argument('-L', action='store', type=long, dest='limit', required=True, help='Population limit')
    parser.add_argument('-R', action='store', type=int, dest='retries', required=True, help='Retries limit')

    return parser.parse_args()