# 📚 Javascript

## 📌 Node.js의 특징
```javascript
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

## 📌 Javscript 더 알아보기
```javascript
1. javascript 자료형
  // 기본 자료형
  string: 문자열
  number: 숫자형
  boolean: true, false
  undefined: undefined
  null: 
  object: {}
  Array: []

  // 타입을 반환하는 함수로 반환 시
  function getType(date){
    return Object.prototype.toString.call(data).silce(8, -1)
  }

  console.log(getType(123)) // Nunmber
  console.log(getType(false)) // Boolean
  console.log(getType(null)) // Null
  console.log(getType({})) // Object
  console.log(getType([])) // Array

2. javascript 연산자
  □ 산술 연산자
  + 더하기 연산자
  - 빼기 연산자
  * 곱하기 연산자
  / 나누기 연산자
  % 나머지 연산자

  console.log(1 + 2) // 3
  console.log(5 - 7) // -2
  console.log(3 * 4) // 12
  console.log(10 / 2) // 5
  console.log(7 % 5) // 2

  // 할당 연산자
  const a = 2 // 재할당 불가능
  let a = 2 // 재할당 가능

  // 좌측과 // 우측 코드는 같은 내역
  a = a + 1 // a += 1 
  a = a - 1 // a -= 1
  a = a * 1 // a *= 1
  a = a / 1 // a /= 1
  a = a % 1 // a %= 1

  // 비교 연산자(comparison operator)
  □ 일치 연산자 ===

  case1)
  const a = 1
  const b = 1

  console.log(a === b) // true

  case2)
  const a = 1
  const b = 3

  console.log(a === b) // false

  function isEqual(x, y) {
    return x === y
  }

  console.log(isEqual(1, 1)) // true
  console.log(isEqual(1, '1')) // false 

  □ 불일치 연산자 !==
  const a = 1
  const b = 3

  console.log(a !== b) // true

  □ 크기 비교 연산자 <, >, <=, >=

  case1)
  const a = 1
  const b = 7

  console.log(a < b>) // true

  case2)
  const a = 13
  const b = 13

  console.log(a >= b) // true

  // 논리 연산자(logical operator)
  □ 그리고(and) 연산자 &&, 또는(or) 연산자 ||

  const a = 1 === 1
  const b = 'AB' === 'AB'
  const c = true

  console.log(a)
  console.log(b)
  console.log(c)

  console.log('&&: ', a && b && c) // &&: true
  console.log('||: ', a || b || c) // ||: true

  // 삼항 연산자(ternary operator)
  const a = 1 < 2

  if (a) {
    console.log('참')
  } else {
    console.log('거짓')
  }

  console.log(a ? '참' : '거짓') // 참

  // 조건문(If statement)
  import random from './getRandom'

  const a = random ()

  if (a === 0) {
    console.log('a is 0')
  } else if (a === 2) {
    console.log('a is 2')
  } else if (a === 4) {
    console.log('a is 4')
  } else {
    console.log('rest...')
  }

  // 조건문(Switch statement)
  const a = random ()

  switch (a) {
    case 0:
      console.log('a is 0')
      break
    case 2:
      console.log('a is 2')
      break
    case 4:
      console.log('a is 4')
      break
    default: 
      console.log('rest...')
  }

  // 반복문(For statement)
  // for(시작조건; 종료조건; 변화조건) {}

  for (let i = 0; i < 3; i += 1) {
    console.log(i)
  }
  // 0 1 2 console 출력

  const ulEl = document.querySelector('ul')

  for (let i = 0; i < 3; i += 1) {
    const li = document.createElement('li')
    li.textContent = 'list-${i + 1}'
    if(i % 2 === 0){
      li.addEventListener('click', function (){
        console.log(li.textContent)
      })
    }
    ulEl.appendChild(li)
  }

  // 변수 유효범위(Variable Scopr)
  // var, let, const
  function scope(){
    if(true){
      var a = 123
    }
    console.log(a)
  }
  scope()

  // 형 변환(Type conversion)
  const a = 1
  const b = '1'

  console.log(a == b) // == 동등 연산자

  // Truthy(참 같은 값)
  // true, {}, [], 1, 2, 'false', -12, '3.14' ...
  
  // Falsy(거짓 같은 값)
  // false, '', null, undefined, 0, -0, NaN

  if ('false'){
    console.log(123)
  }
```

## 📌 javascript 함수 
```javascript
1. 화살표 함수
  // () => {} vs function () {}
  // 일부 내용을 축약해서 편리하게 작성 가능한 함수

  const double = function(x){
    return x * 2
  }
  console.log('double: ', double(7))

  const doubleArrow = x => x * 2 
  // ({name : 'Heropy'})
  // 화살표 함수에서 {}는 ()로 감싸서 사용가능 
  console.log('doubleArrow', doubleArrow(7))

2. 즉시실행함수(IIFE, Immediately-Invoked Function Expression)
  const a = 7
  function double(){
    console.log(a * 2)
  }
  double();

  // 이렇게 작성하면 사용 가능
  (function () {
    console.log(a * 2)
  })();

  (function () {
    console.log(a * 2)
  }());

3. 호이스팅(Hoisting)
  // 함수 선언부가 유효범위 최상단으로 끌어올려지는 현상
  const a = 7
  
  double()

  function double(){
    console.log(a * 2)
  }

4. 타이머 함수
  // setTimeout(함수, 시간): 일정 시간 후 함수 실행
  // setInterval(함수, 시간): 시간 간격마다 함수 실행
  // clearTimeout(): 설정된 Timeout 함수를 종료
  // clearInterval(): 설정된 Interval 함수를 종료

  const timer = setTimeout(() => {
    console.log('Heropy!')
  }, 3000)

  const h1El = document.querySelector('h1')
  h1El.addEventListener('click', () => {
    clearTimeout(timer)
  })

5. 콜백(Callback)
  // 함수의 인수로 사용되는 함수
  // setTimeout(함수, 시간)

  function timeout(cb) {
    setTimeout(() => {
      console.log('Heropy!')
      cb()
    }, 3000)
  }
  timeout(() => {
    console.log('Done!')
  })

5. 생성자 함수
  // case1)
  const heropy = {
    firstName: 'Heropy',
    lastName: 'Park'
    getFullName: function () {
      return `${this.firstName} ${this.lastName}`
    }
  }
  console.log(heropy.getFullName())

  // case2)
  function user(first, last) {
    this.firstName = first
    this.lastName = last
  }
  user.prototype.getFullName = function () {
    return `${this.firstName} ${this.lastName}`
  }

  const heropy = new user('Heropy', 'Park')
  const amy = new user('Amy', 'Clarke')
  const neo = new user('Neo', 'Smith')

  // heropy, amy, neo는 인스턴스라고 함

6. this
  // 일반(Normal) 함수는 호출 위치에 따라 this 정의!
  // ghktkfvy(Arrow) 함수는 자신이 선언된 함수 범위에서 this 정의!

  const heropy = {
    name: 'Heropy',
    normal: function() {
      console.log(this.name)
    },
    arrow: () => {
      console.log(this.name)
    }
  }
  heropy.normal() // Heropy
  heropy.arrow() // undefinde

  const amy = {
    name: 'Amy',
    normal: heropy.normal,
    arrow: heropy.arrow
  }
  // amy.normal()
  // amy.arrow()

7. Math함수
  Math.abs() :  주어진 숫자의 절대값을 반환
  Math.min() : 주어진 숫자 중 가장 작은 수 반환
  Math.max() : 주어진 숫자 중 가장 큰 수 반환
  Math.ceil() : 주어진 숫자를 정수단위로 올림처리 // 3.14입력->4출력
  Math.floor() : 주어진 숫자를 정수단위로 내림처리 // 3.14 입력->3출력
  Math.round() : 주어진 숫자를 반올림or반내림 처리
  Math.random() : 무작위로 숫자 반환

8. javascript 배열 API
  const numbers = [1, 2, 3, 4]
  const fruits = ['Apple', 'Banana', 'Cherry']

  // Index
  console.log(numbers[1]) // 2
  console.log(fruits[2]) // Cherry

  // . length
  console.log(nubers.length) // 4
  console.log(fruits.length) // 3
  console.log([1, 2].length) // 2
  console.log([].length) // 0

  // .concat()
  console.log(numbers.concat(fruits))
  console.log(numbers)
  console.log(fruits)

  // .forEach()
  fruits.forEach(function (element, index, array){
    console.log(element, index, array)
  })

  // .map()
  const b = fruits.map(function (fruit, index) {
    return `${fruit}-${index}`
  })
  console.log(b)

  const b =fruits.map(function (fruit, index) {
    return {
      id: index,
      name: fruit
    }
  })
  console.log(b)

  const b = fruits.map((fruit, index) => ({
    id: index,
      name: fruit
  }))
  console.log(b)

  // .filter()
  const a = numbers.map(number => {
    return number < 3
  })
  console.log(a) // (4) [true, true, false, false]

  const b = numbers.filter(number => {
    return number < 3
  })
  console.log(b) // (2) [1, 2]

  // .find() .findIndex()
  const a = fruits.find(fruit => {
    return /^B/.test(fruit)
  })
  console.log(a) // Banana

  const b = fruits.findIndex(fruit => {
    return /^B/.test(fruit)
  })
  console.log(b) // 1

  // 정규표현식
  /^B/ -> B로 시작하는 지 확인

  // .includes()
  const a = numbers.includes(3)
  console.log(a) // true

  const b =fruits.includes('HEROPY')
  console.log(b) // false

  // .push() .unshift()
  // 원본 수정됨 주의!
  number.push(5)
  console.log(number) // [1, 2, 3, 4, 5]

  numbers.unshift(0)
  console.log(numbers) // [0, 1, 2, 3, 4, 5]

  // .reverse()
  // 원본 수정됨 주의!
  numbers.reverse()
  fruits.reverse()

  console.log(numbers) // [4, 3, 2, 1]
  console.log(fruits) // ["Cherry", "Banana", "Apple"]

  // .splice(a, b, c)
  // 원본 수정됨 주의!
  // 인덱스 번호 a에서 b만큼 요소를 지워라, 인덱스 번호 a에 c 추가
  numbers.splice(2, 0)
  console.log(numbers) // [1, 2, 3, 4]

  numbers.splice(2, 1)
  console.log(numbers) // [1, 2, 4]

  numbers.splice(2, 2)
  console.log(numbers) // [1, 2]

  numbers.splice(2, 0, 999)
  console.log(numbers) // [1, 2, 999, 3, 4]

  numbers.splice(2, 1, 99)
  console.log(numbers) // [1, 2, 99, 4]
```

## 📌 객체데이터
```javascript
1. 객체데이터
  // case1
  const userAge = {
    // key: value
    name: 'Heropy',
    age: 85
  }

  const userEmail = {
    name: 'Heropy',
    email: 'thesecon@gmail.com'
  }

  const target = Object.assign(userAge, userEmail)
  console.log(target)
  console.log(userAge)
  console.log(target === userAge) // true

  const a = { k: 123 }
  const b = { k: 123 }
  console.log(a === b) // false

  // case2
  const user = {
    name: 'Heropy',
    age: 85,
    email: 'thesecon@gmail.com'
  }

  const keys = Object.keys(user)
  console.log(keys) // ['name', 'age', 'email']

  console.log(user['email'])

  const values = keys.map(key => user[key])
  consoloe.log(values) // ["Heropy", "85", "thesecon@gmail.com"]

2. 구조 분해 할당(Destructuring assignment) == 비구조화 할당
  const user = {
    name: 'Heropy',
    age: 85,
    email: 'thesecon@gmail.com'
  }
  const { name, age, email. address } = user
  // E.g, user.address

  console.log(`사용자의 이름은 ${name}입니다.`)
  console.log(`${name}의 나이는 ${age}세입니다.`)
  console.log(`${name}의 이메일 주소는 ${email}입니다.`)
  console.log(address)

  const t fruits = ['Apple', 'Banana', 'Cherry']
  const [a, b, c, d] = fruits
  console.log(a, b, c, d)

3. 전개 연산자(Spread)
const fruits = ['Apple', 'Banana', 'Cherry']
console.log(fruits)
console.log(...fruits)
// consolee.log('Apple', 'Banana', 'Cherry')

function toObject(a, b, ...c) {
  return {
    a: a,
    b: b,
    c: c
  }
}
console.log(toObject(...fruits)) 

const toObject = (a,  b, ...c) => ({a, b, c})
console.log(toObject(...fruits)) 
```

## 📌 Javascript의 특성
```javascript
1. 데이터 불변성(Immutability)
  // 원시 데이터: String, Number, Boolean, undefined, null
  // 참조형 데이터: Object, Array, Function

  // case1)
  let a = 1
  let b = 4
  console.log(a, b, a === b) // 1 4 false
  b = a
  console.log(a, b, a === b) // 1 1 true
  a = 7
  console.log(a, b, a === b) // 7 1 false
  let c = 1
  console.log(b, c, b === c) // 1 1 true

  // case2)
  let a = { k: 1 }
  let b = { k: 1 }
  console.log(a, b, a ==== b) // {k:1}, {k:1}, false 
  a.k = 7
  b = a
  console.log(a, b, a === b) // {k:7}, {k:7}, true
  a.k 2
  console.log(a, b, a === b) // {k:2}, {k:2}, true
  let c = b
  console.log(a, b, c, a === c) // {k:2}, {k:2}, true
  a.k = 9
  console.log(a, b, c, a === c) // {k:9}, {k:9}, true

2. 복사
  // 얕은 복사(Shallow copy) : 표면만 복사
  // 깊은 복사(Deep copy) : 데이터 값 자체를 복사
  const user = {
    name: 'Heropy',
    age: 85,
    emails: ['thesecon@gmail.com']
  }
  const copyUser = Object.assign({}, user)
  console.log(copyUser === user)

  user.agee = 22
  console.log('user', user)
  console.log('copyUser', copyUser)

  console.log('------')
  console.log('------')

  user.emails.push('neo@zillinks.com')
  console.log(user.emails === copyUser.emails)
  // console.log('user', user)
  // console.log('copyUser', copyUser)


```

## 📌 
```javascript

```