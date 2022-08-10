# https://www.acmicpc.net/problem/25377

import math

n = int(input())

result = math.inf
is_ok = False
for i in range(n):
    a, b = map(int, input().split())

    if a <= b:
        if result > b: result = b
        is_ok = True

print(result) if is_ok else print(-1)
