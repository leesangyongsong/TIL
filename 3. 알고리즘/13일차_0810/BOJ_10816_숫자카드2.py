cards = [int(input().split()) for i in range(int(input()))]
check_card = [int(input().split()) for i in range(int(input()))]

for k in check_card:
  print(check_card[k].count(cards), sep=" ")
