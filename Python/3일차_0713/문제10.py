# 문제 10. 5의 개수 구하기
# 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.
count = 0
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
for i in numbers:
    if i == int(5):
        count += 1
print(count)