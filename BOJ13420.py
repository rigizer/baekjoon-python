# https://www.acmicpc.net/problem/13420

t = int(input())
for _ in range(t):
    data = list(input().split())
    if data[1] == '+':
        print('correct' if int(data[0]) + int(data[2]) == int(data[4]) else 'wrong answer')
    elif data[1] == '-':
        print('correct' if int(data[0]) - int(data[2]) == int(data[4]) else 'wrong answer')
    elif data[1] == '*':
        print('correct' if int(data[0]) * int(data[2]) == int(data[4]) else 'wrong answer')
    elif data[1] == '/':
        print('correct' if int(data[0]) // int(data[2]) == int(data[4]) else 'wrong answer')
