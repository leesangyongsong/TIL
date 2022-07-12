# 미세먼지 농도에 따른 등급 알려주기
dust = int(input())
if dust > 150 :
    if dust > 300 :
        print('야외 활동을 자제하세요!')
    print('미세먼지 매우 나쁨')
elif dust > 80 :
    print('미세먼지 나쁨')
elif dust > 30 :
    print('미세먼지 보통')
elif dust > 0 :
    print('미세먼지 좋음')
else :
    print('값이 잘못되었습니다.')
   
# else는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건 불가능
# 조건문에서 else는 생략 가능