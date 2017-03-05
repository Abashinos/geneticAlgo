from copy import copy
import random
import time
from argparser import parse_args


def get_children(parents, limit, board_size, mutation=0):
    total_errors = 0
    for parent in parents:
        parent['errors'] = 0
        for i in range(0, len(parent['places'])-1):
            for j in range(i+1, len(parent['places'])):
                if (j - i) == abs(parent['places'][j] - parent['places'][i]):
                    parent['errors'] += 1
        total_errors += parent['errors']
    total_errors //= board_size-1

    ok_parents = []
    for parent in parents:
        if parent['errors'] <= total_errors:
            ok_parents.append(parent)

    random.shuffle(ok_parents)

    children = []
    min_error = ([], 99999999)
    for i in range(0, len(ok_parents)-1):
        for j in range(i+1, len(ok_parents)):

            child = {'id': i, 'parents': (i, j), 'errors': 0, 'places': copy(ok_parents[i]['places'])}
            fixed = []

            for k in range(0, board_size):
                if ok_parents[i]['places'][k] == ok_parents[j]['places'][k]:
                    fixed.append((k, ok_parents[i]['places'][k]))

            random.shuffle(child['places'])

            for pos, item in fixed:
                index = child['places'].index(item)
                child['places'][pos], child['places'][index] = child['places'][index], child['places'][pos]

            if mutation >= random.randint(1, 100):
                a = random.randint(0, board_size-1)
                b = random.randint(0, board_size-1)
                child['places'][a], child['places'][b] = child['places'][b], child['places'][a]

            for ii in range(0, len(child['places'])-1):
                for jj in range(ii+1, len(child['places'])):
                    if (jj - ii) == abs(child['places'][jj] - child['places'][ii]):
                        child['errors'] += 1
            if min_error[1] > child['errors']:
                min_error = (child['places'], child['errors'])
            if min_error[1] == 0:
                break

            children.append(child)
            if len(children) >= limit or min_error[1] == 0:
                break

        if len(children) >= limit or min_error[1] == 0:
            break

    print(len(children))
    return min_error[1], min_error[0], children

if __name__ == '__main__':
    args = parse_args()
    N = args.board_size
    pop_limit = args.limit
    mutation = args.mutation if args.mutation else 0

    retries = 0
    error = 99999999

    while error > 0:
        parents = [{'places': [x for x in range(0, N)], 'errors': 0} for x in range(0, N)]
        for parent in parents:
            random.shuffle(parent['places'])

        error = 99999999
        best_child = []

        start = time.time()
        while error > 0:
            if len(parents) <= 0 or len(parents) >= pop_limit:
                break

            error, best_child, parents = get_children(parents, limit=pop_limit, board_size=N, mutation=mutation)
        end = time.time()

        print("Epoch = {}s".format(end - start))
        print(error, best_child)
