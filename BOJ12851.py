# https://www.acmicpc.net/problem/12851

from collections import deque

class Node:
    def __init__(self, x, t):
        self.x = x  # x 좌표
        self.t = t  # 지난 시간

    def __str__(self):
        return 'x={}, t={}'.format(self.x, self.t)

st = 1e9  # 동생을 찾는 가장 빠른 시간
sc = 0    # 동생을 찾는 방법의 경우의 수

def bfs(n, k):
    global st, sc

    queue = deque()
    visited = [1e9 for _ in range(100_001)]

    queue.append(Node(n, 0))
    visited[n] = True

    while queue:
        node = queue.popleft()

        if node.x == k:
            if st > node.t:
                st = node.t
                sc = 1
            elif st == node.t:
                sc += 1
            
            continue

        for dir in [-1, 1, node.x]:
            x = node.x + dir

            if 0 <= x <= 100_000 and visited[x] >= node.t:
                queue.append(Node(x, node.t + 1))
                visited[x] = node.t

def main():
    n, k = map(int, input().split())
    bfs(n, k)
    print(st)
    print(sc)

if __name__ == '__main__':
    main()
