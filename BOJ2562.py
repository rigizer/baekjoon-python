# https://www.acmicpc.net/problem/2562

num_list = []
for i in range(9):
    num_list.append(int(input()))

max_num = 0
max_idx = 0
for i in range(9):
    if max_num < num_list[i]:
        max_num = num_list[i]
        max_idx = i + 1

print(max_num)
print(max_idx)
