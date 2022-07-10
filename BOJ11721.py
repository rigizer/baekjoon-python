# https://www.acmicpc.net/problem/11721

s = input()
n = 0

for _ in s:
    print(_, end='')

    n += 1
    if n % 10 == 0:
        print()
