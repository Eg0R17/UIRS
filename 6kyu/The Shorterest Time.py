#https://www.codewars.com/kata/5953c6f8af7ac14fd4000021/train/python
def shorterest_time(n, m, speeds):
    if n == 0:
        return 0

    a, b, c, d = speeds
    return min(
        n * d,
        abs(n - m) * d + b * 2 + c + m * a,
        abs(n - m) * a + b * 2 + c + n * a
    )