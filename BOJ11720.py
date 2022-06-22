# https://www.acmicpc.net/problem/11720

N = int(input())
n = str(input())
sum = 0
for i in range(N):
    sum = sum + int(n[i])
print(sum)
