# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
word = 'good' # banana

for i in word:
    upper = chr(ord(i) - 32)
    print(upper, end='')

# 강사님 풀이
# word = 'banana'
# result = ''
# for문 작성 후
# for char in n word:
# 1. 알파벳을 숫자로 바꾸고
# number = ord(char)
# 2. 그 숫자에 -32를 하고
# number = number - 32
# 3. 다시 숫자를 알파벳으로 바꾼다.
# result += chr(number)
# 출력
# print(result)