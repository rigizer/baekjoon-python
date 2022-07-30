# https://www.acmicpc.net/problem/1929

import math

m, n = map(int, input().split())

pnum_list = []

if m <= 2:
    # m이 1 혹은 2인경우 2라는 소수를 목록에 미리 추가
    # 이후의 i를 반복하는 for문은 2의 배수(짝수)를 모두 건너뛰어버리기 때문에 예외적으로 별도추가
    # if문을 넣지않고 무조건 추가하면 m이 2를 넘어버리는 경우에도 2가 추가되어 오류가 발생하기 때문이다.
    pnum_list.append(2)

if m % 2 == 0:
    # m이 짝수인 경우 어차피 건너뛰기 때문에 홀수로 만들어주기 위해 +1 처리
    m += 1

for i in range(m, n + 1, 2):
    if i == 1:
        continue

    is_pnum = True
    for j in range(3, int(math.sqrt(i)) + 1, 2):
        # 파이썬 for문이 해당수 미만까지만 반복하므로 math.sqrt(i)에 +1을 해주어야 한다. (정수값)
        # i에 루트를 씌워주는 이유는, i의 약수 중 루트 i에의 값보다 큰 약수는 루트 i보다 같거나 작은 약수의 배수이기 때문에 반복문을 돌려도 의미가 없기 때문이다.
        if i % j == 0:
            # 반복문을 돌리면서 나누어 떨어지는 수가 존재할 경우 j에 대한 for문을 돌리는 것을 중단과 동시에 소수판정 False 처리
            is_pnum = False
            break

    if is_pnum == True:
        pnum_list.append(i)

for pnum in pnum_list:
    print(pnum)
