# https://www.acmicpc.net/problem/11653

n = int(input())

r = []
while True:
    for i in range(2, n + 1):
        if n % i == 0:
            r.append(i)
            n = n // i
            break

    if n == 1:
        break

print(''.join(str(i)+'\n' for i in r))
