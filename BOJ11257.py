# https://www.acmicpc.net/problem/11257

n = int(input())

for _ in range(n):
    data = list(map(int, input().split()))
    total = data[1] + data[2] + data[3]

    is_pass = True
    if data[1] < 35 / 100 * 30:
        is_pass = False
    if data[2] < 25 / 100 * 30:
        is_pass = False
    if data[3] < 40 / 100 * 30:
        is_pass = False
    if total < 55:
        is_pass = False

    print('{} {} {}'.format(data[0], total, 'PASS' if is_pass else 'FAIL'))
