result = []
for _ in range(3):
  s = input()
  length = 1
  li = []
  for i in range(1, 8):
    if s[i] == s[i - 1]:
      length += 1
    else:
      li.append(length)
      length = 1
  li.append(length)
  result.append(max(li))
print(*result, sep='\n')