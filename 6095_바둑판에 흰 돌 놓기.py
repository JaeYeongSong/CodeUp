import sys

d = [[0 for j in range(19)] for i in range(19)]

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().strip().split())))

for i in a:
    d[i[0] - 1][i[1] - 1] = 1

for i in d:
    for j in i:
        print(j, end=' ')
    print()