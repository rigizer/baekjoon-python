# https://www.acmicpc.net/problem/25418

from collections import deque
a, k = map(int, input().split())

queue = deque()
visited = [1e9] * 1_000_001

queue.append((a, 0))
visited[a] = 0

result = 1e9

while queue:
    num, cnt = queue.popleft()

    if num == k:
        result = min(result, cnt)
    
    if num * 2 <= k and result > cnt + 1 and visited[num * 2] > cnt + 1:
        queue.append((num * 2, cnt + 1))
        visited[num * 2] = cnt + 1
    
    if num + 1 <= k and result > cnt + 1 and visited[num + 1] > cnt + 1:
        queue.append((num + 1, cnt + 1))
        visited[num + 1] = cnt + 1

print(result)
