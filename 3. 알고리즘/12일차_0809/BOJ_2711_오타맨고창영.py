for _ in range(int(input())):
  n, word = input().split()
  n = int(n)
  print(word[:n-1], word[n:], sep='')
