# 초심자의 회문 검사
# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.

def palindrome(word):
  if word == word[::-1]:
    return 1
  else:
    return 0

t = int(input())
for test_case in range(1, t+1):
  n = str(input())  

  print("#{} {}".format(test_case, palindrome(n)))