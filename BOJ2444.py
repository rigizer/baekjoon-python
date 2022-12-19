# https://www.acmicpc.net/problem/2444

n = int(input())

for i in range(n * 2 - 1):
    
    if i < n - 1:
        for j in range(n - 1 - i):
            print(' ', end='')
        for j in range((i + 1) * 2 - 1):
            print('*', end='')
    else:
        for j in range(i - n + 1):
            print(' ', end='')
        for j in range((n * 4 - (i * 2) - 3)):
            print('*', end='')
    
    print()
