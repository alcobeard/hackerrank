import timeit
import random


def breakbadsp(ar):
    return ar.count(max(ar))


def aida71(ar):
    max_h = ar[0]
    max_n = 1
    for c in ar[1:]:
        if c > max_h:
            max_h = c
            max_n = 1
        elif c == max_h:
            max_n += 1
    return max_n


random.seed()
arr = list(random.sample(range(10**9),5))

print(timeit.timeit('breakbadsp(arr)', globals=globals()))
print(timeit.timeit('aida71(arr)', globals=globals()))