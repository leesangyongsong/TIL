title = 0
i = 666
N = int(input())
while 1 :
  if '666' in str(i): # i의 스트링을 검사해서 666이 있을 경우
    title += 1 # 타이틀에 1을 ㄷ더해줌
  if len(title) == N: # 원하는 시리즈까지 왔을 경우 브레이크
    print(1)
    break
  i += 1