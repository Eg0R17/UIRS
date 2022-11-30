# https://www.codewars.com/kata/60a516d70759d1000d532029/train/python
from itertools import accumulate
def survivors(ms, pss):
    return [i
            for i, (m, pss) in enumerate(zip(ms, pss))
            if all(m > 0 for m in accumulate(pss, lambda m, p: m - 1 + p, initial=m))]