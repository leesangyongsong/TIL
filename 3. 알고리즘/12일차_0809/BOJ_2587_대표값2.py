numbers = [int(input()) for i in range(5)] # 5개의 수 줄바꾸면서 입력하기
numbers.sort() # 입력된 수 정렬

print(sum(numbers)/5) # 평균값 정수 출력
print(numbers[2]) # 가운데 수 출력