# 월이 입력될 때 계절 이름이 출력되도록 해보자.
# 월 : 계절 이름
# 12, 1, 2 : winter
# 3, 4, 5 : spring
# 6, 7, 8 : summer
# 9, 10, 11 : fall

a = int(input())
if a == 1 or a == 2 or a == 12:
  print('winter')
elif a == 3 or a == 4 or a == 5:
  print('spring')
elif a == 6 or a == 7 or a == 8:
  print('summber')
elif a == 9 or a == 10 or a == 11:
  print('fall')
else:
  print('해당 월은 존재하지 않습니다.')

# 인터넷 풀이
# a=int(input())
# if a//3==1:
#     print("spring")
# elif a//3==2:
#     print("summer")
# elif a//3==3:
#     print("fall")
# else:
#     print("winter")