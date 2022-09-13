# https://www.acmicpc.net/problem/11034

while True:
    try:
        A, B, C = map(int, input().split())
        print(max(B-A, C-B)-1)
    except:
        break
