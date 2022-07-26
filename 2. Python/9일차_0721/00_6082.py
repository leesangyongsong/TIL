# 30보다 작은 정수 1개가 입력된다. (1~29)
# 1부터 그 수까지 순서대로 공백을 두고 수를 출력하는데, 3 or 6 or 9가 포함되어 있는 수인 경우, 그 수 대신 영문 대문자 X를 출력한다.

n = int(input())
for i in range(1, n+1):
  if i % 3 == 0:
    print('X', end=' ')
  else:
    print(i, end=' ')