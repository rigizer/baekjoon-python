# https://www.acmicpc.net/problem/5532

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = 0
for day in range(1, l + 1):
    a -= c
    b -= d

    if a <= 0 and b <= 0:
        result = l - day
        break

print(result)
