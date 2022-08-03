# 게임 참가자 수 입력
n = int(input())

# 게임별 빈리스트 생성 후 제출한 점수를 받기
first = []
second = []
third = []

for i in range(n):
  a, b, c = map(int, input().split())
  first.append(a)
  second.append(b)
  third.append(c)

# 게임별 리스트 내 동일점수 없을 경우 개인점수 추가
for j in range(n):
  score = 0
  if first.count(first[j]) == 1:
    score += first[j]
  if second.count(second[j]) == 1:
    score += second[j]
  if third.count(third[j]) == 1:
    score += third[j]
  # 세번째 게임까지 확인 후 합산점수 참가자 순서대로 최종점수 반환
  print(score)