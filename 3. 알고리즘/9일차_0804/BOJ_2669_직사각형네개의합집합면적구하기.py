# x, y 평면 생성
board = [[0 for _ in range(101)] for _ in range(101)]

# 입력값 생성
for _ in range(4):
  x1, y1, x2, y2 = map(int, input().split())
  
  #사각형 부분만 1로 바꾸어줌
  for i in range(x1, x2):
    for j in range(y1, y2):
      board[i][j] = 1

result = 0
for k in board:
  result += sum(k)
print(result)