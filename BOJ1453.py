# https://www.acmicpc.net/problem/1453

com = [False] * 101
n = int(input())
customer = list(map(int, input().split()))

reject = 0
for c in customer:
    if com[c] == True:
        reject += 1
    else:
        com[c] = True

print(reject)
