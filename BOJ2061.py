# https://www.acmicpc.net/problem/2061

k, l = map(int, input().split())
for i in range(2, l):
    if k % i == 0:
        print('BAD {}'.format(i))
        break
else:
    print('GOOD')
