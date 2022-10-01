# https://www.acmicpc.net/problem/1085

import sys
x, y, w, h = map(int, input().split())

m = sys.maxsize
m = min(m, w - x)
m = min(m, x)
m = min(m, h - y)
m = min(m, y)
print(m)
