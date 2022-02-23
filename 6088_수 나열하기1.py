a, d, n = list(map(int, input().split()))

while n > 1:
    a += d
    n -= 1
print(a)