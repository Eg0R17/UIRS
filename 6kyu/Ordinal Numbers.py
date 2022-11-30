# https://www.codewars.com/kata/52dda52d4a88b5708f000024/train/python
def ordinal(n, brief=False):
    n %= 100
    if 9 < n < 20:
        return "th"
    n %= 10
    if n == 1:
        return "st"
    if n == 2:
        return "nd"[brief:]
    if n == 3:
        return "rd"[brief:]
    return "th"