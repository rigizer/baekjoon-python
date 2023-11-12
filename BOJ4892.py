t = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break
    
    n1 = 3 * n0
    if n1 % 2 == 0:
        n2 = n1 // 2
    else:
        n2 = (n1 + 1) // 2
    n3 = 3 * n2
    n4 = n3 // 9
    
    print('{}. {} {}'.format(t,'even' if n1 % 2 == 0 else 'odd', n4)) 
    t += 1
