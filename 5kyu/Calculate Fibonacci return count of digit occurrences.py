# https://www.codewars.com/kata/5779f894ec8832493f00002d/train/python
memo=[0, 1]
def fib_digits(n):
    if len(memo)==2:
        for i in range(2, 100001):
            memo.append(memo[i-1]+memo[i-2])
    num=str(memo[n])
    res=[]
    for i in range(0,10):
        check=num.count(str(i))
        if check:
            res.append((check, i))
    return sorted(res, reverse=True)