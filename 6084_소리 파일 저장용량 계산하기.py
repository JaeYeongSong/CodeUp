h, b, c, s = list(map(int, input().split()))

print(format(h * b * c * s/8/1024/1024, '.1f'), 'MB', sep=' ')