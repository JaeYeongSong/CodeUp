a, m, d, n = list(map(int, input().split()))

while n > 1:
    a *= m
    a += d
    n -= 1
print(a)