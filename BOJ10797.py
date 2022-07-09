# https://www.acmicpc.net/submit/10797

n = int(input())
s = 0

arr = list(map(int,input().split()))
for i in arr:
    if i == n:
        s += 1

print(s)
