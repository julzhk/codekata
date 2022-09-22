# save actual stdin in case we need it again later

STD_IN = [
    '5',
    '2 3 6 6 5',
]


def input():
    return STD_IN.pop(0)


from itertools import product

if __name__ == '__main__':
    n = int(input())
    data = map(int, input().split(' '))
    data = sorted(list(set(data)))
    print(data[-2])
