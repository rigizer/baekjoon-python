# https://www.acmicpc.net/problem/2566

data = [list(map(int, input().split())) for _ in range(9)]
max = 0
h, w = 0, 0

for i in range(9):
    for j in range(9):
        if max < data[i][j]:
            max = data[i][j]
            h = i
            w = j

print(max)
print('{} {}'.format(h + 1, w + 1))
