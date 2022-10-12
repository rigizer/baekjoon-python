# https://www.acmicpc.net/problem/2755

import decimal

n = int(input())

tp = 0
tc = 0
for _ in range(n):
    s, p, c = map(str, input().split())

    if c == 'A+': point = 4.3
    elif c == 'A0': point = 4.0
    elif c == 'A-': point = 3.7
    elif c == 'B+': point = 3.3
    elif c == 'B0': point = 3.0
    elif c == 'B-': point = 2.7
    elif c == 'C+': point = 2.3
    elif c == 'C0': point = 2.0
    elif c == 'C-': point = 1.7
    elif c == 'D+': point = 1.3
    elif c == 'D0': point = 1.0
    elif c == 'D-': point = 0.7
    elif c == 'F': point = 0.0

    tp += int(p)
    tc += int(p) * point

context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP

print(round(decimal.Decimal(str(tc / tp)), 2))
