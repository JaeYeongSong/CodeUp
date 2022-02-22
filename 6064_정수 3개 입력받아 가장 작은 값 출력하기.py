a, b, c = list(map(int, input().split()))

print((a if a < b else b) if a < c else (b if b < c else c))