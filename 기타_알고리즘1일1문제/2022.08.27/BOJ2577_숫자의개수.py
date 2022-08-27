## ver1. 문자열 활용하기

A = int(input())
B = int(input())
C = int(input())

Mul = str(A * B * C)

for i in range(0, 9):
  print(Mul.count(str(i)))



## ver2. 리스트 활용하기

# 세 개의 자연수 입력
a = int(input())
b = int(input())
c = int(input())

# 세 자연수의 곲을 리스트로 변환 
result = list(map(int, str(a*b*c)))

# 0부터 10까지 반복하여 몇 번 쓰였는지 count하여 출력
for i in range(10):
    print(result.count(i))
    
    # result.count(0) 0의 갯수 출력
    # result.count(1) 1의 갯수 출력
    # result.count(2) 2의 갯수 출력
    # result.count(3) 3의 갯수 출력
    # result.count(4) 4의 갯수 출력
    # result.count(5) 5의 갯수 출력
    # result.count(6) 6의 갯수 출력
    # result.count(7) 7의 갯수 출력
    # result.count(8) 8의 갯수 출력
    # result.count(9) 9의 갯수 출력
    # result.count(10) 10의 갯수 출력