word = input()
for i in "CAMBRIDGE":
  word = word.replace(i, "")
print(word)

# 1. 변수 word에 이메일의 내용을 입력한다.
# 2. for문을 i에 CAMBRIDGE를 넣으며 돌면서 word에 i가 있다면 
#     replace()함수를 사용하여 i를 ""으로 바꾸어준다.
# 3. 최종적으로 word를 출력한다.

# 다른 풀이1
a = "CAMBRIDGE"
s = list(input())
for i in a:
  for j in range(len(s)):
    if i == s[j]:
      s[j] = ''
for i in s:
  print(i, end='')

# 다른 풀이2
cambridge = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
word = input()
result = ''
for i in word:
  if i not in cambridge:
    result += i
print(result)