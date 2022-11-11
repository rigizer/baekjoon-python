# https://www.acmicpc.net/problem/11650

n = int(input())
data = [list(map(int, input().split())) for _  in range(n)]
data.sort(key=lambda x: (x[0], x[1]))
print('\n'.join([' '.join([str(j) for j in i]) for i in data]))
