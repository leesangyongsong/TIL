import sys
input = sys.stdin.readline

n = int(input())
card_dic = {}

for i in range(n) :
  card = int(input())
  if card in card_dic :
    card_dic[card] += 1
  else :
    card_dic[card] = 1

result = sorted(card_dic.items(),key = lambda x : (-x[1],x[0]))
print(result[0][0])

# 딕셔너리를 사용한 이유는 key값에 카드의 번호를 저장하고, 
# value값에 카드의 개수를 저장하여 마지막에 value값을 내림차순해주고 
# 같다면 key값을 오름차순해주기 위해서이다.