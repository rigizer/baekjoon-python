# https://www.acmicpc.net/problem/13458

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0 # 총 감독관 수

for i in a:
    m = 1 # 총감독
    s = 0 # 부감독

    temp = i - b

    if temp > 0:
        if temp % c == 0: s += temp // c
        else: s += (temp // c) + 1
    
    result += m
    result += s

print(result)
