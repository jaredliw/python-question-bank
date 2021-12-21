# CPU: 0.06 s
def gcd(x, y):
    if x == 0:
        if y == 0:
            raise ArithmeticError("GCD of 0 and 0 is undefined")
        return abs(y)
    else:
        return gcd(y % x, x)

def lcm(x, y):
    if x == 0 or y == 0:
        raise ArithmeticError("LCM of {} and {} is undefined".format(x, y))
    return abs(x * y) // gcd(x, y)

num1, num2, max_sec = map(int, input().split())
print("yes" if lcm(num1, num2) <= max_sec else "no")
