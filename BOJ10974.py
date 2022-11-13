# https://www.acmicpc.net/problem/10974

import itertools

n = int(input())
data = list(itertools.permutations([i for i in range(1, n + 1)], n))

print('\n'.join([' '.join(str(j) for j in i) for i in data]))
