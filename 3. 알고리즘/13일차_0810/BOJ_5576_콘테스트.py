# 대학별로 점수를 10개씩 받아서 리스트에 저장
w_college = [int(input()) for i in range(10)]
k_college = [int(input()) for j in range(10)]

# 정렬
w_college.sort()
k_college.sort()

# 대학별 최고득점자 3명 합산 점수 출력
print(sum(w_college[7:10]), sum(k_college[7:10]))

####
# 코드 간략화
W = sorted([int(input())for i in range(10)])
K = sorted([int(input())for j in range(10)])
print(sum(w_college[7:10]), sum(k_college[7:10]))