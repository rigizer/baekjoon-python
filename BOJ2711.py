# https://www.acmicpc.net/problem/2711

n = int(input())

for _ in range(n):
    t1, t2 = input().split()
    e = int(t1)
    s = str(t2)

    for i in range(0, len(s)):
        if i + 1 != e:
            print(s[i], end='')
    print()
