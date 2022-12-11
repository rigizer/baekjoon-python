# https://www.acmicpc.net/problem/11060

from collections import deque

def bfs(n, result):
    queue = deque()
    visited = [False] * n

    queue.append((0, 0))
    visited[0] = True

    while queue:
        idx, cnt = queue.popleft()
        
        if idx == n - 1:
            return cnt

        for i in range(1, board[idx] + 1):
            if idx + i < n and visited[idx + i] == False:
                queue.append((idx + i, cnt + 1))
                visited[idx + i] = True

    return -1

n = int(input())
board = list(map(int, input().split()))

result = bfs(n, board)
print(result)
