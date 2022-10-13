# https://www.acmicpc.net/problem/9723

t = int(input())

for tc in range(1, t + 1):
    data = list(map(int, input().split()))
    data.sort(reverse=True)

    if data[1] ** 2 + data[2] ** 2 == data[0] ** 2:
        print("Case #{}: {}".format(tc, "YES"))
    else:
        print("Case #{}: {}".format(tc, "NO"))
