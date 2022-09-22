from collections import defaultdict

STD_IN = [
    '5',
    'Harry',
    '37.21',
    'Berry',
    '37.21',
    'Tina',
    '37.2',
    'Akriti',
    '41',
    'Harsh',
    '39',
]


def input():
    return STD_IN.pop(0)


if __name__ == '__main__':
    data = defaultdict(list)
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data[score].append(name)
    score = sorted(data.keys())[1]
    result = sorted(data[score])
    print("\n".join(result))
