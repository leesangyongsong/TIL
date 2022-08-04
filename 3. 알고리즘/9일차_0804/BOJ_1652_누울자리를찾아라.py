# 함수 생성
def Possible(li):
  result_count = 0
  # 입력받은 값을 통해 X가 없는 연속구간 확인하는 함수 작성
  for i in range(n):
    result = 0
    for j in range(n):
      # X를 만났을 때 연속구간이 2 이상이라면 가능여부 1 반환, 아니라면 0 반환
      if li[i][j] == 'X':
        if result >= 2:
          result_count += 1
        result = 0
      else:
        result += 1
    if result >=2: # 마지막 원소까지 확인 후 X가 없는 연속구간이 2이상이라면 1반환
      result_count += 1
  return result_count

n = int(input())
row = [list(input()) for _ in range(n)]
col = [[row[i][j] for i in range(n)] for j in range(n)]
print(Possible(row),Possible(col))