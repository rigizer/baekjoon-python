# https://www.acmicpc.net/submit/6780

r = 2

a = int(input())
b = int(input())

while a - b >= 0:
    t = b
    b = a - b
    a = t
    r += 1

print(r)
