from collections import deque

if __name__ == '__main__':
    no_lines = int(input())
    d = deque()
    fn_case = {
        'append': lambda x: d.append(x),
        'appendleft': lambda x: d.appendleft(x),
        'pop': lambda x: d.pop(),
        'popleft': lambda x: d.popleft()
    }

    for _ in range(no_lines):
        fn_name, fn_arg = [*input().split(' '), ''][:2]
        fn_case[fn_name](fn_arg)

    print(*d)
