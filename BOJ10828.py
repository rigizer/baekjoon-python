# https://www.acmicpc.net/problem/10828

import sys

stack = []

for tc in range(int(sys.stdin.readline())):
    size = len(stack)
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if size == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(size)
    elif command[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if size == 0:
            print(-1)
        else:
            print(stack[-1])
