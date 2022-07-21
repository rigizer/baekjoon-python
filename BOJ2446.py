# https://www.acmicpc.net/problem/2446

n = int(input())

for i in range(n, 1, -1):
    for j in range(0, n - i):
        print(" ", end="")
    for j in range(i * 2 - 1, 0, -1):
        print("*", end="")
    print()

for i in range(0, n):
    for j in range(i, n - 1):
        print(" ", end="")
    for j in range(0, i * 2 + 1):
        print("*", end="")
    print()
