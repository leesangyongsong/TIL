#  3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2 == 0:
  print(f'{a}는 짝수입니다.')
else:
  print(f'{a}는 홀수입니다.')
if b%2 == 0:
  print(f'{b}는 짝수입니다.')
else:
  print(f'{b}는 홀수입니다.')
if c%2 == 0:
  print(f'{c}는 짝수입니다.')
else:
  print(f'{c}는 홀수입니다.')
  