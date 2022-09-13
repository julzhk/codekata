# save actual stdin in case we need it again later
STD_IN = ['qwewrtyuiopasdfghjklzxcvbnm', ]



def input():
    return STD_IN.pop(0)

from collections import Counter

if __name__ == '__main__':
    word = input()
    counter = Counter(word)
    d = counter.most_common()
    d.sort(key=lambda x: x[1] + (ord('z') - ord(x[0]))/100, reverse=True)
    for i in d[:3]:
        print(i[0], i[1])
