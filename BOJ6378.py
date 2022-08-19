# https://www.acmicpc.net/problem/6378

while True:
    data = int(input())
    if data == 0:
        break
    
    isBreak = False
    sum = 0
    while True:
        while True:
            if data == 0:
                break

            sum += data % 10
            data = data // 10

        if sum // 10 == 0:
            break
        
        data, sum = sum, 0
    
    print(sum % 10)
