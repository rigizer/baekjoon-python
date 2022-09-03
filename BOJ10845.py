# https://www.acmicpc.net/problem/10845

import sys
from collections import deque

tc = int(input())
queue = deque()
result = []

for t in range(tc):
    q_size = len(queue)
    cmd = sys.stdin.readline().rstrip()
    if 'push' in cmd:
        cmd = list(map(str, cmd.split()))
        queue.append(int(cmd[1]))

    else:
        if cmd == 'pop':
            if q_size == 0:
                result.append(-1)
            else:
                result.append(queue.popleft())

        elif cmd == 'size':
            result.append(q_size)

        elif cmd == 'empty':
            result.append(1 if q_size == 0 else 0)

        elif cmd == 'front':
            if q_size == 0:
                result.append(-1)
            else:
                result.append(queue[0])

        elif cmd == 'back':
            if q_size == 0:
                result.append(-1)
            else:
                result.append(queue[q_size - 1])

print('\n'.join([str(i) for i in result]))
