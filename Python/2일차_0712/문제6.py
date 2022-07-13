# 주어진 리스트 numbers에서 최대값을 구하여 출력하시오.
numbers = [0, 20, 100]
# max_num = float("-inf")
max_num = numbers[0]
# 1. 반복
for n in numbers:
    # print(n)
    # 2. 만약, max값이 n보다 작으면 바꾼다.
    if  max_num < n:
        max_num = n
print(max_num)


# numbers2 = [0, 20, 100, 50, -60, 50, 100] # 100
# numbers3 = [0, 1, 0] # 1
# numbers4 = [-10, -100, -30] # -10 

