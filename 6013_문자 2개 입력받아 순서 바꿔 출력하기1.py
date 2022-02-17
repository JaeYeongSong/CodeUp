import sys

string = []
for _ in range(2):
    string.append(sys.stdin.readline().strip())

for i in range(1, -1, -1):
    print(string[i])