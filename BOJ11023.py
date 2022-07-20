# https://www.acmicpc.net/problem/11023

l = list(map(int, input().split()))

s = 0
for i in l:
    s += i

print(s)
