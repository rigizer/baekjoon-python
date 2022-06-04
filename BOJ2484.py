# https://www.acmicpc.net/problem/2484

def calc(a, b, c, d):
    # 같은 눈이 4개 나오는 경우
    if a == b and b == c and c == d:
        return 50000 + a * 5000
    
    # 같은 눈이 3개 나오는 경우
    if a == b and b == c:
        return 10000 + a * 1000
    if a == b and b == d:
        return 10000 + a * 1000
    if a == c and c == d:
        return 10000 + a * 1000
    if b == c and c == d:
        return 10000 + b * 1000
    
    # 같은 눈이 2개씩 두 쌍이 나오는 경우
    if a == b and c == d:
        return 2000 + (a * 500) + (c * 500)
    if b == c and a == d:
        return 2000 + (a * 500) + (c * 500)
    if a == c and b == d:
        return 2000 + (a * 500) + (b * 500)

    # 같은 눈이 2개만 나오는 경우
    if a == b:
        return 1000 + a * 100
    if b == c:
        return 1000 + b * 100
    if c == d:
        return 1000 + c * 100
    if a == d:
        return 1000 + d * 100
    if a == c:
        return 1000 + a * 100
    if b == d:
        return 1000 + b * 100

    # 모두 다른 눈이 나오는 경우
    else:
        max_num = max([a, b, c, d])
        return max_num * 100

n = int(input())
temp = []
for _ in range(0, n):
    a, b, c, d= input().split()
    temp.append(calc(int(a), int(b), int(c), int(d)))

print(max(temp))
