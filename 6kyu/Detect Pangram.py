# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True