# https://www.acmicpc.net/problem/1920

import sys
sys.setrecursionlimit(100000)

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()


def binary_search(i, start, end):
    if start > end:
        return False

    if a[start] > i or a[end] < i:
        return False

    mid = start + int(end / 2)

    if a[mid] == i:
        return True

    if i < a[mid]:
        return binary_search(i, start, mid - 1)
    else:
        return binary_search(i, mid, end)


for i in b:
    result = binary_search(i, 0, len(a) - 1)
    print(1 if result else 0)
