# 체스판 입력받기
S = [input() for _ in range(8)]

count = 0
# 돌려돌려 돌림판
for i in range(8):
  for j in range(8):
    # 홀수 줄 홀수 번째에 F 오면 카운트
    if i % 2 == 1 and j % 2 == 1 and S[i][j] == "F":
      count += 1
    # 짝수 줄 짝수 번째에 F 오면 카운트
    if i % 2 == 0 and j % 2 == 0 and S[i][j] == "F":
      count += 1
print(count)