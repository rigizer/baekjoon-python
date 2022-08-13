# https://www.acmicpc.net/problem/7510

tc = int(input())
res = ''

for i in range(tc):
    a, b, c = map(int, input().split())

    result = False
    if a ** 2 == b ** 2 + c ** 2:
        result = True
    elif b ** 2 == a ** 2 + c ** 2:
        result = True
    elif c ** 2 == a ** 2 + b ** 2:
        result = True

    res += 'Scenario #{}:\n{}\n\n'.format(i + 1, 'yes' if result else 'no')

print(res)
