import sys
input = sys.stdin.readline

N = int(input())
Name = {}
for _ in range(N):
  name, Log = map(str, input().split())

  if Log == 'enter':
    Name[name] = 'enter'

  else:
    del Name[name]

result = sorted(Name.keys(), reverse = True)

for i in result:
  print(i)