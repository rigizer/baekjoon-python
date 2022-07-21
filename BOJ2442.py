# https://www.acmicpc.net/problem/2442

n = int(input())

for i in range(0, n):
    for j in range(i, n - 1):
        print(" ", end="")
    for j in range(0, i * 2 + 1):
        print("*", end="")
    print()
