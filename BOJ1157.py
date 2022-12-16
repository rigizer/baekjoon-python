# https://www.acmicpc.net/problem/1157

data = dict()
for i in input():
    if data.get(i.upper()) == None:
        data[i.upper()] = 1
    else:
        data[i.upper()] += 1

max_key = ''
max_val = 0
max_dup = False

for key, val in data.items():
    if max_val < val:
        max_key = key
        max_val = val
        max_dup = False
    elif max_val == val:
        max_dup = True

print('?' if max_dup else max_key)
