# 출력은 되는데 백준은 틀렸다고 나와서 궁금...
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a_score = 0
b_score = 0

for i in range(10):
  if A[i] > B[i]:
    a_score += 3
  elif A[i] < B[i]:
    b_score += 3
  elif A[i] == B[i]:
    a_score += 1
    b_score += 1

if a_score > b_score:
  print(a_score, b_score)
  print('A')
elif A == B:
  print(a_score, b_score)
  print('D')
elif a_score <= b_score:
  print(a_score, b_score)
  print('B')

# 다른 풀이 1

A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A == B:
  print(10, 10); 
  print("D")
else:
  a = b = 0
  for i in range(10):
    if A[i] > B[i]:
      a += 3; win = 'A'
    elif A[i] < B[i]:
      b += 3; win = 'B'
    else:
      a += 1; b += 1;    
  print(a, b)
  if a == b:
    print(win)
  else:
    print('A' if a > b else 'B')