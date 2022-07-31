# https://www.acmicpc.net/problem/2522

n = int(input())

MAX_WIDTH = n * 2 - 1
for i in range(MAX_WIDTH):
    ii = 0
    if i < n:
        ii = n - i - 1
    else:
        ii = i - n + 1

    for j in range(n):
        if j < ii:
            print(' ', end='')
        else:
            print('*', end='')
    print()
