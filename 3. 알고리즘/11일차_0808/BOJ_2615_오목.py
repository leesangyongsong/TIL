import sys

sys.stdin = open("_오목.txt")

# 우 하 우상 우하
dy = [0, 1, -1, 1]
dx = [1, 0, 1, 1]
BLACK = 1
WHITE = 2
N = 9

board = []

# 오목판 상황 입력
for _ in range(N):
  # 하나의 행을 입력
  temp_list = list(map(int, input().split()))
  board.append(temp_list)

# 이중 반복문
for y in range(N):
  # 델타 검색
  for x in range(N):
    # 방향이 바뀔 때마다 돌의 개수가 갱신(0)
    for d in range(4):
      # 다음 좌표 탐색
      ny = y + dy[d]
      nx = x + dx[d]

      while True:
        # 인덱스 조건
        if not (-1 < ny < N and -1 < nx < N):
          break
        # 같은색(값) 돌인지 확인하는 조건
        if not(board[y][x] == board[ny][nx]):
          break

        # 같은 값이고 범위를 벗어나지 않으면
        stone_count += 1

        # 같은 방향 다음 좌표를 탐색
        ny = ny + dy[d]
        nx = nx + dx[d]

      # 돌의 개수가 5개라면
      if stone_count == 5:
        # 이전 좌표
        prev_y = y - dy[d]
        prev_x = x - dx[d]

        # 육목인지 판단
        # 조건 1. 이전 좌표가 범위를 벗어나면 오목
        if not (-1 < prev_y < N and -1 < prev_x < N):

        # 조건 2. 기준 좌표의 값과 이전 좌표의 값이 다르면 오목
        if board[y][x] != board[prev_y][prev_x]: