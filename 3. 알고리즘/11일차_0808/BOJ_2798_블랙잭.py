N, M = map(int, input().split()) # 카드 개수 N, 카드 합 한도 M 입력
cards = list(map(int, input().split())) # N개만큼의 카드에 쓰여 있는 수
accommodating = [] # 빈 리스트 생성
# 카드 합 한도를 넘지 않는 3 카드의 합을 리스트에 넣는 브루트포스 실행
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      sum_result =  cards[i] + cards[j] + cards[k]
      if sum_result > M:
        continue
      else:
        accommodating.append(sum_result)
# 조건을 만족하는 카드 합 중 가장 큰 값 출력
print(max(accommodating))