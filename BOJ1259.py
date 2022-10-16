# https://www.acmicpc.net/problem/1259

while True:
    data = input()
    if data == '0': break
    print('yes' if data == data[::-1] else 'no')
