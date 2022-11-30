# https://www.codewars.com/kata/5a24a35a837545ab04001614/train/python
def interlaced_spiral(s):
    n = int((s - 1) ** .5) + 1
    for x, r in enumerate(range(n, 0, -2)):
        for y in range(x, x+r-(r>1)):
            for _ in range(4):
                yield x * n + y
                if r == 1: return
                x, y = y, n-x-1

def encode(s):
    table = {j: i for i, j in enumerate(interlaced_spiral(len(s)))}
    return ''.join(s[i] if i < len(s) else ' ' for i in map(table.get, range(len(table))))

def decode(s):
    return ''.join(s[i] for i in interlaced_spiral(len(s))).rstrip()