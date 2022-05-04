# https://www.acmicpc.net/problem/1436

n = int(input())
idx = 0
result = 0

for i in range(666, 999999999):
    if '666' in str(i):
        idx += 1
        if idx == n:
            result = i
            break

print(result)
