# 행과 열 크기 받아 이차원 리스트 생성
n, m = map(int, input().split())
guard = [input() for _ in range(n)]

# 행과 열에 필요한 경비원 수 카운트
row, col = 0, 0

for i in range(n):
  if 'X' not in guard[i]:
    row += 1
        
for j in range(m):
  if "X" not in [guard[i][j] for i in range(n)]:        
    col += 1

# 더 많이 필요한 경비원 수 출력
print(max(row, col))