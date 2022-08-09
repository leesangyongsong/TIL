import sys

input=sys.stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_score = 0
B_score = 0

for i in range(10):
  # 비길 경우
  if A[i] == B[i]:
    A_score += 1
    B_score += 1
  
  # A가 이길 경우
  elif A[i] > B[i]:
    A_score += 3

  # B가 이길 경우
  elif A[i] < B[i]:
    B_score += 3

# A스코어가 더 높을 경우
if A_score > B_score:
  print(A_score, B_score)
  print("A")

# B스코어가 더 높을 경우
elif A_score < B_score:
  print(A_score, B_score)
  print("B")

# A, B스코어가 같을 경우
else: 
  if A_score[-1] > B_score[-1]:
    print(A_score, B_score)
    print("A")
  
  elif A_score[-1] < B_score[-1]:
    print(A_score, B_score)
    print("B")

  else:
    print(A_score, B_score)
    print("D")
  