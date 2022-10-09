3 https://www.acmicpc.net/problem/2738

n, m = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        arr1[i][j] = arr1[i][j] + arr2[i][j]

        print(arr1[i][j], end=' ')
    print()
