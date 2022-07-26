# https://www.acmicpc.net/problem/1100

isWhiteFirst = True
count = 0

for line in range(8):
    t = input()
    isWhite = True if isWhiteFirst else False
    for i in t:
        if i == 'F' and isWhite:
            count += 1
        
        isWhite = False if isWhite else True

    isWhiteFirst = False if isWhiteFirst else True

print(count)
