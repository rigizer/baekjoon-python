# https://www.acmicpc.net/problem/11651

data = [list(map(int, input().split())) for _ in range(int(input()))]
data.sort(key=lambda x:(x[1], x[0]))
print('\n'.join((' '.join(str(j) for j in i)) for i in data))
