# https://www.acmicpc.net/problem/2028

n = int(input())    # 테스트케이스 반복횟수

for i in range(n):
    num = int(input())  # 해당 케이스를 체크할 변수
    k = len(str(num))   # 변수의 길이
    if str(num**2)[-k:] == str(num):
        print("YES")
    else:
        print("NO")
