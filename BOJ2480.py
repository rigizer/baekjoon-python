# https://www.acmicpc.net/problem/2480

def calc(a, b, c):
    if a == b and b == c:
        return 10000 + a * 1000
    if a == b:
        return 1000 + a * 100
    if b == c:
        return 1000 + b * 100
    if a == c:
        return 1000 + c * 100
    if a > b and a > c:
        return a * 100
    if b > a and b > c:
        return b * 100
    if c > a and c > b:
        return c * 100

a, b, c = map(int, input().split())
print(calc(a, b, c))
