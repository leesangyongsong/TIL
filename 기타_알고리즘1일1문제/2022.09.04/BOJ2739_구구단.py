# 기본 표기
n = int(input())
for i in range(1, 10):
  print(n, '*', i, '=', n * i)

# 다른 표기 1
n = int(input())
for i in range(1,10):
  print("%d * %d = %d" %(n, i, n * i))

# 다른 표기 2
n = int(input())
for i in range(1, 10):
  print(f'{n} * {i} = {n * i}')