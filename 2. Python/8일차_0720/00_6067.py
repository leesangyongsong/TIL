# 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
# 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D

a = int(input())
if a < 0 and a%2==0:
  print(f'{a}는 A타입(음수, 짝수)입니다.')
elif a < 0 and a%2==1:
  print(f'{a}는 B타입(음수, 홀수)입니다.')
elif a > 0 and a%2==0:
  print(f'{a}는 C타입(양수, 짝수)입니다.')
else:
  print(f'{a}는 D타입(양수, 홀수)입니다.')
