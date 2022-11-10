# https://www.acmicpc.net/problem/2798

import itertools

n, m = map(int, input().split())
card = list(map(int, input().split()))

data = list(itertools.combinations(card, 3))

result = 0
for d in data:
    temp = sum(d)
    if result < temp <= m:
        result = temp
    elif temp == m:
        result = m
        break

print(result)
