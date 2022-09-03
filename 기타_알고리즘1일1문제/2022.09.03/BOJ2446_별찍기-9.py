n = int(input())
for i in range(1, n+1):
  print(' ' * (i-1) + '*' * ((2 * (n+1-i))-1)   + ' ' * (i-1))

for i in range(2, n+1):
  print(' ' * (n-i) + '*' * ((2 * i)-1))

## 인터넷 풀이
n = int(input())
for i in range(n):
  print(" " * i + "*" * ((n - i) * 2 - 1))
for i in range(n - 2, -1, -1):
  print(" " * i + "*" * ((n - i) * 2 - 1))