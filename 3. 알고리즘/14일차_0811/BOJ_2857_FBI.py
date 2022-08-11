li = [] 
for i in range(1, 6): 
  agent_name = input() 
  if "FBI" in agent_name: 
    li.append(i) # 요원명에 FBI 있을 경우 리스트에 해당 요원 순서 추가
if li: 
  print(*li) # *(asterisk)로 리스트 언패킹하여 출력 
else: 
  print("HE GOT AWAY!") # FBI 요원 없을 경우