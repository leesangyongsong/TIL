# 📚 알고리즘 11일차

## 📌 지난 시간 복습
```python
# 2차원 리스트 회전
1. 왼쪽으로 90도 회전하기
  matrix =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]

  n = 3
  rotated_matrix = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      rotated_matrix[i][j] = matrix[j][n-i-1]

2. 오른쪽으로 90도 회전하기
  matrix =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]

  n = 3
  rotated_matrix = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      rotated_matrix[i][j] = matrix[n-j-1][i]
```

## 📌 완전탐색I(Exhaustive Search)
```python
1. 무식하게 풀기(Brute-force)
  Brute-force는 '모든 경우의 수'를 탐색하여 문제를 해결하는 방식이다.
  - '브루트포스'라곧돋 하며, 무식하게 밀어붙인다는 뜻읻다.
  - 가장 단순한 풀이 기법이며, 
    단순 조건문과 반복문을 이용해서 풀 수 있다.
  - 복잡한 알고리즘보다는, 
    아이디어를 어떻게 코드로 구현할 것인지가 중요하다.

2. 델타 탐색(Delta Search)
  지금까지는 모든 경우의 수를 따지는 일반적인 완전탐색을 알아보았다.
  '이차원 리스트의 완전탐색'에서 많이 등장하는 유형인 
  '델타 탐색(상하좌우 탐색)'을 알아보자.

  (0, 0)에서부터 이차원 리스트의 모든 원소를 순회하며
  '각 지점에서 상하좌우에 위치한 다른 지점을 조회하거나 이동'하는 방식

  이차원 리스트의 인덱스(좌표)의 조작을 통해서 상하좌우 탐색을 한다.
  이때 행과 열의 변량인 -1, +1을 '델타(delta)값'이라 한다.

  # 이차원 리스트의 상하좌우 탐색 정리
    # 1. 델타값 정의(상하좌우)
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    
    # 2. 이차원 리스트 순회
    for x in range(n):
      for y in range(m):

      # 3. 델타값을 이용해 상하좌우 이동
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]

        # 범위를 벗어나지 않으면 갱신
          if 0 <= nx 3 and 0<= ny < 3:
            x = nx
            y = ny

      


```

## 📌
```python

```