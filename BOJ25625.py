# https://www.acmicpc.net/problem/25625

x, y = map(int, input().split())
if x > y: print(x + y)
else: print(y - x)
