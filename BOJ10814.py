# https://www.acmicpc.net/problem/10814

n = int(input())
data = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    data.append([i, int(age), name])

data.sort(key=lambda x: (x[1], x[0]))

for i, age, name in data:
    print('{} {}'.format(str(age), name))
