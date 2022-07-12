# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
numbers = [0, 20, 100] # 20
numbers2 = [0, 20, 100, 50, -60, 50, 100] # 50
numbers3 = [0, 1, 0] # 0
numbers4 = [-10, -100, -30] # -30

numbers = set(numbers)
numbers = list(numbers)
numbers.sort()
print(numbers[-2])

numbers2 = set(numbers2)
numbers2 = list(numbers2)
numbers2.sort()
print(numbers2[-2])

numbers3 = set(numbers3)
numbers3 = list(numbers3)
numbers3.sort()
print(numbers3[-2])

numbers4 = set(numbers4)
numbers4 = list(numbers4)
numbers4.sort()
print(numbers4[-2])