# https://www.acmicpc.net/problem/5026

n = int(input())

for _ in range(n) :
    data = input()
      if data == 'P=NP' :
        print('skipped')
    else :
        a, b = map(int, data.split('+'))
        print(a + b)
