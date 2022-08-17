# https://www.acmicpc.net/problem/5430

from collections import deque

tc = int(input())
for _ in range(tc):
    isError = False
    isReverse = False # 매번 명령마다 queue.reverse()를 하면 비효율적, 시간초과 발생.

    ac = input()
    n = int(input())
    queue = deque(list(input()[1:-1].split(',')))

    for command in ac:
        if command == 'R':
            isReverse = False if isReverse == True else True
        elif command == 'D':
            if len(queue) == 0 or n == 0:
                isError = True
                break

            queue.pop() if isReverse == True else queue.popleft()

        if isError == True:
            break

    if isError == True:
        print('error')
        continue

    if isReverse == True:
        queue.reverse()

    print('[{}]'.format(','.join(queue)))
