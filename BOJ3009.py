# https://www.acmicpc.net/problem/3009

x_points = []
y_points = []

for _ in range(3):
    x, y = map(int, input().split())
    x_points.append(x)
    y_points.append(y)

for i in range(3):
    if x_points.count(x_points[i]) == 1:
        x4 = x_points[i]
    if y_points.count(y_points[i]) == 1:
        y4 = y_points[i]

print(x4, y4)
