STD_IN = [
    "7",
    "UK",
    "China",
    "USA",
    "France",
    "New Zealand",
    "UK",
    "France"
]


def input():
    try:
        return STD_IN.pop(0)
    except IndexError:
        return None


def country_count(s):
    result = set()
    for i in range(int(s)):
        result.add(input())
    print(len(result))


if __name__ == '__main__':
    count = input()
    country_count(count)
