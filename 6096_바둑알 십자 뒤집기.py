import sys

d = []
for _ in range(19):
    d.append(list(map(int, sys.stdin.readline().strip().split())))
n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().strip().split())))

for i in a:
    for j in range(19):
        if d[i[0] - 1][j] == 1:
            d[i[0] - 1][j] = 0
        else:
            d[i[0] - 1][j] = 1
        if d[j][i[1] - 1] == 1:
            d[j][i[1] - 1] = 0
        else:
            d[j][i[1] - 1] = 1

for i in d:
    for j in i:
        print(j, end=' ')
    print()