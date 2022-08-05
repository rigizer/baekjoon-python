# https://www.acmicpc.net/problem/9506

while True:
    n = int(input())

    if n == -1:
        break

    divisor_list = []
    for i in range(1, n):
        if n % i == 0:
            divisor_list.append(i)

    if n == sum(divisor_list):
        print('{} = {}'.format(n, ' + '.join(str(i) for i in divisor_list)))
    else:
        print('{} is NOT perfect.'.format(n))
