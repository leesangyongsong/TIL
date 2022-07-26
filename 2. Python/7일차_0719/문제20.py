# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 
# input : 123
# output : 6

# 0. 변수 설정
N = int(input())
answer = 0

# 1. 입력된 N(정수형)을 문자로 형 변환한다.
# 2. 형 변환된 문자열의 길이만큼 반복하면서 각 자리 값을 갖고 온다.
# 3. 갖고 온 자리값을 숫자로 변환해 변수에 합한다.
for n in str(N): 
  answer += int(n) 
print(answer)
