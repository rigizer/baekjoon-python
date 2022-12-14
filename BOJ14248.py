# https://www.acmicpc.net/problem/14248

from collections import deque

def bfs(n, board, s):
    result = 1

    queue = deque()
    visited = [False] * n

    queue.append(s - 1)
    visited[s - 1] = True

    while queue:
        node = queue.popleft()

        for x in [node - board[node], node + board[node]]:
            if 0 <= x < n and visited[x] == False:
                queue.append(x)
                visited[x] = True
                result += 1

    return result

n = int(input())
board = list(map(int, input().split()))
s = int(input())

result = bfs(n, board, s)
print(result)
