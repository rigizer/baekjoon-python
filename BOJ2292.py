# https://www.acmicpc.net/problem/2292

n = int(input())

line = 1
i = 1

if n == 1:
    print(1)
else:
    while True:
        if n <= i:
            print(line)
            break
        
        i += (6 * line)
        line += 1 
