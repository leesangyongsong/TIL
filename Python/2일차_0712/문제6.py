# 주어진 리스트 numbers에서 최대값을 구하여 출력하시오.
numbers = {0, 20, 100}
a = 0
for i in numbers:
    if i > a:
        a = i
print(a)


numbers2 = [0, 20, 100, 50, -60, 50, 100] # 100
a = 0
for i in numbers2:
    if i > a:
        a = i
print(a)

numbers3 = [0, 1, 0] # 1
a = 0
for i in numbers3:
    if i > a:
        a = i
print(a)

numbers4 = [-10, -100, -30] # -10 
result = numbers4[0]
for i in numbers4:
    if i > result:
        result = i
print(result)
