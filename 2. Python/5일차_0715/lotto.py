import random

# 1~45까지의 숫자!
# 그 중에 6개
numbers = random.sample(range(1, 46), 6)
numbers.sort()
print(numbers, type(numbers))

# 원하는만큼 로또 돌리기
# import random
# n = int(input('얼마쓸래'))
# for i in range(n):
#     numbers = random.sample(range(1, 46), 6)
#     numbers.sort()
#     print(numbers, type(numbers))