from collections import Counter

def max_varieties(T):
    counts = Counter(T)
    given = []
    remaining_to_give = len(T) // 2
    for item in list(counts):
        if remaining_to_give > counts[item]:
            given.append(item * counts[item])
            remaining_to_give -= counts[item]
        else:
            given += [item] * remaining_to_give
            result = T.copy()
            for i in given:
                result.remove(i)
            return len(set(result))

// given a list of items, keep half of the quantity, and give away as many duplicates as possible 
// ie from these 10, give away 5 of the eights.
// how many different types remaining?
// 1000,12345,and some 8s

x = max_varieties([8, 8, 1000, 8, 8, 8, 8, 8, 8, 12345] )
print(x) //3
