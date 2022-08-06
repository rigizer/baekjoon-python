# https://www.acmicpc.net/problem/1920

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

for i in b:
    result = True
    start = 0
    end = len(a) - 1
    while True:
        if a[start] > i or a[end] < i:
            result = False
            break

        mid = (start + end) // 2

        # 어차피 mid값 계속가면 start 혹은 end번째 인덱스에 도달
        if i == a[mid]:
            result = True
            break

        # mid와 일치하지 않기 때문에 -1 혹은 +1을 해줌
        if i < a[mid]:
            end = mid - 1
        else:
            start = mid + 1

    print(1 if result else 0)
