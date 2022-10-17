# https://www.acmicpc.net/problem/5586

data = input()

joi = 0
ioi = 0

for i in range(len(data) - 2):
    temp = data[i:i+3]
    if temp == 'JOI':
        joi += 1
    elif temp == 'IOI':
        ioi += 1

print(joi)
print(ioi)
