# https://www.acmicpc.net/problem/9733

import sys
lst = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']
bee = dict()
for i in lst:
    bee[i] = 0
 
cnt = 0
lines = sys.stdin.readlines()
for line in lines:
    txt = list(line.split())
    for i in txt:
        if i in lst:
            bee[i] = bee.get(i, 0) + 1
        cnt += 1
 
for i in bee:
    print(i, bee.get(i), '{:.2f}'.format(bee.get(i)/cnt))
 
print('Total', cnt, '1.00')
