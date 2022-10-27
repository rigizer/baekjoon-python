# https://www.acmicpc.net/problem/5218

for _ in range(int(input())):
    a, b = input().split()
    li = []
    for i in range(len(a)):
        if ord(a[i]) > ord(b[i]):
            li.append(26 - (ord(a[i])-ord(b[i])))
        else:
            li.append(ord(b[i]) - ord(a[i]))
    print("Distances:", *li)
