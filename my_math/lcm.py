# https://ithelp.ithome.com.tw/articles/10250910
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


print(lcm(45, 90))


