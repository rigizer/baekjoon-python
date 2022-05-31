// https://www.acmicpc.net/problem/1546

n = int(input())
m = list(map(int, input().split()))
max_num = max(m)

for i in range(n):
    m[i] = m[i] / max_num * 100
print("%.2f" %(sum(m)/ n))
