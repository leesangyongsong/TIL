# 수상하게 높은 금액은 의심해야지...
# 1차 코드
total_price = int(input())
N = int(input())
product_list = []

for i in range(N):
  price, quantity = map(int, input().split())
  product_list.append(price * quantity)

if sum(product_list) == total_price:
  print('Yes')
else:
  print('No')

# 코드 간소화
total_price = int(input())
product_list = []

for i in range(int(input())):
  price, quantity = map(int, input().split())
  product_list.append(price * quantity)

print('Yes' if sum(product_list) == total_price else 'No')


