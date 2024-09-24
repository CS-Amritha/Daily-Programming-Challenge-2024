def gcd(x, y):
    if x == 0:
        return y
    return gcd(y % x, x)

def lcm(x, y):
    return (x // gcd(x, y)) * y
n = 15
m = 20
print('LCM of', n, 'and', m, 'is', lcm(num1, num2))
