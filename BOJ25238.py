# https://www.acmicpc.net/problem/25238

m, p = map(int, input().split())

result = (float(m) / 100) * (100 - p)
if result < 100:
    print(1)
else:
    print(0)
