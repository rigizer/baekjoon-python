# https://www.acmicpc.net/problem/8980

# 마을수 N, 트럭 용량 C
n, c = map(int, input().split())

# 박스 정보 개수 M
m = int(input())

# 박스 정보 입력 (0: 보내는 마을, 1: 받는 마을, 2: 박스 개수)
box = [list(map(int, input().split())) for _ in range(m)]

# 조건1: 박스를 트럭에 실으면, 받는 마을에서만 내린다
# 조건2: 트럭은 지나온 마을로 되돌아가지 않는다
# 조건3: 박스들 중 일부만 배송할 수도 있다

# 받는 마을 기준으로 박스조건 정렬, 겹치면 보내는 마을이 더 빠른경우
box.sort(key=lambda x: x[1])

# 최대 배송할 수 있는 박스 수
answer = 0

# 각 마을에서의 남은 공간 기록
space = [c] * (n + 1)

# 박스 정보만큼 반복
for i in range(m):
    # 트럭 용량만큼 옮길 수 있다고 가정
    temp = c

    # 목적지까지 거쳐가는 마을 중 적재량이 가장 작은 적재량 선택
    for j in range(box[i][0], box[i][1]):
        temp = min(temp, space[j])

    # 적재량과 가장 작은 적재량 중 적은 쪽을 선택
    temp = min(temp, box[i][2])

    # 박스를 싣기로 선택한 수 만큼 거져가는 마을에 적재량 감소처리
    for j in range(box[i][0], box[i][1]):
        space[j] -= temp

    answer += temp

print(answer)
