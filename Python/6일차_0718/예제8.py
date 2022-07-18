# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# "모음 개수 구하기"

# Input
word = 'HappyHacking'

count = 0
for char in word:
    if char == 'a' or char == 'o' or char == 'u' or char == 'i' or char == 'e':
        count += 1
print(count)

# output
# 3