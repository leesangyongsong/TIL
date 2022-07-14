# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

# word = 'banana'
# count = 0
# for i in word:
#     if i == 'a':
#         break
#     else:
#         count += 1
# if count == len(word):
#     count = -1
# print(count)

# # 추가 문제 : 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.

# word2 = 'HappyHacking'
# count2 = 0
# for i2 in word2:
#     count2 += 1
#     if i2 == 'a':
#         print(count2, end = ' ')

# 강사님 풀이 #1
word = 'banana'
# 문자로 순회하는 것이 아니라!
# 인덱스로 접근해서쓰자.
# 원하는 숫자? 0, 1, 2, 3, 4, 5
# 얻는 방법은? range(len(word)) => range(6) => 0 ~5
for idx in range(len(word)):
    # print(idx, word[idx])
    # 알파벳이 a일때
    if word[idx] == 'a':
        print(idx)
        break
# for문을 다 돌았다는 뜻은
# 한번도 break에 안 걸렸다.
# 즉, a는 없었다.
else:
    print(-1)

# 강사님 풀이 #2