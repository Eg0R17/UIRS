#  https://www.codewars.com/kata/590bb735517888ae6b000012/train/python
def sum_prod_diags(m):
    s, n = 0, len(m)
    for d in 0, -1:
        for x in range(n):
            h = v = 1
            for u in range(n-x):
                h *= m[u ^ d][x+u]
                if x: v *= m[(x+u) ^ d][u]
            s += (d | 1) * (h + v)
    return s