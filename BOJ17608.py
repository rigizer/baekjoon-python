# https://www.acmicpc.net/problem/17608

n = int(input())
data = [int(input()) for _ in range(n)]

cnt = 1
max_height = data[n - 1]

for i in range(n - 2, -1, -1):
    if data[i] <= max_height: continue
    max_height = data[i]
    cnt += 1

print(cnt)
