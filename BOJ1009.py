T = int(input())

# 어떤 수를 제곱을 한 것의 일의 자리 수에 대한 반복패턴이 존재한다
arr = []

'''
arr = [
    [0]
    ,[1]
    ,[2, 4, 8, 6]
    ,[3, 9, 7, 1]
    ,[4, 6]
    ,[5]
    ,[6]
    ,[7, 9, 3, 1]
    ,[8, 4, 2, 6]
    ,[9, 1]
]
'''

for i in range(10):
    arr_sub = []
    j = 1
    while True:
        temp = i ** j % 10
        if temp in arr_sub:
            break
        arr_sub.append(temp)
        j += 1

    arr.append(arr_sub)

for _ in range(T):
    a, b = map(int, input().split())

    # 어떤 수의 0제곱은 항상 1이다
    if b == 0:
        print(1)
        continue

    t = arr[a % 10][b % len(arr[a % 10]) - 1]
    print(10 if t == 0 else t)
