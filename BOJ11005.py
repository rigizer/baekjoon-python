# https://www.acmicpc.net/problem/11005

system = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int, input().split())
result = '' 

while n != 0:
    result += system[n % b]
    n //= b
    
print(result[::-1])
