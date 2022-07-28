# https://www.acmicpc.net/problem/2979

a, b, c = map(int, input().split())
a_start, a_end = map(int, input().split())
b_start, b_end = map(int, input().split())
c_start, c_end = map(int, input().split())

time_list = [a_start, a_end, b_start, b_end, c_start, c_end]
time_min = min(time_list)
time_max = max(time_list)

coast = 0
for time in range(time_min, time_max):
    car_now = 0

    if a_start <= time < a_end:
        car_now += 1
    if b_start <= time < b_end:
        car_now += 1
    if c_start <= time < c_end:
        car_now += 1

    # 한 대당 비용만 지불하는 것이 아닌, 여러 대라면 여러 대 만큼 각자 비용을 내야함에 주의!
    if car_now == 1:
        coast += a
    elif car_now == 2:
        coast += (b * 2)
    elif car_now == 3:
        coast += (c * 3)

print(coast)
