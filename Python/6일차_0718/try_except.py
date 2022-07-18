# 숫자 입력을 받아서 출력
number = input('숫자를 입력해주세요:') # 자료 형태는 str
print(number)

try:
    if int(number) == 5:
        print('오오~')
    else:
        print('오가 아닙니다.')
except:
    print('숫자가 아닙니다.')