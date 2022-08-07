# 📚 Javascript

## 📌 Javascript 의 특징
```javascript
1. 표기법
  1. dash-case(kebab-case) : '-'를 사용하여 단어를 구분함
  2. snake_case : '_'를 사용하여 단어를 구분함
  3. camelCase : 두번째 단어부터 첫 알파벳을 대문자로 표기, "jsp"에서 주로 사용
  4. PascalCase : 첫번째 단어부터 첫 알파벳을 대문자로 표기, 생성자 함수에서 주로 사용

2. Zero-based Numbering
  : 0 기반 번호 매기기! 특수한 경우를 제외하고 0부터 숫자를 시작한다.

3. Javascript 예시
let fruits = ['Apple', 'Banana', 'Cherry'];

console.log(fruits[0]); // 'Apple'
console.log(fruits[1]); // 'Banana'
console.log(fruits[2]); // 'Cherry'

console.log(new Date('2021-01-30').getDay()); # 6, 토요일
console.log(new Date('2021-01-31').getDay()); # 0, 일요일
console.log(new Date('2021-02-01').getDay()); # 1, 월요일

4. 주석(comments)
// 한줄 메모
/* 한줄 메모*/
/**
 * 여러줄
 * 메모1
 * 메모2
 */
```

## 📌 데이터 종류(자료형)
```javascript
  1. String: 문자데이터
    - 따옴표를 사용한다.

    let myName = "HEROPY";
    let email = 'thesecon@gmail.com';
    let hello = `Hello #{myName}?!` 
    // 보관법: 백틱(`)을 사용해서 변수를 할당한다.

    console.log(myName); # HEROPY
    console.log(email); # thesecon@gmail.com
    console.log(hello); # Hello #{myName}?!

  2. Number: 숫자데이터
    - 정수 및 부동소수점 숫자를 나타낸다.

    let number = 123; 
    let opacity = 1.57;

    console.log(number); //123
    console.log(opacity); //1.57

  3. Boolean: 불린 데이터
    - true, false 두 가지 값밖에 없는 논리 데이터입니다.

    let checked = true;
    let isShow = false;

    console.log(checked); //true
    console.log(isShow); // false

  4. Undefined
    - 값이 할당되지 않은 상태를 나타냅니다.

    let undef;
    let obj = { abc: 123 };

    console.log(undef); //undefined
    console.log(obj.abc); // 123
    console.log(obj.xyz); // undefined

  5. Null
    - 어떤 값이 '의도적'으로 비어있음을 의미합니다.

    let empty = null;

    console.log(empty); // null

  6. Object: 객체 데이터
    - 여러 데이터를 Key:Value 형태로 저장합니다. {}

    let user = {
      // key: value,
      name: 'HEROPY',
      age: 85,
      isValid: true
    };

    console.log(user.name); // HEROPY
    console.log(user.age); // 85
    console.log(user.isValid); // true

  7. Array: 배열 데이터
    - 여러 데이터를 순차적으로 지정합니다. []
    
    let fruits = ['Apple', 'Banana', 'Cherry'];

    console.log(fruits[0]); // 'Apple'
    console.log(fruits[1]); // 'Banana'
    console.log(fruits[2]); // 'Cherry'
```

## 📌 변수와 예약어
```javascript
  1. 변수란? 
  : 데이터를 저장하고 참조(사용)하는 데이터의 이름
    ex) let, const

    case)1
    // 재사용이 가능!
    // 변수 선언!
    let a = 2;
    let b = 5;

    console.log(a + b); // 7
    console.log(a - b); // -3
    console.log(a * b); // 10
    console.log(a / b); // 0.4

    case)2
    // 값(데이터)의 재할당 가능!
    let a =12;
    console.log(a); // 12

    a = 999;
    console.log(a); // 999

    case)3
    // 값(데이터)의 재할당 불가!
    const a =12; 
    console.log(a); // 12

    a = 999;
    console.log(a); // TypeError: Assignment to constant variable.

    => let은 재할당이 가능하고 const는 재할당이 불가능하다.

  2. 예약어란? 
  : '특별한 의미'를 가지고 있어, 변수나 함수 이름 등으로 사용할 수 없는 단어

    let this = 'Hello!'; // SyntaxError
    let if = 123; // SyntaxError
    let break = true; // SyntaxError
```

## 📌 함수
```javascript
함수란?
: 특정 동작(기능)을 수행하는 일부 코드의 집합(부분)

  ex)
  // 함수 선언
  function helloFunc(){
    // 실행 코드
    console.log(1234);
  }

  // 함수 호출
  helloFunc()
```

```javascript
  case)1
  function returnFunc(){
    return 123;
  }

  let a = returnFunc();
  console.log(a); // 123

  case)2
  // 함수 선언
  function sum(a, b) { // a와 b는 매개변수(Parameters))
    retrun a + b;
  }

  // 재사용!
  let a = sum(1, 2); // 1과 2는 인수(Arguments)
  let b = sum(7, 12);
  let c = sum(2, 4);

  console.log(a, b, c); // 3, 19, 6

  case)3
  // 기명(이름이 있는) 함수
  // 함수 선언!
  function hello(){
    console.log('Hello~');
  }

  // 익명(이름이 없는) 함수
  // 함수 표현!
  let world = function(){
    console.log('World~');
  }

  // 함수 호출!
  hello(); // Hello~
  world(); // World~

  case)4
  // 객체 데이터
  const heropy = {
    name: 'HEEROPY',
    age: 82,
    // 메소드(Method)
    getName: function(){
      reeturn this.name;
    }
  };

  const hisName = heropy.getName();
  console.log(hisName); // HEROPY
  // 혹은
  console.log(heropy.getName()); // HEROPY
```

## 📌 조건문
```javascript
조건문이란?
: 조건의 결과(truthy, falsy)에 ㄸ다라 다른 코드를 실행하는 구문

  ex)
  if, else

  case)1
  let isShow = true;
  let checked = false;

  if(isShow){
    console.log('Show!'); //Show! 위쪽에서 실행되면 밑에 조건문은 실행x!
  }

  if(checked){
    console.log('Checked!');
  }

  case)2
  let isShow = true;

  if(isShow){
    console.log('Show!');
  }else{
    console.log('Hide?');
  }
```

## 📌 DOM API
```javascript
DOM API(Document Object Model, Application Programming Interface)
: 의역하자면 javascript에서 HTML을 제어하는 명령들

  // HTML 요소(Element) 1개 검색/찾기
  const boxEl = document.querySelectior('.box');

  // HTML 요소에 적용할 수 있는 메소드!
  boxEl.addEventListener();

  // 인수(Arguments)를 추가 가능!
  boxEl.addEventListener(1, 2);

  // 1- 이벤트(Event, 상황)
  boxEl.addEventListener('click', 2);

  // 2- 핸들러(Handler, 실행할 함수)
  boxEl.addEventListener('click', function(){
    console.log('Click~!');
  });

  // 요소의 클래스 정보 객체 활용!
  boxEl.classList.add('active');
  let isContains = boxEl.classList.contains('active');
  console.log(isContatins); // true

  boxEl.classList.remove('active');
  isContains = boxEl.classList.contains('active');
  console.log(isContatins); // false
```

```javascript
  // HTML 요소(Element) 모두 검색/찾기
  const boxEls = document.querySelectorAll('.box');
  console.log(boxEls);

  // 찾은 요소들 반복해서 함수 실행!
  // 익명 함수를 인수로 추가
  boxEls.forEach(function() {});

  // 첫 번째 매개변수(boxEl): 반복 중인 요소
  // 두 번째 매개변수(index): 반복 중인 번호
  boxEls.forEach(function(boxEl, index){});

  // 출력!
  boxEls.forEach(function(boxEl, index){
    boxEl.classList.add(`order-${index + 1}`);
    console.log(index, boxEls);
  });
```

```javascript
  const boxEl = document.querySelection('.box');

  // Getter, 값을 얻는 용도
  console.log(boxEl.textContent); // Box!!

  // Setter, 값을 지정하는 용도
  boxEl.textContent = 'HEROPY?!';
  console.log(boxEl.textContent); // HEROPY?!
```

## 📌 메소드 체이닝
```javascript
메소드체이닝
: 메소드들을 연결하여 사용하는 것

  const a = 'Hello~';
  const b = a.split('').reverse().join(''); // 메소드 체이닝...
  // split: 문자를 인수 기준으로 쪼개서 배열로 반환
  // reverse: 배열 뒤집기
  // join: 배열을 인수 기준으로 문자로 병합해 반환

  console.log(a); // Hello~
  console.log(b); // ~olleH
```

## 📌 질의응답
```javascript
Q1. 'The quick brown fox' 문장을 camelCase(낙타 표기법)로 작성하시오!
A1. theQuickBrownFox

Q2. let fruits = ['Apple', 'Banana', 'Cherry']; 
    위 데이터를 활용해 'Banana'를 콘솔 출력하시오!
A2. console.log(fruits[1]);

Q3. 불린데이터(Boolean)에서 '거짓'을 의미하는 데이터는?
A3. False

Q4. '값이 의도적으로 비어있음'을 의미하는 데이터는?
A4. null

Q5. {} 해당 데이터의 종류는?
A5. Object(객체 데이터)

Q6. 아래 코드를 통해 콘솔 출력될 값(데이터)은?
  let obj = { abc:123 };
  console.log(obj.xyz);
A6. undefined

Q7. 값(데이터)을 재할당할수 없는 변수 선언 '키워드'는?
A7. const

Q8. 함수에서 값(데이터)을 반환하기 위해 사용하는 키워드는?
A8. return

Q9. sum(2, 4); 해당 함수 호출에서 2, 4를 무엇이라 하는가?
A9. 인수(Arguments)

Q10. 아래 함수 선언의 a, b와 같이, 함수 호출에서 전달받은 인수를
    함수 내부로 전달하기 위한 변수를 무엇이라 하는가?
    function sum(a, b){
      return a+b;
    }
A10. 매개변수(Parameters)

Q11. '이름이 없는 함수'를 무엇이라 하는가?
A11. 익명함수(Anonymous Function)

Q12. hello 이름의 함수 표현을 작성하고 호출하시오!
A12. 
  const hello = function(){};
  hello();

Q13. 아래 코드의 getName과 같이, 함수가 할당된 객체 데이터의 속성을 무엇이라 하는가?
  const user = {
    getNamee: function(){}
  }
A13. 메소드(Method)

Q14. 조건이 참(true)인 조건문을 작성하시오!
A14. if(true){}

Q15. 가져온 JS파일을 HTML 문서 분석 이후에 실행하도록 지시하는 HTML속성은?
A15. 'defer'

Q16. 아래 HTML 요소의 내용을 콘솔 출력하시오!
  <div clasee="box">BOX!!</div>
A16.
  const boxEl = document.querySelector('.box');
  console.log(boxEl.textContent);

Q17. 값(데이터)을 재할당할 목적의 변수 선언 '키워드'는?
A17. let

Q18. 아래 코드의 boxEl 요소에 클릭(click) 이벤트를 추가해, 
    클릭시 'Hello~'를 콘솔 출력하시오
  const boxEl = document.querySelector('.box');
A18.
  boxEl.addEventListener('click', function(){
    console.log('Hello~');
  });

Q19. 아래 2개의 DIV요소에 JS로 class="hrllo"를 추가하시오!
  <div>1</div>
  <div>2</div>
A19.
  const divEls = document.querySeletorAll('div');
  divEls.forEach(function(divEl){
    divEl.classList.add('hello');
  });

Q20. 아래와 같이, '메소드를 이어 작성하는 방법'을 무엇이라 하는가?
  'HEROPY'.split('').reverse().join('');
A20. 메소드 체이닝

Q21. 아래 코드의 boxEl 요소에 HTML 클래스 속성의 값으로 'active'가 포함되어 있으면,
    '포함됨!'을 콘솔 출력하시오!
  const boxEl = document.querySelector('.box');
A21.
  if(boxEl.classList.contains('active')){
    console.log('포함됨!');
  }
```

## 📌 Node.js의 특징
```python
# Node.js
  Node.js는 Chrome V8 JavaScript 엔진으로 빌드된 
  JavaScript 런타임(프로그래밍 언어가 동작하는 환경!)

  - JS는 웹브라우저 및 컴퓨터에서 작용 가능하다.
    단, 웹브라우저에서는 HTML, CSS, JS만 사용 가능하여 
    개발에 제한이 생기고 비효율적이다.

    => 이를 Node.js를 통해 컴퓨터를 제어해 개발을 효율적으로 운영한다!

# NPM(생태계라고도 함)
  NPM(Node Package Manager)은 
  전 세계의 개발자들이 만든 다양한 기능(패키지, 모듈)들을 관리

  Trade-off 발생!
  - 학습 난이도 증가
  - 구성 복잡
  vs
  + 관리 효율 증가
  + 손쉬운 기능 고도화 
```
