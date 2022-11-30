# https://www.codewars.com/kata/5a3267b2ee1aaead3d000037/train/python
from itertools import product
dict={'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3, 'G': 4, 'H': 4, 'I': 4, 'J': 5, 'K': 5, 'L': 5, 'M': 6, 'N': 6, 'O': 6, 'P': 7, 'Q': 7, 'R': 7, 'S': 7, 'T': 8, 'U': 8, 'V': 8, 'W': 9, 'X': 9, 'Y': 9, 'Z': 9}
dict2={2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}
def check1800(s):
    temp=s.split("-")
    word=temp[-2]+temp[-1]
    word1=[dict2[dict[i]] for i in word[:3]]
    word2=[dict2[dict[i]] for i in word[:4]]
    word3=[dict2[dict[i]] for i in word[3:]]
    word4=[dict2[dict[i]] for i in word[4:]]
    list1=["".join(i) for i in product(*word1) if "".join(i) in WORDS]
    list2=["".join(i) for i in product(*word2) if "".join(i) in WORDS]
    list3=["".join(i) for i in product(*word3) if "".join(i) in WORDS]
    list4=["".join(i) for i in product(*word4) if "".join(i) in WORDS]
    return {f"1-800-{i}-{j}" for i,j in product(list1, list3)} | {f"1-800-{i}-{j}" for i,j in product(list2, list4)}