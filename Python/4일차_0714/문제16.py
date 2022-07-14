# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 

word = 'apple'
count = 0
for i in word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u': # if i == 'aeiou' 로 치환 가능
        count += 1
print(count)