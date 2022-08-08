# 9명의 키를 수직으로 입력받기
nanjaeng2 = [int(input()) for _ in range(9)]
sumList = sum(nanjaeng2)
 
# 7명 키의 합이 100이므로 불특정 2명을 제외했을 때 100이 되는 for문/if문 작성
for i in range(8):
  for j in range(i+1, 9):
    if sumList - (nanjaeng2[i] + nanjaeng2[j]) == 100:
      one = nanjaeng2[i]
      two = nanjaeng2[j]
      nanjaeng2.remove(one)
      nanjaeng2.remove(two)
      nanjaeng2.sort()
      for b in nanjaeng2:
        print(b)
    if len(nanjaeng2)<=8:
      break
  if len(nanjaeng2)<=8:
    break