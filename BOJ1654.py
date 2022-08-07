# https://www.acmicpc.net/problem/1654

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    lan_count = 0

    for i in range(k):
        lan_count += lan[i] // mid

    if lan_count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
