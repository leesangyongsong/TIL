# 첫째 줄에 손님의 수 N, 둘째 줄에 손님이 들어오는 순서대로 앉고 싶은 자리 순서 말하고 비어있으면 착석, 사용중이면 거절
# 첫째 줄에 거절당하는 사람의 수 출력

n = int(input())  # 손님의 수
client = list(map(int, input().split()))  # 손님이 앉고 싶어하는 자리
rejected_people = 0  # 거절당하는 사람의 수
seat = []  # 피시방 자리

for i in range(n):
  # 앉고 싶어하는 자리에 사람이 있으면 거절당하는 인원 수 카운트
  if client[i] in seat:         
    rejected_people += 1 
  # 빈자리일 경우 착석
  else:                           
    seat.append(client[i])   
print(rejected_people)
