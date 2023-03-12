# https://www.acmicpc.net/problem/12605

from collections import deque

n = int(input())
t = deque()

for i in range(n):
    t = str(input()).split()
    t.reverse()
    print(f'Case #{i + 1}:', ' '.join(t))
    t.clear()
