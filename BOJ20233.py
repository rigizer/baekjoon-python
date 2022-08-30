# https://www.acmicpc.net/problem/20233

a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

if t < 30: i = a
else: i = a + (t - 30) * x * 21

if t < 45: j = b
else: j = b + (t - 45) * y * 21

print('{} {}'.format(i, j))
