# 주어진 숫자부터 0까지 순서대로 찍어보세요
# 아래는 입력된 숫자가 N일 때 거꾸로 출력하는 예시입니다

n = int(input('숫자를 입력하세요: '))
for i in range (n, -1, -1):
  print(i , end=' ')