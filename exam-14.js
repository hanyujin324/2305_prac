/* 자바스크립트가 선언형으로 지원하는 Number.isInteger() 함수, 정수인지 판단하는 내장 메서드를 절차형으로 표현한 예제입니다.
해당 부분에 대한 작성을 python으로는 어떻게 처리할 수 있는지 정보를 얻어보시기 바랍니다. */
function exampleOne(a){
  if(typeof a==='number'){
    if(a-Math.floor(a)!==0){ //a-소수점 버린a가 0이 아니라면 ex)a가 3.5일경우 
      throw new Error('정수를 입력해야 합니다');
    }
  }else{ //a가 숫자가 아닐 경우
    throw new Error('정수를 입력해야 합니다');
  }
  return a;
}