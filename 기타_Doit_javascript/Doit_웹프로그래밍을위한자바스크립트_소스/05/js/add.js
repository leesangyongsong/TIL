var num1 = parseInt(prompt("첫 번째 숫자는?"));
var num2 = parseInt(prompt("두 번째 숫자는?"));
// 값 2개와 함께 함수 실행
addNumber(num1, num2); 

// 매개변수 a, b가 있는 함수 선언
function addNumber(a, b) { 
  var sum = a + b;
  alert('두 수를 더한 값은' + sum + '입니다.');
}

// 1. 프롬프트 창에서 사용자에게 입력값을 받아 변수 num1, num2에 저장합니다.
// 2. num1과 num2 값을 가지고 addNumber()함수를 호출합니다.
// 3. 함수 선언부로 넘어옵니다. 넘겨주는 값도 두 개이고, addNumber() 함수의 매개변수도 두개이므로 정상적으로 함수를 실행합니다. 나열된 순서대로 num1 값은 매개변수 a로, num2 값은 매개변수 b로 넘겨줍니다.
// 4. 매개변수에 들어온 인수 값을 사용해 함수 안의 명령을 실행합니다. a값과 b값을 더해 sum 변수에 저장한 후 알림 창에 sum 값을 표시합니다.
