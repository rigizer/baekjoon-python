# https://www.acmicpc.net/problem/4949

while True:
    data = input()
    if data == '.':
        break

    stack = []
    for d in data:
        if d not in ['(', ')', '[', ']']:
            continue

        size = len(stack)
        if d == '(':
            stack.append(d)
        elif d == ')':
            if size == 0:
                stack.append(d)
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(d)
        elif d == '[':
            stack.append(d)
        elif d == ']':
            if size == 0:
                stack.append(d)
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(d)

    print('yes' if len(stack) == 0 else 'no')
