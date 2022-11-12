# https://www.acmicpc.net/problem/1018

n, m = map(int, input().split())
data = [[j for j in input()] for i in range(n)]

min = 1e9
for a in range(n - 8 + 1):
    for b in range(m - 8 + 1):
        for c in range(2):
            temp_min = 0

            for i in range(a, a + 8):
                for j in range(b, b + 8):
                    if min <= temp_min:
                        break

                    if c == 0:    # 첫 시작이 B인 경우
                        if i % 2 == 0:
                            if j % 2 == 0:
                                if data[i][j] != 'B': temp_min += 1
                            elif j % 2 == 1:
                                if data[i][j] != 'W': temp_min += 1
                        elif i % 2 == 1:
                            if j % 2 == 0:
                                if data[i][j] != 'W': temp_min += 1
                            elif j % 2 == 1:
                                if data[i][j] != 'B': temp_min += 1

                    elif c == 1:  # 첫 시작이 W인 경우
                        if i % 2 == 0:
                            if j % 2 == 0:
                                if data[i][j] != 'W': temp_min += 1
                            elif j % 2 == 1:
                                if data[i][j] != 'B': temp_min += 1
                        elif i % 2 == 1:
                            if j % 2 == 0:
                                if data[i][j] != 'B': temp_min += 1
                            elif j % 2 == 1:
                                if data[i][j] != 'W': temp_min += 1

            if min > temp_min:
                min = temp_min

print(min)
