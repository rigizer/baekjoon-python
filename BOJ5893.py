# https://www.acmicpc.net/problem/5893

n = int(input())
n = int(str(n), 2)
n *= 17
print(bin(n)[2:])
