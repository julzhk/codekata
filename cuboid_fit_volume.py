# save actual stdin in case we need it again later

STD_IN = [
    '1',
    '1',
    '1',
    '2'
]


def input():
    return STD_IN.pop(0)


from itertools import product



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    combinations = [s for s in product(range(x + 1), range(y + 1), range(z + 1))]
    print([list(c) for c in combinations if sum(c) != n])
