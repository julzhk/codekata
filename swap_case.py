# save actual stdin in case we need it again later
from pprint import pprint

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

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
