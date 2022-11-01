# https://www.acmicpc.net/problem/7567

dish = list(str(input()))
answer = 0

for i in range(len(dish)):
    if i == 0:
        answer += 10
    elif dish[i] == dish[i-1]:
        answer += 5
    else:
        answer += 10
        
print(answer)
