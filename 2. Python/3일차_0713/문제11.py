# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

for dan in range(2, 10):
    print(dan, '단')
    for n in range(1, 10):
        print(dan, 'x', n, '=', dan*n)