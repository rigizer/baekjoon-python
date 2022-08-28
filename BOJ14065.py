# https://www.acmicpc.net/problem/14065

data = float(input())
gpm = 3.785411784
mpk = 1.609344
print('{:.6f}'.format(100 / data / mpk * gpm))
