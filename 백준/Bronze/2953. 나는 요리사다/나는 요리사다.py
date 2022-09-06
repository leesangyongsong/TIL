a = sum(list(map(int, input().split())))
b = sum(list(map(int, input().split())))
c = sum(list(map(int, input().split())))
d = sum(list(map(int, input().split())))
e = sum(list(map(int, input().split())))
if max(a, b, c, d, e) == a:
  print(1, a)
elif max(a, b, c, d, e) == b:
  print(2, b)
elif max(a, b, c, d, e) == c:
  print(3, c)
elif max(a, b, c, d, e) == d:
  print(4, d)
else:
  print(5, e)