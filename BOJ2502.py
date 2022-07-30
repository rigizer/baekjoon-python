d, k = map(int, input().split())

before_a = 0
before_b = 1
a = 1
b = 1
result_a = 1  # 최소값은 1
result_b = 1  # 최소값은 1

for i in range(3, d):
    temp_a = before_a + a
    temp_b = before_b + b

    before_a = a
    before_b = b

    a = temp_a
    b = temp_b

while True:
    if (k - (a * result_a)) % b != 0:
        result_a += 1
        continue

    result_b = int((k - (a * result_a)) / b)
    break

print(result_a)
print(result_b)
