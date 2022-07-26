# 로또 당첨번호 1회 출력
# import random

# number = range(1, 46)
# result = random.sample(number, 6)

# print(result)

# 5회 반복하고 싶을 경우
# import random

# for i in range(5):
#   number = range(1, 46)
#   result = random.sample(number, 6)
#   print(result)

# n회 구매하고 싶을 때
import random

def generate_lotto(n):
  result = []
  for i in range(n):
    numbers = range(1, 46)
    pick = random.sample(numbers, 6)
    pick.sort()
    result.append(pick)
  return result