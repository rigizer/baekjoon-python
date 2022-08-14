# https://www.acmicpc.net/problem/18258

# input() 쓰면 속도 느리니 주의
# sys.stdin.readline() 쓰면 엔터키가 \n으로 입력됨에 주의

import sys
from collections import deque

queue = deque()
result = ''

for tc in range(int(sys.stdin.readline())):
    size = len(queue)
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(int(command[1]))

    elif command[0] == 'pop':
        if size == 0:
            result += '-1\n'
        else:
            value = queue.popleft()
            result += str(value) + '\n'

    elif command[0] == 'size':
        result += str(size) + '\n'

    elif command[0] == 'empty':
        if size == 0:
            result += '1\n'
        else:
            result += '0\n'

    elif command[0] == 'front':
        if size == 0:
            result += '-1\n'
        else:
            value = queue.popleft()
            queue.appendleft(value)
            result += str(value) + '\n'

    elif command[0] == 'back':
        if size == 0:
            result += '-1\n'
        else:
            value = queue.pop()
            queue.append(value)
            result += str(value) + '\n'

print(result)
