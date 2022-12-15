# https://www.acmicpc.net/problem/1302

data = dict()

n = int(input())

for _ in range(n):
    d = input()
    if data.get(d) == None:
        data[d] = 1
    else:
        data[d] += 1

m = 0
m_name = []

for key, value in data.items():
    if m < value:
        m = value
        m_name.clear()
        m_name.append(key)

    elif m == value:
        m_name.append(key)

m_name.sort()
print(m_name[0])
