# 📚 React & Redux

## 📌 React 알아보기
```javascript
1. as 라이브러리
  // 라이브러리 vs 프레임워크
  라이브러리(공구) : 개발 편의를 위한 도구의 모음 
  프레임워크(공장) : 기반 구조까지 잡혀 있음

2. 생태계(구글링)
  해당 기술에 대한 관심도/실제 사용 빈도/사용자 수

  관련 라이브러리(도구)가 많고,
  문제를 해결할 방법을 찾기가 쉽고(like.stackoverflow),
  나와 같은 고민을 하는/했던 사람이 많다.
  실무에서 사용할 확률이 높다.

3. 기술적 근간
  많은 사람들에게 사랑받고 있다면 !== 기술적 근간이 좋다.

  하지만 리액트는 기술적으로 '확실한 장점'이 있다.
  Vitual DOM/JSX/Flux/Functional Programming

  새로운 기술을 배우는 '시작점'으로 좋다.

4. with 라이브러리
  생태계가 성숙해가면서 고민의 깊이 또한 '성숙'해졌다.
  리액트를 풍성하게 해주는 라이브러리들이 많고,
  '새로운, 좋은' 라이브러리들이 계속 나오고 있다.
  (swr, framer motion 등등)
```

## 📌 강의 소개
```javascript
// 강의를 통해 얻어갈 수 있는 것들
1. 프로그래밍의 흥미
2. 탄탄한 기초
3. 새로운 것을 익힘
4. 혼자 할 수 있는 힘

// 트렌드
  기술의 트렌드는 '빠르게' 변한다. 
  프론트엔드가 각광받기 시작한지 '그리 오래되지 않았다.'
  그렇기 때문에 '새로운 기술'을 빠르게 익히는 능력이 중요하다.

  처음에는 어려운 게 당연하다. 하지만 이 또한 '반복'하면 된다.
  리액트를 라이브러리로서 접근, 약 20여개의 다양한 라이브러리들을 
  '반복' 접근, '공식문서'를 토대로 익힌다.(만든 이의 사용 설명서)
  그 안의 '패턴'을 찾고, 새로운 기술을 '익히는 요령'을 습득

  - 리액트 맛보기(간단한 예제, 직접 따라 치기)
  - 리액트 공식문서를 통해 '중심'을 잡기
  - 다양한 '라이브러리'를 접하기
```

## 📌 DOM 다루기/ Element 생성하기
```javascript
1. DOM(Document Object Model)
  문서를 '논리 트리'로 표현한다.

  '순수' 자바스크립트
  : 특정 라이브러리나 프레임워크를 사용하지 않은 그 자체의 자바스크립트

  CodeSandBox
  : 프론트엔드 코드를 작성하고 이것저것 시돋해볼 수 있는 
  모래상자(놀이도구) React 등 다양한 환경에 대한 기본 설정이 되어있음

  CDN(Content Delivery Network)
  : 웹에서 사용되는 다양한 컨텐츠(리소스)를 저장하여 제공하는 시스템

  DOM 다루기 / Element 생성하기 정리
  CodSandBox -> 리액트 맛보기 동안 사용할 도구
  Vanilla js Dom -> W3Schools / createElement
  CDN -> unpkg
  React / React-dom -> element 생성 / appendChild
```

## 📌 JSX / Babel 다루기 외 기능 알아보기
```javascript
  JSX: 문자도 HTML도 아닌 Javascript의 '확장 문법'
    const element = <h1>Hello, world!</h1>

  JavaScript Complier
  컴파일러
  : 언어 해석기, 특정 언어를 다른 프로그래밍 언어로 옮기는 프로그램

  JSX -> React.createElement 표현식
  Babel -> JavaScript Complier
  JSX 다루기 -> spread 연산자
  Fragment -> React.Fragment or <></>

  // element 찍어내기
  Function -> 재사용 가능한 Element
  Custom Element -> Upper case
  Children 제한 -> 없음

  // JS와 JSX 섞어쓰기
  Interpolation -> 이미 HTML에서 쓰고 있었다.
```

## 📌 프론트엔드 개발의 장점
```javascript
  눈에 직접적으로 보인다.
  눈으로 '바로 확인'할 수 있다.
  google / MDN / console
```

## 📌 리액트와 리랜더링 알아보기
```javascript
  바닐라 JS -> 변경으로 인해 Element를 다시 그림
  React -> 변경된 부분만 다시 그림

  React 앨리먼트는 불변객체(immutable)입니다.
  불변객체? 변하지 않는 객체
  우리는 그저 ReactDOM.render(element, rootElement);로 전달할뿐
  변경 판단 및 반영은 리액트가 알아서 한다.

  앨리먼트 타입이 바뀌면?
  이전 앨리먼트는 버리고 새로 그린다.
  앨리먼트 타입이 같다면?
  key를 먼저 비교하고, props를 비교해서 변경사항을 반영한다.

  리액트의 앨리먼트 -> 불변객체
  변경사항 반영 -> 리액트에게 일임
  리액트의 비교 -> Reconciliation
  Virtual Dom -> 비교시 활용
```

## 📌 이벤트 핸들러
```javascript
1. 이벤트 핸들러 만들어보기
//addEventListener
  on{event} onclick onmouseout onfocus onblur

// 간단한 검색창 만들어보기
  // 구성
  input / button
  onChangee / onClick

  + 전역 변수

  // 코드 작성
  const rootElement = document.getElementById("root");

  const state = { keyword: "", typing: false, result: "" };

  const App = () => {
    function handleChange(event) {
      setState( { typing: true, keyword: event.target.value });
    }

    function handleClick() {
      setState({
        typing: false,
        result: `We find results of ${state.keyword}`
      });
    }

    return (
      <>
        <input onChange={handleChange}/>
        <button>search</button>
        <p>
          {state.typing ? `Looking for {state.keyword}...` : state.result}
        </p>
      </>
    );
  };

  function setState(newState) {
    Object.assign(state, newState);
    render();
  }

  function render() {
    ReactDOM.render(<App />, rootElement);
  }

  render();

  // 변수 선언 방법
  기본 문장 on click
  카멜 케이스 onClick
  파스칼 케이스 OnClick
  케밥 케이스 on-click
  스네이크 케이스 on_click
```

## 📌 컴포넌트
```javascript
DOM: 논리 트리
컴포넌트: '앨리먼트의 집합'
앨리먼트: 요소
```

## 📌 Redux
```javascript
1. Redux 개요
  1) 단일 스토어를 만드는 법
  2) 리액트에서 스토어 사용하는 법을 익히는 시간

    - 단일 스토어다!
    - [만들기] 단일 스토어 사용 준비하기
      - import redux
      - 액션을 정의하고,
      - 액션을 사용하는, 리듀서를 만들고,
      - 리듀서들을 합친다.
      - 최종 합쳐진 리듀서를 인자로, 단일 스토어를 만든다.
    - [사용하기]준비한 스토어를 리액트 컴포넌트에서 사용하기
      - import react-redux
      - connect 함수를 이용해서 컴포넌트에 연결

2. Action - 액션
  리덕스의 액션이란?
  - 액션은 사실 그냥 객체(object)입니다.
  - 두 가지 형태의 액션이 있습니다.
    - {type:'test'} // payload 없는 액션
    - {type:'test', params:'hello'} // payload 있는 액션
    - type만이 필수 프로퍼티이며, type은 문자열입니다.
  
  리덕스의 액션은 어떤일을 하나요?
  - 액션 생성자를 통해 액션을 만들어 냅니다.
  - 만들어낸 액션 객체를 리덕스 스토어에 보냅니다.
  - 리덕스 스토어가 액션 객체를 받으면 스토어의 
    상태 값이 변경됩니다.
  - 변경된 상태 값에 의해 상태를 이용하고 있는 
    컴포넌트가 변경됩니다.
  - 액션은 스토어에 보내는 일종의 인풋이라고 볼 수 있다.

  액션을 준비하기 위해서는?
  - 액션의 타입을 정의하여 변수로 빼는 단계
    - 강제는 아님
    - 타입을 문자열로 넣기에는 실수 유발 가능성이 큼
    - 미리 정의한 변수 사용 시, 스펠링에 덜 주의해도됌
  - 액션 객체를 만들어 내는 함수를 만드는 단계
    - 하나의 액션 객체를 만들기 위해 하나의 함수를생성
    - 액션타입은 미리 정의한 타입 변수를 가져와서 사용

3. Reducers - 리듀서
  리덕스의 리듀서란?
  - 액션을 주면, 그 액션이 적용되어 달라진
    (안달라질 수도 있음) 결과를 만들어 줌
  - 그냥 함수
    - Pure Function
    - Immutable
      - 리듀서를 통해 스테이트가 달려졌음을 
        리덕스가 인지하는 방식
  
  function 리듀서(previousState, action) {
    return newState;
  }
  - 액션을 받아서 스테이트를 리턴하는 구조
  - 인자로 들어오는 previousState와 
    리턴되는 newState는 다른 참조를 가지도록 해야 함.

4. createStore
  스토어를 만드는 함수
  const store = createStore(리듀서);
    createStore<S>(
      reducer:Reducer<S>
      preloadedState: S,
      engancer?:StoreEnhancer<S>
    ):Store<S>;

5. combineReducers

6. Redux를 React에 연결


```

## 📌 
```javascript

```

## 📌 
```javascript

```