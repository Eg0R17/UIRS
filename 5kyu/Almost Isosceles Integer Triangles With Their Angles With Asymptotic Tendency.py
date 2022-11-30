# https://www.codewars.com/kata/5be4d000825f24623a0001e8/train/python
def find_closest_perim(p):
    x, y, z = 97, 28, 28
    while p > y:
        x, y, z = 7 * x + 24 * y, 7 * y + 2 * x, y
    return y if y - p <= p - z else z