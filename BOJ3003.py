# https://www.acmicpc.net/problem/3003

orig = [1, 1, 2, 2, 2, 8]
inpt = list(map(int, input().split()))

for i in range(6):
    inpt[i] = orig[i] - inpt[i]

print(*inpt)
