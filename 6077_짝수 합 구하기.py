n = int(input())
sum = 0

for i in range(1, n + 1):
    if not (i % 2):
        sum += i

print(sum)