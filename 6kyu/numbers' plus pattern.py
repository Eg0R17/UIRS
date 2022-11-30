# https://www.codewars.com/kata/563cb92e0996a4ac0b000042/train/python
def pattern(n):
    upper = [str(i % 10).rjust(n) for i in range(1, n)]
    return '\n'.join(upper +
                     [''.join(str(i % 10) for i in list(range(1, n)) + list(range(n, 0, -1)))] +
                     upper[::-1]) + '\n'