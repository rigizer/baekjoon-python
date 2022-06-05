# https://www.acmicpc.net/problem/2547

for _ in range(int(input())):
    input()
    student_num = int(input())
    candy = 0
    for __ in range(student_num):
        candy += int(input())

    if candy % student_num == 0:
        print("YES")
    else:
        print("NO")
