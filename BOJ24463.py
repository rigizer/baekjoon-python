# https://www.acmicpc.net/problem/24463

import sys
sys.setrecursionlimit(10_000_000)

class Node:
    def __init__(self, y, x, t, r):
        self.y = y
        self.x = x
        self.t = t
        self.r = r

    def __str__(self):
        return 'y={}, x={}, t={}, r={}'.format(self.y, self.x, self.t, self.r)

def init(n, m, board):
    temp = list()

    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                board[i][j] = '@'
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    temp.append([i, j])

    return temp

def dfs(y, x):
    if y == end[0] and x == end[1]:
        return True
    
    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        i, j = y + dy, x + dx

        if 0 <= i < n and 0 <= j < m and visited[i][j] == False and board[i][j] == '@':
            board[i][j] = '.'
            visited[i][j] = True
            if dfs(i, j) == True: return True # 탐색 가능한 경우의 수가 있으면 더 깊이 들어가고, 모든 경우의 수가 성공하면 True 반환
            board[i][j] = '@'
            visited[i][j] = False

    # 더 이상 탐색 가능한 경우의 수가 없음
    return False

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
start, end = init(n, m, board)

board[start[0]][start[1]] = '.'
visited[start[0]][start[1]] = True

result = dfs(start[0], start[1])
print('\n'.join([''.join([j for j in i]) for i in board]))
