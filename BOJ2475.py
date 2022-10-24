# https://www.acmicpc.net/problem/2475

data = list(map(int, input().split()))
print(sum([i ** 2 for i in data]) % 10)
