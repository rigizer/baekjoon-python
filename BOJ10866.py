# https://www.acmicpc.net/problem/10866

import sys
from collections import deque

queue = deque()
tc = int(sys.stdin.readline())

for _ in range(tc):
    size = len(queue)
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        queue.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        queue.append(int(command[1]))
    elif command[0] == 'pop_front':
        if size == 0:
            print(-1)
            continue

        print(queue.popleft())
    elif command[0] == 'pop_back':
        if size == 0:
            print(-1)
            continue

        print(queue.pop())
    elif command[0] == 'size':
        print(size)
    elif command[0] == 'empty':
        print(1 if size == 0 else 0)
    elif command[0] == 'front':
        if size == 0:
            print(-1)
            continue

        print(queue[0])
    elif command[0] == 'back':
        if size == 0:
            print(-1)
            continue

        print(queue[size - 1])
