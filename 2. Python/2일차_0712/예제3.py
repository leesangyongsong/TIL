# 1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드를 작성하시오.
# 처음 시작 값
n = 0
# 0부터 더하기 위해서
result = 0
# user_input 값
user_input = int(input())

while n <= user_input:
    result += n
    n += 1
print(result)