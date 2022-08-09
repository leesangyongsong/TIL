point_spot = int(input()) # 점의 개수 입력
q1, q2, q3, q4, axis = 0, 0, 0, 0, 0 # 사분면 및 축 변수 할당
for i in range(point_spot): # 좌표 입력하여 사분면 확인
  x,y = map(int,input().split())
  if x > 0 and y > 0 :
    q1 += 1
  elif x < 0 and y < 0 :
    q3 += 1
  elif x < 0 and y > 0 : 
    q2 += 1
  elif x > 0 and y < 0 :
    q4 += 1
  else :
    axis += 1 
print(f"Q1: {q1}\nQ2: {q2}\nQ3: {q3}\nQ4: {q4}\nAXIS: {axis}") 
# 사분면 및 축에 위치한 개수 출력