# https://www.acmicpc.net/problem/13915

jinho = input()
n = int(input())
s = 0
for _ in range(n):
    if jinho == input(): 
        s += 1
print(s)
