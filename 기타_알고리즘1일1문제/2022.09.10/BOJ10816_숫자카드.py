## 시간초과라니...
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
number = list(map(int, input().split()))

for i in range(len(number)):
  print(cards.count(number[i]), end=" ")

