r, g, b = list(map(int, input().split()))

i = 0
for x in range(r):
    for y in range(g):
        for z in range(b):
            print(x, y, z, sep=' ')
            i += 1
print(i)