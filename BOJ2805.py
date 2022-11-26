# https://www.acmicpc.net/problem/2805

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    temp = sum([(i - mid if i > mid else 0) for i in tree])
    
    if temp >= m: start = mid + 1
    else: end = mid - 1
    
print(end)
