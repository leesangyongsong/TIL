data = input()
search = input()

n = len(search)
cnt = 0
i = 0
while i < len(data)-n+1:
  if data[i:i+n] == search:
    cnt += 1
    i += n
  else:
    i += 1
print(cnt)