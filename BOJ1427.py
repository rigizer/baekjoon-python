# https://www.acmicpc.net/problem/1427

n = [int(i) for i in input()]
n.sort(reverse=True)
print(''.join([str(i) for i in n]))
