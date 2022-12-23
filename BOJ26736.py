# https://www.acmicpc.net/problem/26736

a, b = 0, 0
for i in input():
    if i == 'A': a += 1
    elif i == 'B': b += 1

print('{} : {}'.format(a, b))
