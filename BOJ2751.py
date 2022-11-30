# https://www.acmicpc.net/problem/2751

data = [int(input()) for _ in range(int(input()))]
print('\n'.join(str(i) for i in sorted(data)))
