# https://www.acmicpc.net/problem/9095

t = int(input())
nums = [int(input()) for _ in range(t)]

cnt = 0

def dp(now, limit):
    global cnt
    if now == limit:
        cnt += 1
        return
    elif now > limit:
        return

    dp(now + 1, limit)
    dp(now + 2, limit)
    dp(now + 3, limit)


for n in nums:
    dp(0, n)
    print(cnt)
    cnt = 0
