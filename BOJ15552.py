# https://www.acmicpc.net/problem/15552

import sys
t = int(sys.stdin.readline().rstrip('\n'))
for _ in range(t): print(sum(map(int, sys.stdin.readline().rstrip('\n').split())))
