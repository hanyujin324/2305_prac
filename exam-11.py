example=[[1,2,3],[4,[5,6]],7,[8,9]]
def flatten(data); #flatten: 다차원 배열을 1차원으로 바꿔줌
output=[]
for item in data:
  if type(item)==list: #item이 리스트인지 확인
    #재귀적으로 처리
    output+=flatten(item)
  else:
    output.append(item)
    return output
  print(flatten(example))