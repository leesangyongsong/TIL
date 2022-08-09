while True:
  sentence = input() # 모음 개수 확인할 문장 입력
  vowel_count = 0 # 모음 개수 받을 변수
  if sentence == '#':	# 입력 시 실행 종료
    break
  for c in sentence:
    if c in 'aeiouAEIOU': # 입력한 문장 중 모음이 있으면 vowel_count 1 up!
      vowel_count += 1
  print(vowel_count) # 총 모음 개수 출력