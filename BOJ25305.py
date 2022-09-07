# https://www.acmicpc.net/problem/25305

n, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data[k - 1])
