# 📚 CSS(Cascading Style Sheets)

## 📌CSS의 속성(Properties)
```python
 박스모델: HTML 요소들은 기본적으로 사각형 모양을 가짐
 글꼴, 문자: font 설정 및 글씨 크기, 두께 조절 가능
 배경: 배경 색상 또는 이미지 삽입 가능
 배치: HTML 요소들을 원하는 위치에 배치 가능
 플렉스(정렬): HTML은 기본적으로 수직방향으로 요소가 정렬되는데 
              플렉스를 사용하면 수평방향으로 요소 정렬이 가능
 전환: 요소의 전상태와 후상태가 있을 경우 애니메이션 처리가 가능
 변환: 요소를 회전, 이동, 크기 조절 등 변환을 줄 수 있음, 
      2D 변환 - 요소 원근법을 주면서 전, 3D 변환도 존재
 띄움: 요소를 띄우게 되면 해당 요소 주변으로 문자를 흐르게 할 수 있음
 애니메이션: 훨씬 더 복잡하고 다양한 애니메이션 기능을 조작할 수 있음
 그리드: 행과 열의 구조를 가지고 있는 2차원의 레이아웃 기술
 다단: 신문, 뉴스기사 등 글자들이 많을 경우 하나의 페이지에서 단을 여러개로 나눌 수 있음
 필터: 요소를 blur. Grayscale, Reverse 등 다양하게 변화할 수 있음
```
<br>

| 박스모델 | 내역 |
| --- | --- |
| width | 요소의 가로 너비, auto 기본값이 들어 있어 브라우저가 자동으로 너비를 계산 |
| height | 요소의 세로 너비, x, em, vw등 단위로 지정 |
| max/min-width | 요소가 커질 수 있는 최대/최소 가로 너비 | 
| max/min-height | 요소가 커질 수 있는 최대/최소 세로 너비 |
| margin | 요소의 외부 여백(공간)을 지정하는 단축 속성, 상하좌우로 각각 여백을 추가할 수 있음 |
| padding | 요소의 내부 여백(공간)을 지정하는 단축 속성, 상하좌우로 각각 여백을 추가할 수 있음 |
| border | 요소의 테두리 선을 지정하는 단축 속성, 두께/종류/색상 순으로 추가할 수 있음 |
| border-radius | 요소의 모서리를 둥글게 깍음 |
| box-sizing | content-box: 요소의 내용(content)으로 크기 계산 <br> border-box: 요소의 내용 + padding + border로 크기 계산 |
| overflow | 요소의 크기 이상으로 내용이 넘쳤을 때, 보여짐을 제어하는 단축 속성 |
| display | 요소의 화면 출력(보여짐) 특성 <br> flex: 1차원 레이아웃, grid: 2차원 레이아웃, none: 보여짐 특성 없음, 화면에서 사라짐 |
| opacity | 요소의 투명도 조정 |

<br>

| CSS단위 | 내역 |
| --- | --- |
| px |  픽셀 |
| % | 상대적 백분율 |
| em | 요소의 글꼴 크기 |
| rem | 루트 요소(html)의 글꼴 크기 |
|vw | 뷰포트 가로 너비의 백분율 |
| vh | 뷰포트 세로 너비의 백분율 |

> Q. opx vs ovw 중 더 큰 값은? <br>
> A. 둘 다 0 이므로 같은 값이다. 

<br>

| 글씨 | 내역 |
| --- | --- |
| font-style | 글자의 기울기 |
| font-weight | 글자의 두께(가중치) |
| font-size | 글자의 크기 |
| font-family | 글꼴(서체) 지정 |
| line-height | 한 줄의 높이, 행간과 유사 |
| color | 글자의 색상 지정 |
| text-align | 문자의 정렬 방식 |
| text-decoration | 문자의 장식(선) |
| text-indent | 문자 첫 줄의 들여쓰기, 음수로 내어쓰기 할 수 있음 |

| 배경 | 내역 |
| --- | --- |
| background-color | 요소의 영역만큼 색상 삽입 |
| background-image | 요소의 배경 이미지 삽입 | 
| background-repeat | 요소의 배경 이미지 반복 |
| background-position | 요소의 배경 이미지 위치 |
| background-size | 요소의 배경 이미지 크기 |
| background-attachment | 요소의 배경 이미지 스크롤 특성 |

<br>

|위치|내역|
| --- | --- |
| position| 요소의 위치 지정 기준 <br> relative: 요소 자신을 기준 <br> absolute: 위치 상 부모 요소를 기준 <br> fixed: 뷰포트(브라우저)를 기준 <br> position속성의 값이 absolute, fixed로 지정된 요소는 display 속성이 block으로 변경됨|
| z-index | 요소의 쌓임 정도를 지정, 숫자가 높을수록 위에 쌓임 |

<br>

| 플렉스(정렬) | 내역 |
| --- | --- |
| display | flex : 블록 요소와 같이 Flex Container 정의 <br> inline-flex : 인라인 요소와 같이 Flex Container 정의 |
| flex-direction | 주 축을 설정 <br> row : 행 축 (좌 => 우) <br> row-reverse 행 축(우 => 좌) <br> column : 열 축(위 => 아래) <br> column-reverse : 열 축(아래=>위) |
| flex-wrap | flex items 묶음(줄 바꿈) 여부 <br> nowrap : 묶음(줄 바꿈) 없음, 기본값 <br> wrap : 여러 줄로 묶음 |
| justify-content | 주 축의 정렬 방법 <br> flex-start: flex items를 시작점으로 정렬, 기본값 <br> flex-end: flex items를 끝점으로 정렬 <br> center: flex items를 가운데 정렬 |
| align-content | 교차 축의 여러 줄 정렬 방법 <br> stretch: flex items를 시작점으로 정렬 <br> flex-start: flex items를 시작점으로 정렬 <br> flex-end: flex items를 끝점으로 정렬 <br> center: flex items를 가운데 정렬 |
| align-items | 교차 축의 한 줄 정렬 방법 |
| flex-grow | flex item의 증가 너비 비율, 숫자로 증가 비율을 설정 |
| flex-shrink | flex item의 감소 너비 비율, Flex Containeer 너비에 따라 감소 비율 적용, 숫자로 감소 비율 설정 |
| flex-basis | flex item의 공간 배분 전 기본 너비, px/em/rem 등 단위로 너비 지정 |

<br>

| 전환, 변환효과 | 내역 |
| --- | --- |
| transition | 요소의 전환(시작과 끝) 효과를 지정하는 단축 속성 <br> transition-property: 전환 효과를 사용할 속성 이름을 지정 <br>  transition-duration: 전환 효과의 지속시간을 지정 <br> transition-timing-function: 전환효과의 타이밍(Easing) 함수를 지정 <br> transition-delay: 전환 효과가 몇초 뒤에 시작할지 대기시간을 지정
| transform | 요소에 변환효과를 주는 속성 |
| transform<br>-2D변환함수 | translate(x,y): 이동(x축,y축) <br> translate(X): 이동(x축) <br> translate(Y): 이동(y축) <br> scale(x, y): 크기(x축, y축) <br> rotate(degree): 회적(각도) <br> skewX(x): 기울임(x축) <br> skewY(y): 기울임(y축) |
| transform<br>-3D변환함수 | translateZ(z): 이동(z축) <br> translate3d(x,y,z): 이동(x축,y축,z축) <br> rotateX(x): 회전(x축) <br> rotateY(y): 회전(y축) <br> perspective(n): 하위 요소를 관찰하는 원근 거리를 지정 |
| backface-visibility | 3D변환으로 회전된 요소의 뒷면 숨김 여부 |








## 📌 
```python

```

## 📌
```python

```

## 📌
```python

```