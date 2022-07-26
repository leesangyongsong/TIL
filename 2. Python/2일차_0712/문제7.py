# 주어진 리스트 numbers에서 최소값을 구하여 출력하시오.
numbers = [0, 20, 100]
result = numbers[0]
for i in numbers:
    if i < result:
        result = i
print(result)

numbers2 = [0, 20, 100, 50, -60, 50, 100] # -60
result = numbers2[0]
for i in numbers2:
    if i < result:
        result = i
print(result)

numbers3 = [0, 1, 0] # 0
result = numbers3[0]
for i in numbers3:
    if i < result:
        result = i
print(result)

numbers4 = [-10, -100, -30] # -100
result = numbers4[0]
for i in numbers4:
    if i < result:
        result = i
print(result)