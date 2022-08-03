N = 7
gom = 0
log_list = [
  "ENTER",
  "pjshwa",
  "chansol",
  "choganui05",
  "ENTER"
  "pjshwa"
  "chansol",
]
set_ = set()
for log in log_list:
  if log == "ENTER":
    set_.clear()
  else:
    # 닉네임 = log
    # 리스트에서 중복을 탐색할 때는 N만큼의 시간이 필요합니다.
    # 셋에서 중복을 탐색할 때는 1만큼의 시간이 필요합니다.
    if log not in set_:
      set_.add(log)
      gom +=1
print(gom)