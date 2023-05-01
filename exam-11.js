/* Pyton 
def는 function을 의미
print는 console.log()를 의미

example=[[1,2,3],[4,[5,6]],7,[8,9]]
def flatten(data);
output=[]
for item in data:
  if type(item)==list:
    #재귀적으로 처리
    output+=flatten(item)
  else:
    output.append(item)
    return output
  print(flatten(example)) */
  let example=[[1,2,3],[4,[5,6]],7,[8,9]];
  function flatten(data); //중첩된 배열을 하나로 만들어 준다.
  let output=[]
  for (item in data){
/*     if(typeof item==list){ } javascript에서는 typeof로 배열인지 확인이 불가능*/
    if(Array.isArray(item)){ //배열인지 확인하기위해 isArray를 사용해야한다.
      output+=flatten(item); //이게 무슨 뜻일까?
    }else{
      output.push(item);
    }
    return output;
  }
console.log(flatten(example));


