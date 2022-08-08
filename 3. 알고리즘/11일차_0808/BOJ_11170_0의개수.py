for _ in range(int(input())):
  zero_count = 0
  n, m = map(int, input().split())
  for i in range(n, m+1):
    zero_count += str(i).count('0')
  print(zero_count)