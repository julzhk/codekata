from collections import defaultdict

if __name__ == '__main__':
    no_cols = int(input())
    d = defaultdict(int)
    for _ in range(no_cols):
        *col_name, col_val = input().split(' ')
        d[' '.join(col_name)] += int(col_val)
    for key, val in d.items():
        print(key, val)
