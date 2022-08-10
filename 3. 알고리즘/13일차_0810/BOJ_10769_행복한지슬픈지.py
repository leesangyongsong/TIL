# 문자 입력
sentence = input()

# 경우마다 문구 다르게 출력 
if sentence.count(":-)") > sentence.count(":-("):
  print('happy')
elif sentence.count(":-)") < sentence.count(":-("):
  print('sad')
# 해당 경우가 가장 밑에 있는 경우보다 먼저 작성되어야 완성
elif sentence.count(":-)") == sentence.count(":-(") == 0:
  print('none')
elif sentence.count(":-)") == sentence.count(":-("):
  print('unsure')