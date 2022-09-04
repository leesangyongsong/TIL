# 최소, 최대값 메서드 활용
N = int(input())
A = list(map(int, input().split()))
print(min(A), max(A))

# 정렬로 풀기
N = int(input())
A = list(map(int, input().split()))
A.sort()
print(A[0], A[-1])