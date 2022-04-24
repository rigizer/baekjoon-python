def inputArr():
    in_arr = input().split()
    n = int(in_arr[0])
    arr = [ 0, 0, 0, 0 ]
    for i in range(1, n + 1):
        arr[int(in_arr[i]) - 1] += 1

    return arr

roundMax = int(input())

list = list()
for round in range(0, roundMax):
    arrA = inputArr()
    arrB = inputArr()

    aWin = False
    bWin = False

    if arrA[3] != arrB[3]:
        if arrA[3] > arrB[3]:
            aWin = True
        else:
            bWin = True
    else:
        if arrA[2] != arrB[2]:
            if arrA[2] > arrB[2]:
                aWin = True
            else:
                bWin = True
        else:
            if arrA[1] != arrB[1]:
                if arrA[1] > arrB[1]:
                    aWin = True
                else:
                    bWin = True
            else:
                if arrA[0] != arrB[0]:
                    if arrA[0] > arrB[0]:
                        aWin = True
                    else:
                        bWin = True
    
    if aWin == True and bWin == False:
        list.append("A")
    elif aWin == False and bWin == True:
        list.append("B")
    else:
        list.append("D")

for s in list:
    print(s)
