# https://www.acmicpc.net/problem/1436

n = int(input())
idx = 0
result = 0

for i in range(0, 10001):
    if '666' in str(i):
        idx += 1
        if idx == n:
            result = i
            break

print(result)
