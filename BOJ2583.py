# https://www.acmicpc.net/problem/2583

import sys
from collections import deque

class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        
    def __str__(self):
        return "y={}, x={}".format(self.y, self.x)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

m, n, k = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

maps = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

area = 0
area_list = []

# 모눈종이에 사각형 그리기
for d in data:
    for i in range(d[1], d[3]):
        for j in range(d[0], d[2]):
            maps[i][j] = 1
            
def bfs(maps, visited, m, n, i, j):
    cnt = 0
    
    queue = deque()
    queue.appendleft(Node(i, j))
    visited[i][j] = True
    cnt += 1
    
    while queue:
        node = queue.pop()
        
        for d in range(4):
            y = node.y + dy[d]
            x = node.x + dx[d]
            
            if 0 <= y < m and 0 <= x < n and maps[y][x] == 0 and visited[y][x] == False:
                queue.appendleft(Node(y, x))
                visited[y][x] = True
                cnt += 1
                
    return cnt

for i in range(m):
    for j in range(n):
        if maps[i][j] == 0 and visited[i][j] == False:
            area += 1
            cnt = bfs(maps, visited, m, n, i, j)
            area_list.append(cnt)

# 넓이 오름차순 정렬
area_list.sort()
            
print(area)
print(' '.join([str(i) for i in area_list]))
