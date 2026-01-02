def gcd(n, m):
    t = n % m
    if (t == 0):
        return m
    return gcd(m, t)

t = int(input())

for _ in range (t):
    a, b = map(int, input().split())
    g = gcd(a, b)
    print(a*b//g)