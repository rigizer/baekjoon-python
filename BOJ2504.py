# https://www.acmicpc.net/problem/2504

data = input()
stack = []
result = 0
isOk = True

for d in data:
    if len(stack) == 0:
        stack.append(d)
        continue

    if d == '(':
        stack.append(d)
    elif d == '[':
        stack.append(d)
    elif d == ')':
        temp_list = []  # 괄호 안에 있는 (x)에 대한 숫자를 더하기 위한 임시리스트
        temp = stack.pop()
        while True:
            if type(temp) == str:
                if temp == '(':
                    break
                else:
                    isOk = False
                    break

            temp_list.append(temp)

            if len(stack) == 0:
                # 더 이상 앞에 여는 기호가 없는데 숫자와 닫는 기호로만 있는 경우에 대한 조건문 추가
                isOk = False
                break

            temp = stack.pop()

        stack.append(2 * (1 if len(temp_list) == 0 else sum(temp_list)))

    elif d == ']':
        temp_list = []  # 괄호 안에 있는 [x]에 대한 숫자를 더하기 위한 임시리스트
        temp = stack.pop()
        while True:
            if type(temp) == str:
                if temp == '[':
                    break
                else:
                    isOk = False
                    break

            temp_list.append(temp)

            if len(stack) == 0:
                # 더 이상 앞에 여는 기호가 없는데 숫자와 닫는 기호로만 있는 경우에 대한 조건문 추가
                isOk = False
                break

            temp = stack.pop()

        stack.append(3 * (1 if len(temp_list) == 0 else sum(temp_list)))

    if isOk == False:
        break

if isOk == True:
    if True in [(type(i) == str) for i in stack]:
        # [[와 같은 케이스에 대한 조건문 추가
        print(0)
    else:
        result = sum(stack)
        print(result)
else:
    print(0)
