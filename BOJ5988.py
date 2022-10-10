# https://www.acmicpc.net/problem/5988

n = int(input())
for _ in range(n):
    k = int(input())
    print('even' if k % 2 == 0 else 'odd')
