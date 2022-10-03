# https://www.acmicpc.net/problem/2752

data = list(map(int, input().split()))
data.sort()
print(' '.join([str(i) for i in data]))
