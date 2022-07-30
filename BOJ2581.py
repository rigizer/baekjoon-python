# https://www.acmicpc.net/problem/2581

import math

m = int(input())
n = int(input())

pnum_list = []

# 1부터 1까지일때는 2가 추가되지 않도록 주의
if m <= 2 and n >= 2:
    pnum_list.append(2)

if m % 2 == 0:
    m += 1

for i in range(m, n + 1, 2):
    if i == 1:
        continue

    is_pnum = True
    for j in range(3, int(math.sqrt(i)) + 1, 2):
        if i % j == 0:
            is_pnum = False
            break

    if is_pnum == True:
        pnum_list.append(i)

if len(pnum_list) == 0:
    print(-1)

else:
    print(sum(pnum_list))
    print(min(pnum_list))
