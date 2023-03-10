import sys
input = sys.stdin.readline

N = int(input())
PAPER = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]


def traversal(x, y, N):
    color = PAPER[x][y]
    for row in range(x, x + N):
        for col in range(y, y + N):
            if color != PAPER[row][col]:
                # 각각 1, 2, 3, 4분면 이동
                traversal(x, y, N // 2)
                traversal(x, y + N // 2, N // 2)
                traversal(x + N // 2, y, N // 2)
                traversal(x + N // 2, y + N // 2, N // 2)
                return 0
    # 모든 범위 내애 종이 색깔이 같다면
    if color == 0:
        answer[0] += 1
    else:
        answer[1] += 1


traversal(0, 0, N)
for a in answer:
    print(a)
