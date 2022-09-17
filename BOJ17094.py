# https://www.acmicpc.net/problem/17094

n = int(input())
s = input()

cnt_e = 0
cnt_two = 0

for i in s:
    if i == '2':
        cnt_two += 1
    elif i == 'e':
        cnt_e += 1

if cnt_e > cnt_two:
    print('e')
elif cnt_e < cnt_two:
    print(2)
else:
    print('yee')
