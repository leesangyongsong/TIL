A, B = map(str, input().split())
A = int(A[::-1])
B = int(B[::-1])

if A > B:
  print(A)
elif A < B:
  print(B)
else:
  print(f'{A}와 {B}는 같다.')