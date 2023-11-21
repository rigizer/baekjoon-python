n, t = map(int, input().split())
li = list(map(int, input().split()))
for i in range(n):
    if sum(li[:i+1]) > t:
        print(i)
        break
    elif i == n - 1:
        print(n)
