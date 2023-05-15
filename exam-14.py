# function이 def이다.
def exampleOne(a):
    # type과 isinstance이 있다.
    if isinstance(a, int):
        if (a - int(a) != 0):
            raise ValueError('정수를 입력해야 합니다')
    else:
        raise ValueError('정수를 입력해야 합니다')
    
    return a


# print(exampleOne(324.5)) 정수를 입력해야 합니다.

# 들여쓰기 잘하기!