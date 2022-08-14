# https://www.acmicpc.net/problem/9012

t = int(input())
for i in range(t):
    data = input()
    stack = list()

    for d in data:
        test = d
        if len(stack) == 0:
            stack.append(d)
        else:
            if stack[-1] == '(' and d == ')':
                stack.pop()
            else:
                stack.append(d)

    print('YES' if len(stack) == 0 else 'NO')
