# https://www.acmicpc.net/problem/3190

from collections import deque

snake = deque()

# 방향벡터 (우, 하, 좌, 상)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 뱀의 방향 (기본: 오른쪽)
dir = 0

# 사과의 위치
n = int(input())
board = [[False] * (n + 1) for _ in range(n + 1)]

k = int(input())
for _ in range(k):
    i, j = map(int, input().split())
    board[i][j] = True

data = deque()

l = int(input())
for _ in range(l):
    x, c = map(str, input().split())
    x = int(x)
    data.append((x, c))

# 새로 생길 머리 위치와 기존에 있던 몸통과 충돌하는지 여부 확인
def body_collision(y, x):
    for s in snake:
        if s[0] == y and s[1] == x:
            return True

    return False

# 초기 뱀 머리 위치
snake.append((1, 1))

t = 0
while True:
    t += 1

    # 뱀의 머리는 항상 queue의 왼쪽에 있다
    snake_head = snake[0]

    y = snake_head[0] + dy[dir]
    x = snake_head[1] + dx[dir]

    # board를 벗어났는지 확인
    if y < 1 or y > n or x < 1 or x > n:
        break

    # 새로 이동할 위치가 몸통과 충돌하는지 확인
    if body_collision(y, x) == True:
        break

    # 새로 이동하는 위치에 사과가 있는지 여부 확인
    if board[y][x] == True:
        snake.appendleft((y, x))
        board[y][x] = False
    else:
        snake.pop()
        snake.appendleft((y, x))

    # 방향을 바꾸어야 하는지 여부 확인
    if len(data) > 0:
        nt, nd = data[0]

        if nt == t:
            if nd == 'L':
                dir = ((dir - 1) + 4) % 4
            elif nd == 'D':
                dir = ((dir + 1) + 4) % 4

            data.popleft()

# 최종 시간 출력
print(t)
