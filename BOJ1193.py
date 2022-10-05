# https://www.acmicpc.net/problem/1193

import sys
input = sys.stdin.readline

n = int(input())
line = 1

while n > line :
    n -= line
    line += 1

if line % 2 == 0:
    num1 = n
    num2 = line - n + 1
elif line % 2 == 1:
    num1 = line - n + 1
    num2 = n

print(num1,'/',num2,sep = "")
