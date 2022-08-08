# 초안
test_case = int(input())
for i in range(test_case):
  car_price = int(input())
  option_plus = int(input())
  for j in range(option_plus):
    option, price = map(int, input().split())
    car_price += option * price
  print(car_price)

# 코드 간소화
for i in range(int(input())):
  car_price = int(input())
  for j in range(int(input())):
    option, price = map(int, input().split())
    car_price += option * price
  print(car_price)