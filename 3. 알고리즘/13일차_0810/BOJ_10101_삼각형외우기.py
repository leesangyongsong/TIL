a = int(input())
b = int(input())
c = int(input())

# 1차
if a == b == c == 60:
  print('Equilateral')
elif a + b + c == 180 and (a == b or b == c or a == c):
  print('Isosceles')
elif a + b + c == 180 and (a != b != c):
  print('Scalene')
elif a + b + c != 180:
  print('Error')

# 코드 정리
if a + b + c == 180:
  if a == b == c == 60:
    print('Equilateral')
  elif a == b or b == c or a == c:
    print('Isosceles')
  else:
    print('Scalene')
else:
  print('Error')