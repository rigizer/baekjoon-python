# https://www.acmicpc.net/problem/2309

from itertools import permutations
from re import I

data = [int(input()) for _ in range(9)]
perm_data = list(permutations(data, 7))

for items in perm_data:
    if sum(items) == 100:
        sorted_items = list(items)
        sorted_items.sort()
        for i in sorted_items:
            print(i)
        break
