d = []
for _ in range(10):
    d.append(list(map(int, input().split())))

success = False
i = 1
j = 1
while not success:
    if i == 8 and j == 8:
        d[i][j] = 9
        break
    if d[i][j] == 2:
        d[i][j] = 9
        success = True
    else:
        d[i][j] = 9
        if d[i][j + 1] == 1:
            i += 1
        else:
            j += 1

for i in d:
    for j in i:
        print(j, end=' ')
    print()