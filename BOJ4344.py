c = int(input())

for i in range(c):
    data = list(map(int, input().split()))
    n = data[0]
    data.pop(0)
    s = sum(data)
    a = float(s) / n

    r = 0
    for j in data:
        if j > a:
            r += 1

    print('{:.3f}%'.format(float(r * 100) / n))
