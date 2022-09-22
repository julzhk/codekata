# save actual stdin in case we need it again later

STD_IN = [
    '6 767',
    '2 488512261 423332742',
    '2 625040505 443232774',
    '1 4553600',
    '4 92134264 617699202 124100179 337650738',
    '2 778493847 932097163',
    '5 489894997 496724555 693361712 935903331 518538304',
]


def input():
    return STD_IN.pop(0)


# !/bin/python3

import os
import datetime


# Complete the time_delta function below.
def time_delta(t1: str, t2: str) -> str:
    IMPUT_TIME_FORMAT = '%a %d %b %Y %H:%M:%S %z'
    delta = datetime.datetime.strptime(t1, IMPUT_TIME_FORMAT) - datetime.datetime.strptime(t2, IMPUT_TIME_FORMAT)
    return str(abs(int(delta.total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta: str = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

print(time_delta('Sun 10 May 2015 13:54:36 -0700',
                 'Sun 10 May 2015 13:54:36 -0000')
      )
