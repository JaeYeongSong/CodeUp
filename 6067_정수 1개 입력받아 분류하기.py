n = int(input())

if n < 0:
    if not (n % 2):
        print('A')
    else:
        print('B')
else:
    if not (n % 2):
        print('C')
    else:
        print('D')