# 애너그램이란? 
# A, B 두 단어에서 A에 속하는 알파벳의 순서를 바꾸어서 B를 만들 수 있다면, 
# A와 B를 애너그램이라고 한다.

for i in range(int(input())):
  A, B = map(str, input().split())
  if sorted(list(A)) == sorted(list(B)):
    print(f'{A} & {B} are anagrams.')
  else:
    print(f'{A} & {B} are NOT anagrams.')
