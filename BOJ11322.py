# https://www.acmicpc.net/problem/11322

from collections import deque

def bfs(n):
    queue = deque()
    queue.append('1')

    while queue:
        num_str = queue.popleft()
        num = int(num_str)

        if num % n == 0:
            print(num)
            return

        queue.append(num_str + '0')
        queue.append(num_str + '1')

for _ in range(int(input())):
    n = int(input())
    bfs(n)
