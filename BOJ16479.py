# https://www.acmicpc.net/problem/16479

z = int(input())
y, x = map(int, input().split())

result = z ** 2 - (((y - x) / 2) ** 2)
print(result)
