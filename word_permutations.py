from collections import defaultdict

if __name__ == '__main__':
    no_lines = int(input())
    d = defaultdict(int)
    for _ in range(no_lines):
        word = input()
        d[word] += 1

    print(len(d))
    print(*d.values())
