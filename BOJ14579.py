# https://www.acmicpc.net/problem/14579

a, b = map(int, input().split())

t = 1
for i in range(a, b + 1): # j for문을 a~b 차이만큼 반복하도록 자정
    s = 0

    for j in range(1, i + 1): # 1부터 i번째까지 누적
        s += j

    t *= s

print(t % 14579)
