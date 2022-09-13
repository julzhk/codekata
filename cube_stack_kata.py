from collections import deque

STD_IN = ['2',
          '6',
          '1 2 3 8 7',
          # '4 3 2 1 3 4',
          '3',
          '1 3 2'
          ]


def input():
    return STD_IN.pop(0)


def check_stackability():
    no_blocks = int(input())
    blocks = map(int, input().split(' ')[:no_blocks])
    d = deque(blocks)
    current_block = 999
    while len(d) > 0:
        if len(d) == 1:
            next_block = d.pop()
        else:
            ends = [d.popleft(), d.pop()]
            next_block = max(ends)
        if next_block > current_block:
            return False
        current_block = next_block
    return True


if __name__ == '__main__':
    no_tests = int(input())
    for _ in range(no_tests):
        print('Yes' if check_stackability() else 'No')
