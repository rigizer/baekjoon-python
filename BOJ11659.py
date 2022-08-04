# https://www.acmicpc.net/problem/11659

n, m = map(int, input().split())

num_list = list(map(int, input().split()))
range_list = []

for i in range(m):
    range_list.append(list(map(int, input().split())))

for i in range(1, n):
    num_list[i] += num_list[i - 1]

for i in range(m):
    start = range_list[i][0] - 2
    end = range_list[i][1] - 1

    if start < 0:
        result = num_list[end]
    else:
        result = num_list[end] - num_list[start]

    print(result)
