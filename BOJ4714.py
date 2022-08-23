# https://www.acmicpc.net/problem/4714

while True:
    data = float(input())
    if data < 0:
        break

    print('Objects weighing {:.2f} on Earth will weigh {:.2f} on the moon.'.format(data, data * 0.167))
