# https://www.acmicpc.net/problem/10991

n = int(input())

count = n - 1
for i in range(1, n + 1):
    print(' ' * count, end='')
    print('* ' * i)
    count -= 1
