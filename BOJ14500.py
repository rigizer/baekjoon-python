# https://www.acmicpc.net/problem/14500

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answer = 0

# 2차원 배열에서 최대값을 max_val에 지정
max_val = max(map(max, board))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x, length, total):
    global answer

    # 테트로미노를 만든 경우
    if length == 4:
        answer = max(answer, total)
        return

    # answer보다 total이 너무 작은경우 조건 확인 X
    if answer > total + max_val * (4 - length):
        return

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == False:
            if length == 2:
                # ㅗ, ㅓ, ㅏ, ㅜ 모양 만들기 위한 로직
                visited[ny][nx] = True
                dfs(y, x, length + 1, total + board[ny][nx])
                visited[ny][nx] = False
            
            visited[ny][nx] = True
            dfs(ny, nx, length + 1, total + board[ny][nx])
            visited[ny][nx] = False

for i in range(n):
    for j in range(m):
        # DFS로직으로 순차탐색
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

print(answer)
