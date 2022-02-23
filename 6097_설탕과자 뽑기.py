h, w = list(map(int, input().split()))
n = int(input())
lists = [[0 for j in range(w)] for i in range(h)]

for i in range(n):
    l, d, x, y = list(map(int, input().split()))
    if d == 0:
        for j in range(l):
            lists[x - 1][y - 1 + j] = 1
    else:
        for j in range(l):
            lists[x - 1 + j][y - 1] = 1

for i in lists:
    for j in i:
        print(j, end=' ')
    print()