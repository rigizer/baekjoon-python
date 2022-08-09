# https://www.acmicpc.net/problem/2576

result = 0
data = [int(input()) for _ in range(7)]
min_num = max(data)

for i in data:
    if i % 2 == 1:
        result += i

        if min_num > i:
            min_num = i

if result == 0:
    print(-1)
else:
    print(result)
    print(min_num)
