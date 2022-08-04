# 📚 알고리즘 8일차

## 📌 1. 이차원 리스트
```python
이차원 리스트는 '리스트를 원소로 가지는 리스트'일 뿐이다.

# 행렬 개념처럼 생각해보기
  matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
  ]

  print(matrix[0][0])
  >>> 1

  print(matrix[1][2])
  >>> 6

  print(matrix[2][0])
  >>> 7

# 특정 값으로 초기화된 이차원 리스트 만들기
1. 직접 작성
  martrix1 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
  ]

2. 반복문으로 작성
  # 100 * 100 행렬
  matrix = []
  for _ in range(100):
    matrix.append([0] * 100)

  # n * m 행렬
  n = 4
  m = 3
  matrix = []
  for _ in range(n):
    matrix.append([0] * m)
  # matrix = [[0] * m for _ in range(n)]

  print(matrix)
  >>> [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

  pprint(matrix)
  >>> [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
  ]

3. 리스트 컴프리헨션으로 작성
  

```

## 📌 2. 입력 받기
```python
1. 행렬의 크기가 미리 주어지는 경우
  matrix = []

  for _ in range(8):
    line = list(input())
    matrix.append(line)
  # matrix = [list(input()) for _ in ragne(8)] 
  # 리스트 컴프리헨션을 통해 간단히 입력을 받을 수 있다.

# 3 X 3 크기의 입력을 받아보자
  1 2 3
  4 5 6
  7 8 9

  matrix = []
  for _ in range(3):
    line = list(map(int, input().split()))
    matrix.append(line)
  # matrix = [list(map(int, input().split())) for _ in range(3)]

```

## 📌 3. 순회
```python
# 이차원 리스트를 단순히 출력하면 아래와 같이 나온다.
    
  matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
  ]

  print(matrix)
  [1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]

# 인덱스를 통해 각각 출력하면 가능하다!
  print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3])
  print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3])
  print(matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3])

  >>> 1 2 3 4
  >>> 5 6 7 8
  >>> 9 0 1 2

# 숫자가 커지면 노가다로 하기 힘듬!!
# 해결방법
1. 이중 for문을 이용한 행 우선 순회
  for i in range(3): # 행
    for j in range(4): # 열
      print(matrix[i][j], end=" ")
    print()

  >>> 1 2 3 4
  >>> 5 6 7 8
  >>> 9 0 1 2

2. 이중 for문을 이용한 열 우선 순회
  for i in range(4):
    for j in a range(3):
      print(matrix[j][i], end=" ")
    print()

  >>> 1 5 9
  >>> 2 6 0
  >>> 3 7 1
  >>> 4 8 2

# [참고] Pythonic한 방법으로 이차원 리스트의 총합 구하기
  matrix = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
  ]

  total = sum(map(sum, matrix))
  print(total)
  >>> 12

# 행 우선 순회를 이용해 이차원 리스트의 최대값, 최소값 구하기
  matrix = [
    [0, 5, 3, 1],
    [4, 6, 10, 8],
    [9, -1, 1, 5]
  ]

  value = 0

  for i in range(3):
    for j in range(4):
      if matrix[i][j] > value: # 최대값, < 최소값
        value = matrix[i][j]
  print(value)
  >>> 10 # 최대값
  >>> -1 # 최소값

# Pythonic한 방법으로 이차원 리스트의 최대값, 최소값 구하기
  max_value = max(map(max, matrix))
  min_value = min(map(min, matrix))
  >>> 10
  >>> -1 
```

## 📌 4. 전치
```python
# 전치(transpose)란 행렬의 행과 열을 서로 맞바꾸는 것을 의미한다.
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

transposed_matrix = [[0] * 3 for _ in range(4)]
# 전치 행렬을 담을 이차원 리스트 초기화(행과 열의 크기가 반대)

for i in range(4):
  for j in range(3):
    transposed_matrix[i][j] = matrix[j][i] # 행, 열 맞바꾸기

transposed_matrix = [
  [1, 5, 9],
  [2, 6, 0],
  [3, 7, 1],
  [4, 8, 2]
]
```

## 📌 5. 회전
```python
# 문제에서 이차원 리스트를 왼쪽, 오른쪽으로 90도 회전하는 경우가 존재한다.

# 원본
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

# 왼쪽 90도 회전
[
  [3, 6, 9],
  [2, 5, 8],
  [1, 4, 7]
]

# 오른쪽 90도 회전
[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
```

## 📌 
```python

```