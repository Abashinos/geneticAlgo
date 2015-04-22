from copy import copy
import random
import sys
from argparser import parse_args


def get_children(parents, limit):
    total_errors = 0
    for parent in parents:
        parent['errors'] = 0
        for i in range(0, len(parent['places'])-1):
            for j in range(i+1, len(parent['places'])):
                if (j - i) == abs(parent['places'][j] - parent['places'][i]):
                    parent['errors'] += 1
        total_errors += parent['errors']
    total_errors //= N-1

    ok_parents = []
    for parent in parents:
        if parent['errors'] <= total_errors:
            ok_parents.append(parent)
    print(len(ok_parents))

    children = []
    for i in range(0, len(ok_parents)-1):
        for j in range(i+1, len(ok_parents)):
            if len(children) >= limit:
                break

            child = {'id': i, 'parents': (i, j), 'errors': 0, 'places': copy(ok_parents[i]['places'])}
            fixed = []

            for k in range(0, N):
                if ok_parents[i]['places'][k] == ok_parents[j]['places'][k]:
                    fixed.append((k, ok_parents[i]['places'][k]))

            random.shuffle(child['places'])

            for pos, item in fixed:
                index = child['places'].index(item)
                child['places'][pos], child['places'][index] = child['places'][index], child['places'][pos]

            children.append(child)

        if len(children) >= limit:
            break

    min_error = (0, sys.maxint)
    for child in children:
        for i in range(0, len(child['places'])-1):
            for j in range(i+1, len(child['places'])):
                if (j - i) == abs(child['places'][j] - child['places'][i]):
                    child['errors'] += 1
        if min_error[1] > child['errors']:
            min_error = (child['places'], child['errors'])
        if min_error[1] == 0:
            break

    return min_error[1], min_error[0], children

if __name__ == '__main__':
    args = parse_args()
    N = args.size

    retries = 0
    min_error = sys.maxint

    while min_error > 0:
        parents = [{'places': [x for x in range(0, N)], 'errors': 0} for x in range(0, N)]
        for parent in parents:
            random.shuffle(parent['places'])

        min_error = sys.maxint
        best_child = []
        while min_error > 0:
            if len(parents) <= 0 or len(parents) >= args.limit:
                break
            min_error, best_child, parents = get_children(parents, args.limit)

        print(min_error, best_child)
