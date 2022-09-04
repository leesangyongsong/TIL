A, B, C = map(int, input().split())

# 3개가 동일할 경우
if A == B == C:
  print(10000 + A * 1000)

# 2개가 동일할 경우
elif A == B or A == C:
  print(1000 + A * 100)
elif B == C:
  print(1000 + B * 100)

# 3개 모두 다를 경우
elif A != B != C: #(else로 대체 가능)
  print(max(A, B, C) * 100)