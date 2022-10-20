# https://www.acmicpc.net/problem/1037

N = int(input())
A = list(map(int, input().split()))

max_num = max(A)
min_num = min(A)

print(max_num * min_num)
