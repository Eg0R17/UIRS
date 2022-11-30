# https://www.codewars.com/kata/5592dd43a9cd0e43a800019e/train/python
def diagonals(matrix):
    def skewed(left, right):
        tilted = [[None] * l + row + [None] * r for l, row, r in zip(left, matrix, right)]
        return [[x for x in row if x is not None] for row in zip(*tilted)]

    left, right = range(len(matrix)), range(len(matrix) - 1, -1, -1)
    return matrix if len(matrix) < 2 else skewed(left, right) + skewed(right, left)