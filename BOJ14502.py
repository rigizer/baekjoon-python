# https://www.acmicpc.net/problem/14502

# 세로 n, 가로 m

# [지도]
# 0 - 빈칸
# 1 - 벽
# 2 - 바이러스

import sys
from itertools import permutations
from collections import deque

class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        
    def __str__(self):
        return "y={}, x={}".format(self.y, self.x)

# 벽을 세울만한 위치를 탐색, 좌표를 리스트에 저장
def get_walls(data, n, m):
    walls = []
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                walls.append([i, j])

    return walls

# 벽을 세울 위치에 대한 순열을 생성
def get_walls_order(walls):
    return [i for i in permutations(walls, 3)]

# BFS 탐색을 통해 벽을 세운 다음 바이러스를 퍼트린다
def bfs(data, w, n, m):
    queue = deque()
    
    # 2차원 리스트 하드카피
    _data = [item[:] for item in data]
    
    # 바이러스 위치를 큐에 집어넣음
    for i in range(n):
        for j in range(m):
            if _data[i][j] == 2:
                queue.appendleft(Node(i, j))
    
    # data에 새로 3개의 벽을 세운 위치를 지정해 줌
    for wall in w:
        _data[wall[0]][wall[1]] = 1

    while queue:
        node = queue.pop()
        
        for d in range(4):
            y = node.y + dy[d]
            x = node.x + dx[d]
            
            if 0 <= y < n and 0 <= x < m and _data[y][x] == 0:
                queue.appendleft(Node(y, x))
                _data[y][x] = 2
    
    return _data

def check_zero(_data, n, m):
    s = 0
    for i in range(n):
        for j in range(m):
            if _data[i][j] == 0:
                s += 1
    
    return s

result = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 가로와 세로 크기를 지정
n, m = map(int, sys.stdin.readline().split())

# 지도 데이터를 입력받음
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

walls = get_walls(data, n, m)
walls_order = get_walls_order(walls)

for w in walls_order:
    _data = bfs(data, w, n, m)
    s = check_zero(_data, n, m)
    result = max(result, s)

print(result)
