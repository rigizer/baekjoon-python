# https://www.acmicpc.net/problem/2503

def data_maker():
    data = []

    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                continue
            for k in range(1, 10):
                if i != j and j != k and k != i:
                    data.append(str(i) + str(j) + str(k))

    return data


n = int(input())
data = data_maker()
for t in range(1, n + 1):
    nums, s, b = map(int, input().split())
    nums = str(nums)

    idx = 0
    max_idx = len(data)
    for i in range(max_idx):
        ss = 0
        bb = 0

        for i in range(3):
            if nums[i] == data[idx][i]:
                ss += 1
            else:
                if nums[i] in data[idx]:
                    bb += 1

        if ss != s or bb != b:
            data.pop(idx)
            max_idx -= 1
            continue

        idx += 1

print(len(data))
