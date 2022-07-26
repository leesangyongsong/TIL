a = [1, 2, 3]
b = a
b[0] = 'hi'

# a를 출력
print(a)
# b를 출력
print(b)

# 깊은 복사
aa = [[1, 2], 2, 3]
bb = list(aa)
bb[0][0] = 'hi'

print(aa)
print(bb)