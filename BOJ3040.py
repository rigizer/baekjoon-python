# https://www.acmicpc.net/problem/3040

import itertools
data = [int(input()) for i in range(9)]
data = list(itertools.combinations(data, 7))
for i in data:
    if sum(i) == 100:
        print('\n'.join(map(str, i)))
        break
