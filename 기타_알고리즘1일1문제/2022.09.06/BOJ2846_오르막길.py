### 솔루션
#1 첫째 줄에 수열의 크기 N 입력
#2 N만큼 숫자 입력
#3 연속적인 오르막길일 경우 오르막의 크기 계산, 구간 내 가장 큰 오르막길 출력 
#4 오르막길이 없는 경우 0 출력



n = int(input()) #1
li = list(map(int, input().split())) #2
a = 0
section = []
for i in range(n-1): #3
    if li[i] < li[i+1]:
        a += li[i+1] - li[i]
    else: #4
        section.append(a)
        a = 0
section.append(a)
print(max(section))