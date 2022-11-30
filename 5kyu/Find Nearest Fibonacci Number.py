# https://www.codewars.com/kata/5ca22e6b86eed5002812061e/train/python
def nearest_fibonacci(n):
    a, b = 0, 1
    while b<n:
        a, b = b, a+b
    return b if b-n<n-a else a