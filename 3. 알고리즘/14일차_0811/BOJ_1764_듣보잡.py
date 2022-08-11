N , M = map(int,input().split()) # 두 인수를 받고
no_listen = set() # 들어본 적 없는 사람들의 집합
no_see = set() # 본 적 없는 사람들의 집합

for _ in range(N): # 들어본적 없는 사람들 집합에 N명 추가
  no_listen.add(input())
for _ in range(M): # 본적 없는 사람들 집합에 M명 추가
  no_see.add(input())

no_listen_see = sorted(list(no_listen & no_see)) # 듣도보도못한(교집합) 생성 -> 리스트 인입 -> ABC순 정렬
print(len(no_listen_see)) # 인원 수 출력

for i in no_listen_see: # 명단 출력
  print(i)