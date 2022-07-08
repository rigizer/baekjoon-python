# https://www.acmicpc.net/problem/5565

t = int(input())
s = 0

for i in range(9):
    n = int(input())
    s += n

print(t - s)
