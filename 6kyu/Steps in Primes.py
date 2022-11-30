# https://www.codewars.com/kata/5613d06cee1e7da6d5000055/train/python
import math
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def step(g, m, n):
    if m >= n:
        return []
    else:
        for i in range(m, n + 1 - g):
            if isPrime(i) and isPrime(i + g):
                return [i, i + g]
