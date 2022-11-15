# https://www.acmicpc.net/problem/1173

N, m, M, T, R = map(int, input().split())
pulse = m
time = 0
exercise = 0

while exercise < N:
    if m + T > M:
        time = -1
        break
        
    time += 1
    
    if pulse + T <= M:
        pulse += T
        exercise += 1
    else:
        if pulse - R < m: pulse = m
        else: pulse -= R
            
print(time)
