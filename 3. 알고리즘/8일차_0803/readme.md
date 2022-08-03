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

## 📌 
```python

```