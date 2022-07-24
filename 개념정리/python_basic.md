# 📚 Jump to 'PYTHON'

## 📌 1. 파이썬 시작하기

    ```
    - '귀도 반 로섬'이 취미로 만든 프로그래밍 언어
      - 1991년 최초 발표
      - 2000년 python 2, 2008년 python 3 version-upgrade
    - 구글에서 만들어진 소프트웨어의 50% 이상이 파이썬
    - 드롭박스(Dropbox), 인스타그램(Instagram) 등
    - 이해하기 쉬워 공동 작업과 유지 보수가 편하다.
    ```
### 1-1. 파이썬의 특징

1) 파이썬은 인간다운 언어이다
    ```python
    if 4 in [1,2,3,4]: print("4가 있습니다") 
    => 만약 4가 [] 안에 있으면 ("4가 있습니다")를 출력해라
    ````
2) 파이썬은 문법이 쉬워 빠르게 배울 수 있다
    ```
    - 대학교 교양 강의로 파이썬 활용
    - 프로그래밍 유 경험자라면 1주일이면 충분
    ```
3) 파이썬은 무료지만 강력하다
    ```
    - 사용료 걱정없이 언제 어디서든 파이썬을 다운로드하여 사용
    - 파이썬과 C는 찰떡궁합(접착언어)
      - 파이썬은 쉬운데 느리고, C는 빠른데 복잡함
      - 상대적으로 쉽지만 느린 파이썬 + 빠른 C언어 조합 가능
    - 파이썬 라이브러리들 중에는 C로 만들어진 것도 많다.
      - NumPy: C라이브러리를 python에서 쓸 수 있도록 래핑
    ```
4) 파이썬은 간결하다.
    ```python
    # simple.py
    languages = ['python', 'perl', 'c', 'java']
    for lang in languages:
      if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
      elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
      else:
        print("should not reach here")

    - 파이썬은 가장 좋은 방법 1가지만 이용하는 것을 선호
    - 실행이 되게 하려면 꼭 줄을 맞추어야 한다.(다른 언어에 비해 엄격한 면이 있음)
    ```
5) 파이썬은 개발 속도가 빠르다
    ```
    - "Life is too short, You neeed python."

### 1-2. 파이썬으로 무엇을 할 수 있을까?
```
- 파이썬으로 할 수 있는 일   
  - 시스템 유틸리티 제작 ex) 고클린 등의 시스템 청소 도구
  - GUI(graphical user interface) 프로그래밍
  : 사용자가 편리하게 사용할 수 있도록 기능을 그래픽으로 나타낸 것
  - C/C++와의 결합
  - 웹 프로그래밍 ex) django, flask
  - 수치 연산 프로그래밍 ex) SQL
  - 데이터베이스 프로그래밍
  - 데이터 분석, 사물 인터넷(IOT) 
  IOT: 각종 사물에 센서와 통신 기능을 내장하여 인터넷에 연결하는 기술

- 파이썬으로 할 수 없는 일
  - 시스템과 밀접한 프로그래밍 영역 ex) OS - Window, Linux
  - 모바일 프로그래밍 ex) App 제작
```

### 1-3. 파이썬 설치하기
```
- 파이썬 언어 패키지를 다운로드한다.
- 파이썬이 어느 곳에서든지 실행될 수 있도록 "Add Python 3.8 to PATH" 옵션을 선택한다.
```

## 📌 2. 자료구조
| 자료에 대한 타입 | 어떤 값을 담는 자료구조 |
| --- | ----|
| 숫자, 문자열, 불 | 변수, 리스트, 튜플, 딕셔너리, 집합 |

> 리스트 : 변수 여러 개를 묶는 역할

### 2-1. 숫자형
  ```python
- 정수형(int)
- 실수형(float)
- 컴퓨터식 지수 표현 방식
- 8진수
- 16진수
  ```

### 2-2. 문자형
  ```python
  str 로 표시되며, "" or '' 둘 다 표시 가능

  - Indexing
  - Slicing [이상:미만:간격] # 간격은 생략가능
  ```

문자열 함수
| 함수명 | 기능 |
| ---- | ----- |
| count | 문자열 개수 세기 |
| find | 문자열 위치 알려주기 |
| join | 문자열 삽입 |
| upper | 소문자 -> 대문자 변경 |
| lower | 대문자 -> 소문자 변경 |
| strip | 양쪽 공백 지우기
| replace | 문자열 바꾸기 |
| split | 문자열 나누기 |

### 2-3. 리스트 자료형

리스트 함수
| 리스트 함수명 | 기능 |
| --- | --- |
| append | 리스트 맨 뒤에 요소 추가 |
| sort | 리스트 정렬 : 문자는 ㄱㄴㄷ순, 숫자는 크기 순|
| reverse | 리스트 순서 뒤집기 |
| index | 위치 반환 |
| insert | 리스트 특정 위치에 요소 추가 |
| remove | 리스트 내 요소 제거 |
| pop | 리스트 내 마지막 요소 제거 |
| extend | 리스트 확장 |

### 2-4. 튜플형 자료형
```python
리스트와 유사하나 차이점이 있음.

- 리스트는 [대괄호], 튜플은 (소괄호) 사용
- 리스트는 내역 변경이 가능하나, 튜플은 불가능(단, 인덱싱 및 슬라이싱은 가능)
```

### 2-5. 딕셔너리 자료형📝 (중요!)
``` python
- 연관 배열(Associative array) 또는 해시(Hash)
- 단어 그대로 해석하면 사전이라는 뜻
- Key를 통해 Value를 얻는다

>>>  a = {
          'name': 'pey',
          'phone': '0119993323',
          'birth': '1118'
          }

◆ 딕셔너리 쌍 추가하기
>>> a = {1: 'a'}
>>> a[2] = 'b'
>>> a
{2: 'b', 1: 'a'}

◆ 딕셔너리 요소 삭제하기
>>> a = {1: 'a'}
>>> a['name'] = "익명"
>>> del a[1]
>>> a
{'name': '익명'}

◆ 딕셔너리에서 key 사용해 value 얻기
>>> grade = {'pey': 10, 'julliet': 99}
>>> grade['pey']
10
>>> grade['julliet']
99

◆ 딕셔너리 만들 때 주의할 사항
>>> a = {1: 'a', 1: 'b'}
>>> a
{1: 'b'} 
# 같은 키가 중복될 경우 마지막에 매칭된 key와 value값으로 인식된다. 
# 딕셔너리는 key값으로 인식하기 때문에 key값을 '반드시' 다르게 해야 한다. 
# (여러 key 값에 같은 value는 가능)

◆ Key 리스트 만들기(keys)
>>> a = {
        'name': 'pey',
        'phone': '0119993323',
        'birth': '1118'
        }
>>> a.keys()
dict_keys(['name', 'phone', 'birth'])

◆ Value 리스트 만들기(values)
dict_values(['pey', '0119993323', '1118'])

◆ Key, Value 쌍 얻기(튜플 형태)
dict_itmes([('name': 'pey'), ('phone': '0119993323'), ('birth': '1118')])

◆ Key, Value 쌍 모두 지우기(clear)
>>> a.clear()
>>> a
{} # 빈 딕셔너리가 됌

◆ 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
>>> a = {
        'name': 'pey',
        'phone': '0119993323',
        'birth': '1118'
        }
>>> 'name' in a
True
>>> 'email' in a
False
```

### 2-6. 집합 자료형
```python
집합의 핵심: 
- 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형(파이썬에만 有)
- 중복을 허용하지 않는다.
- 순서가 없다(unordered)

◆ 집합 자료형
>>> s1 = set([1, 2, 3])
>>> print(s1)
{1, 2, 3}
# list를 set으로 감싸면 집합으로 변환

>>> 1 = [1,2,2,3,3]
>>> newList = list(set(1))
>>> print(newList)
[1, 2, 3]
# set으로 중복값을 없앤 후 다시 리스트로 변환

>>> s1 = set('Hello')
>>> print(s1)
{'o', 'l', 'e', 'H'}

◆ 교집합
>>> s1 = set([1, 2, 3, 4, 5, 6])
>>> s2 = set([4, 5, 6, 7, 8, 9])
>>> print(s1 & s2) or print(s1.intersection(s2)) # 교집합 구하기
{4, 5, 6}

◆ 합집합
>>> s1 = set([1, 2, 3, 4, 5, 6])
>>> s2 = set([4, 5, 6, 7, 8, 9])
>>> print(s1 | s2) or print(s1.union(s2)) # 합집합 구하기
{1, 2, 3, 4, 5, 6, 7, 8, 9}

◆ 차집합
>>> s1 = set([1, 2, 3, 4, 5, 6])
>>> s2 = set([4, 5, 6, 7, 8, 9])
>>> print(s1 - s2) or print(s1.difference(s2)) # 차집합 구하기
{1, 2, 3}

◆ 값 추가하기
>>> s1 = set([1, 2, 3])
>>> s1.add(4) # 값 1개 추가하기 add
>>> print(s1)
{1, 2, 3, 4}

>>> s1 = set([1, 2, 3])
>>> s1.update([4, 5, 6]) # 값 여러 개 추가하기 update
>>> print(s1)
{1, 2, 3, 4, 5, 6}

◆ 값 제거하기
>>> s1 = set([1, 2, 3])
>>> s1.remove(2) # 값 제거하기 remove
>>> print(s1)
{1, 3}
```

### 2-7. 불리언 자료형(불)
| 구분 | 값 | 참 or 거짓 |
| --- | -- | ----- | 
| 문자열_str | "python" | 참 |
| 문자열_str | " " | 거짓 |
| 리스트_list | [1, 2, 3] | 참 |
| 리스트_list | [] | 거짓 |
| 튜플_tuple | () | 거짓 |
| 딕셔너라_dictionary | {} | 거짓 |
| 숫자열 | 1(그 외 1 이상의 수) | 참 |
| 숫자열 | 0 | 거짓 |
| 불 | None | 거짓

### 2-8. 변수
```python
변수: 자료형의 값을 저장하는 공간

파이썬에서 사용하는 변수는 객체를 가리키는 것
>>> a = 3

- 3이라는 값을 가지는 정수 자료형(객체)이 자동으로 메모리에 생성
- 변수 a는 객체가 저장된 메모리의 위치를 가리키는 레퍼런스(Reference)
- a라는 변수는 3이라는 정수형 객체를 가리키고 있다

# 변수의 활용 : case1
>>> a = [1, 2, 3]
>>> b = a
>>> a[1] = 4 # b가 a의 주소를 가져오는 것이기 때문에 a의 리스트 내역이 바뀌면 b도 같이 변경된다!
>>> print(a)
>>> print(b)
[1, 4, 3] # a의 리스트
[1, 4, 3] # b의 리스트

# 변수의 활용 : case2
>>> a = [1, 2, 3]
>>> b = a[:] # a를 슬라이싱한 값을 b에 넣어 새로운 값을 얻음
>>> a[1] = 4 
>>> print(a)
>>> print(b)
[1, 4, 3] # a의 리스트
[1, 2, 3] # b의 리스트
```

## 📌 3. 제어문
| 구분 | 내역 |
| ---- | ---- |
| 조건문 | ~하면 ~해라 |
| 반복문 | ~하는 동안 ~ 해라 |


### 3-1. 조건문
```python
돈이 있으면 택시를 타고, 돈이 없으면 걸어간다!
>>> money = True
>>> if money:
      print("택시를 타고 간다")
    else:
      print("걸어간다!")
```

### 3-2. 반복문
| 구분 | 내역 |
| ---- | ---- |
| for문 | 순회할 때 (문자열/리스트 등) + 횟수를 알 때(range) |
| while문 | 조건에 도달할 때까지(while True + break) |

```python
나무를 10번 찍는다
>>> treeHit = 0
>>> while treeHit <=1:
      treeHit += 1
      print("나무를 &d번 찍었습니다" % count)
      if treeHit == 10:
      print("나무가 쓰러졌습니다.")
```

### 3-3. 이중반복문
```python
구구단 만들어보기
>>> for i in range(2, 10):
      print(f"{i}단")
      for j in range(1, 10):
        print(f"{i} '*' {j} '=' '{i * j}' ")

구구단 리스트에 넣기
>>> result = []
    for x in range(2,10):
      for y in range(1, 10):
        result.append(x * y)

# 한줄로 표현하면?
>>> result = [x * y for x in ragnge(2, 10) for y in range(1, 10)]
```

## 📌 4. 함수
### 4-1. 파이썬 함수의 구조
```python

def 함수명(매개변수):
  <수항핼 문장1>
  <수항핼 문장2>
  ...
  return 리턴 값

ex)
>>> def sum(a, b):
      result = a + b
      retrun result
    print(sum(1,2))
3

# 함수의 결과값은 항상 하나!
>>> def sum_and_mul(a,b):
      return a+b, a*b # 리턴 값이 두개일 때는
    print(sum_and_mul(1,2))
(3, 2) #tuple 형태로 1개의 결과값 출력

# 매개 변수에 초기값 미리 설정하기
>>> def say_myself(name, old, man=True): # 초기값을 미리 설장한다면?
      print("나의 이름은 %s 입니다." % name)
      print("나이는 %d 입니다." % old)
      if man:
        print("남자입니다.")
      else:
        print("여자입니다.")
    say_myself("라이유튜브", 20) # 함수 사용시 별도로 인자가 없어도 실행! 

# 함수 안에서 선언된 변수의 효력 범위
>>> a = 1
    def vartest(a):
      a = a + 1
    vartest(a)
    print(a)
1 # return 값이 없으면 함수는 외부 변수에 영향을 줄 수 없음

# Lambda 함수: 함수를 간단하게 표현하는 방법
>>> add = lambda a, b : a+b
    result = add(3,4)
    print(3, 4)
7

# 아래와 완전히 동일
>>> def add(a, b):
      return a + b
```

### 4-2. 사용자 입력과 출력
```python
# input의 사용, input: 입력을 받는 내장함수
>>> a = input()
Life is too short, you need python
>>> print(a)
'Life is too short, you need python'

# print문
>>> print("life" "is" "too short")
lifeistoo short
>>> print("life"+"is"+"too short")
lifeistoo short
>>> print("life", "is", "too short")
life is too short
>>> for i in range(10):
      print(i, end=' ')
0 1 2 3 4 5 6 7 8 9
```

### 4-3. 파일 읽고 쓰기
| 파일열기모드 | 설명 |
| --- | --- |
| r | 읽기모드 - 파일을 읽기만 할 때 사용 |
| w | 쓰기모드 - 파일에 내용을 쓸 때 사용 |
| a | 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용 |

```python
# 파일 생성하기
f = open("새파일.txt", "w") 
# 상대경로: 현재 실행하는 파일을 기준으로 상대적인 경로를 써주는 것
f.close()

# 파일을 쓰기 모드로 열어 출력값 적기
f = open("C:/Python/새파일.txt", 'w', encoding="UTF-8") 
# 절대경로: 처음부분(C:/)부터 주소를 써주는 것
for i in range(1, 11):
  data = "%d번째 줄입니다.\n" % i
  f.write(data)
f.close()

# 파일 읽기
readline(): 한줄 읽는 것
readlines(): 리스트 형태로 가져와서 출력
read(): 통째로 가져오는 것

# 파일 추가/수정
f.write()

# close를  안하는 방법
with open("foo.txt", "w") as f:
  f.write("Life is too short, you need python")
```

```python
# Immutable(변하지 않는 자료형 : 정수, 실수, 문자열, 튜플)
a = 1
def vartest(a):
  a = a + 1
vartest(a)
print(a)

# Mutable(변할 수 있는 자료형 : 리스트, 딕셔너리, 집합)
b = [1, 2, 3]
def vartest2(b):
  b = b.append(4)
vartest2(b)
print(b)
```

## 📌 5. 파이썬 날개 달기
### 5-1. 클래스
```python
# 클래스란?
클래스: 반복되는 변수 & 메서드(함수)를 미리 정해놓은 틀(설계도), 파이썬 프로그래밍의 핵심
클래스는 도대체 왜 필요한가? 
-> 같은 내역의 함수를 여러번 사용하고자 할 때 유용!

# 클래스를 쓰는 방법!
# 1. Class를 입력하고 
# 2. 대무낮로 시작하는 클래스의 이름을 작성 
# 3. 안에 들어갈 함수와 변수 설정

class FourCal:
  def __init__(self, first, second): # init은 생성자기 때문에 1번만 사용하면 됌
    self.first = first
    self.second = second
  def setdata(self, first, second):
    self.first = first
    self.second = second
  def add(self):
    result = self.first + self.second
    return result

a = FourCal(1, 2)

# 클래스의 상속
class FourCal: # 부모 클래스
  def __init__(self, first, second): 
    self.first = first
    self.second = second
  def setdata(self, first, second):
    self.first = first
    self.second = second
  def add(self):
    result = self.first + self.second
    return result
  def mul(self):
    result = self.first * self.second
    return result
  def sub(self):
    result = self.first - self.second
    return result
  def div(self):
    result = self.first / self.second
    return result

class SafeFourCal(FourCal): # 자식 클래스
  def div(self): 
    if self.second == 0:
      return 0
    else:
      return self.first / self.second
a = SafeFourCal(4, 0)
print(a.div())
2.0
# 메서드 오버라이딩 
# : 부모 클래스와 자식 클래스에 같은 메서드가 있을 때 자식 클래스에 있는 메서드로 작동됌
```

### 5-2. 모듈
```python
# 모듈이란?
모듈 : 미리 만들어놓은 파이썬 파일(함수, 변수, 클래스 등)
import mod1 # mod1.py 파일 생성 후 연결하여 사용 ex) 부트스트랩(css라이브러리)
print(mod1.add(1, 2))
3

from mod1 import add # mod1 파일에서 add만 가져오겠다 -> mod1 전부를 가져올 때보다 속도 up!

# import하려는 파일이 같은 폴더에 없을 경우 추가적으로 경로를 적어줘야 한다.
import sys
sys.path.append("C:\\jocoding\\subFolder")
import mod1
print(mod1.add(3,4))
```

### 5-3. 패키지
```python
# 패키지란?
패키지: 모듈 여러 개를 모아놓은 것 # 라이브러리와 비슷
game/
  __init__.py # 패키지 관련 설정하는 곳
  sound/
    __init__.py
    echo.py
  graphic/
    __init__.py
    render.py

# 패키지 안의 함수 실행하기
import game.sound.echo
game.sound.echo.echo_test() # 정석적인 루트 접근 후 echo_test() 사용하겠다

from game.sound import echo
echo.echo_test() # game.sound 파일 내 echo만 연결하여 사용하겠다

from game.sound import *
echo.echo_test() # game.sound 파일 내 모든 내역을 불러와라

# Relative 패키지
from ..sound.echo import echo_test
def render_test():
  print("render")
  echo_test()
```

### 5-4. 예외처리
```python
# 예외처리란?
예외처리: 오류가 발생했을 때 어떻게 할지 정하는 것
try:
  # 오류가 발생할 수 있는 구문
except Exception as e:
  # 오류 발생
else:
  # 오류 발생하지 않음
finally:
  # 무조건 마지막에 실행  
```

### 5-5. 내장함수
```python
# 내장함수란?
내장함수: 파이썬에서 기본적으로 포함하고 있는 함수
```
| 함수명 | 기능 |
| ---- | ---- |
| print() | 확인, 출력하기 |
| type() | 변수의 자료형 확인하기 |
| abs() | 변수의 절대값 확인하기 |
| all() | 포함하고 있는 변수가 모두 참인지 검사하기 |
| any() | 하나라도 참이 있는지 검사하기 |
| chr() | ASCII(아스키 코드) 코드를 입력 받아 문자 출력하기 |
| dir() | 자체적으로 가지고 있는 변수나 함수를 보여준다 |
| divmod() | 몫과 나머지를 튜플 형태로 돌려준다 |
| enumerate() | 리스트를 딕셔너리처럼 활용할 수 있다 |
| eval() | 실행 후 결과값을 돌려준다 |
| filter() | 함수를 통과하여 참인 것만 돌려준다 |
| id() | 변수의 주소 값 확인하기 |
| input() | 사용자가 입력한 값을 받는다 |
| int() | 변수를 10진수의 정수 형태로 변환한다 |
| len() | 변수의 길이를 확인한다 |
| list() | 변수를 리스트로 변환한다 |
| map() | 각 요소가 수행한 결과를 돌려준다 |
| max() | 최대값을 확인한다 |
| min() | 최소값을 확인한다 | 
| pow() | 제곱한 결과값을 반환한다 |
| range() | 범위를 설정한다 |
| round() | 변수를 반올림한다 |
| sorted() | 문자는 abc/가나다 순으로, 숫자는 작은 수부터 정렬한다 |
| str() | 변수를 문자열로 반환한다 |
| tuple() | 변수를 튜플로 변환한다 |
| zip() | 자료형을 묶어준다 |
```python 
# ASCII(아스키코드)= 0 ~ 127사이의 숫자를 각 문자에 대응
```

### 5-6. 외장함수
```python
# 외장함수란?
외장함수: 라이브러리 함수, import 해서 쓰는 것
- sys.argv
- pickle
- time
- time.sleep
- random
- webbrowser
```

## 📌 6. 파이썬 프로그래밍, 어떻게 시작해야 할까?
```python
Point! 프로그램을 만들려면 가장 먼저 '입력'과 '출력'을 고려해서 단계적으로 작성해야 한다!

# 구구단 만들기
def GuGu(n):
  result = []
  i = 1
  while < 10:
    result.append(n*i)
  return result
print(GuGu(2))
[2, 4, 6, 8, 10, 12, 14, 16, 18]

# 1000 이하의 자연수 중 3과 5의 배수 합하기
result = 0
for n in range(1,1000):
  if n % 3 == 0 or n % 5 == 0:
    result += n
print(result)
233168

# 게시판 페이징하기
def getTotalPage(m, n): # m : 게시물의 총 건수, n: 페이지당 보여줄 게시물 수
  if m % n == 0:
    return m // n
  else:
    return m // n + 1
print(getTotalPage)

# 간단한 메모장 만들기
import sys
option = sys.argv[1]

if option == '-a':
  memo = sys.argv[2]
  f = open('memo.txt','a')
  f.write(memo)
  f.write('\n')
  f.close()
elif option == '-v':
  f = open('memo.txt')
  memo = f.read()
  f.close()
  print(memo)

# 탭을 4개의 공백으로 바꾸기
import sys
src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_conteent = tab_content.replace("\t"," "*4)
print(space_content)

f = open(dst, 'w')
f.write(space_content)
f.close()

# 하위 디렉터리 검색하기
import os
def search(dirname):
  try:
  filenames = os.listdir(dirname)
  for filename in filenames:
    full_filename = os.path.join(dirname, filename)
    if os.path.isdir(full_filename):
      search(full_filename)
    else:
      ext = os.path.splitxt(full_filename)[-1]
      if ext == ".py":
        print(full_filename)
  except PermissionError:
    pass

search("C:/")
```

## 📌 7. 정규 표현식
### 7-1. 정규표현식 알아보기
```python
# 정규표현식이란?
정규표현식: 복잡한 문자열을 처리할 때 사용하는 기법, 모든 언어 공통

  정규표현식은 문자열에 관련된 복잡한 문제를 해결해야 될 때,
  정규 표현식을 사용하게 되면 짧고 간결하게 문제를 해결할 수 있게 해준다.

# 문자 클래스 []
[abc]
■ [] 사이의 문자들과 매치
■ "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
■ "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
■ "dude"는 정규식과 일치하는 문자인 a, b, c 중 어느 하나도 포함하고 있지 않으므로 매치되지 않음
■ 하이픈을 사용하여 From-To로 표현 가능
  ■ Ex) [a-c] = [abc], [0-5] = [012345]

# Dot(.)
a.b
■ 줄바꿈(\n)을 제외한 모든 문자와 매치
■ "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 `.`와 일치하므로 정규식과 매치
■ "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 `.`와 일치하므로 정규식과 매치
■ "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는 있어야 하는 이 정규식과 
  일치하지 않으므로 매치되지 않는다.

# 반복(*)
ca*t
■ "ct"는 "a"가 0번 반복되어 매치
■ "cat"는 "a"가 0번 이상 반복되어 매치(1번 반복)
■ "caaat"는 "a"가 0번 이상 반복되어 매치(3번 반복)

# 반복(+)
ca+t
■ "ct"는 "a"가 0번 반복되어 매치되지 않음
■ "cat"는 "a"가 0번 이상 반복되어 매치(1번 반복)
■ "caaat"는 "a"가 0번 이상 반복되어 매치(3번 반복)

# 반복({m, n},?)
ca{2}t
■ "cat"는 "a"가 1번만 반복되어 매치되지 않음
■ "caat"는 "a"가 2번 반복되어 매치

ca{2,5}t
■ "cat"는 "a"가 1번만 반복되어 매치되지 않음
■ "caat"는 "a"가 2번 반복되어 매치
■ "caaaaat"는 "a"가 5번 반복되어 매치

ab?c # ? == {0,1}와 같은 표현
■ "abc"는 "b"가 1번 사용되어 매치
■ "ac"는 "b"가 0번 사용되어 매치
```
### 7-2. 정규표현식 시작하기
```python
# 파이썬에서 정규 표현식을 지원하는 re모듈
import re
p = re.compile('ab*')

# match
import re
p = re.compile('[a-z]+')
m = p.match('3 python')
print(m)

> 매치 성공 시 : <re.Match object; span=(0, 6), match='python'>
> 매치 실패 시 : None

# search
import re
p = re.compile('[a-z]+')
m = p.search('3 python')
print(m)

> 서치 성공 시 : <re.Match object; span=(2, 8), match='python'>
> 서치 실패 시 : None

# findall
import re
p = re.compile('[a-z]+')
m = p.findall('life is too short')
print(m)
> ['life', 'is', 'too', 'short']

# finditer
import re
p = re.compile('[a-z]+')
m = p.finditer('life is too short')
print(m)
> <callable_iterator object at 0x025f50b8>
```