# https://www.acmicpc.net/problem/18409

n = int(input())
s = str(input())
count = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
        
print(count)
