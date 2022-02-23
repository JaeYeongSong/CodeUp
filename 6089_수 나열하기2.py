a, r, n = list(map(int, input().split()))

while n > 1:
    a *= r
    n -= 1
print(a)