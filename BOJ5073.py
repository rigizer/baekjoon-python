# https://www.acmicpc.net/problem/5073

while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    if (a + b > c) and (b + c > a) and (a + c > b):
        if a == b and b == c and c == a:
            print('Equilateral')
        elif (a == b and a != c) or (b == c and b != a) or (c == a and a != b):
            print('Isosceles')
        elif a != b and b != c and c != a:
            print('Scalene')
        
    else:
        print('Invalid')
