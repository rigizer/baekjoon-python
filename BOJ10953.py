# https://www.acmicpc.net/problem/10953

t = int(input())
data = [list(map(int, input().split(','))) for _ in range(t)]
print('\n'.join([str(sum(i)) for i in data]))
