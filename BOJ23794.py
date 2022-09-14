# https://www.acmicpc.net/problem/23794

n = int(input())

for i in range(n + 2):
    for j in range(n + 2):
        if 0 < i < n + 1 and 0 < j < n + 1:
            print(" ", end='')
        else:
            print("@", end='')
    print()
