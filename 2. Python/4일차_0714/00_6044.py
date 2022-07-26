# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단, b는 0이 아니다.

a = int(input())
b = int(input())
print('더하기', a + b)
print('빼기', a - b)
print('곱하기', a * b)
print('나누기', a / b)
print('몫' , a // b)
print('나머지', a % b)