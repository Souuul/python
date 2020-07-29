# python의 함수
# python의 함수는 크게 2가지 분류가 있어요!
# 1. 내장함수
# 2. 사용자 정의 함수(user define function)

# 함수 > 특정작업을 수행하는 일정량의 코드 모음
# 함수를 만들려면 어떻게 해야 하나요?

# 일반적인 함수의 정의와 사용
# def my_sum(a, b, c): #관용적으로 함수이름은 소문자와 _로 의미있게 표현
# #code convention 함수는 2칸 띄우는 것을 권장
#     return a + b + c
#
#
# result = my_sum(10, 20, 30)
# print("함수 호출의 결과는 : {}".format(result))

# 함수를 호출하는데 전달되는 인자의 수가 가변적일 경우는 어떻게 하나요??
#def my_sum(a,b,c,d) #전달되는 인자의 수가 4개로 고정
# def my_sum(*args): # 전달되는 인자를 tuple로 받아요!
#     tmp = 0
#     for k in args:
#         tmp += k
#     return tmp
#
# result = my_sum(1, 2, 3)
# print("결과값은 : {}".format(result)) # 결과값은 : 6
#
# # python은 함수의 결과값이(리턴값이) 2개 이상일수 있다는데요??
# def my_operator(a, b):
#     result1 = a + b
#     result2 = a * b
#     return result, result2 # 튜플로 저장 !! 튜플은 괄호 생략 가능
#
# result3 = my_operator(1, 2)
# print(type(result3))    #<class 'tuple'>
# print(result3)  #(6, 2)
#
# tmp1, tmp2 = my_operator(10, 20)
# print(tmp1)     #6
# print(tmp2)     #200

# python의 함수는 default parameter를 사용할 수 있어요!
# def my_default(a, b, c=True):    # 맨 마지막 인자만 값을 할당가능 (중간 X)
#     data = a + b
#     if data > 10 and c:
#         return data
#     else:
#         return 0
#
# result1 = my_default(10, 20, False)
# print(result1)   #0
# result2 = my_default(10, 20) # 실인지 (real parameter)
# print(result2)   #30

# python 함수의 인자는 mutable, immutable 둘 중에 하나에요.
# call-by-value & call-by-reference X
# python에서 함수에 인자를 전달하고 함수는 전달된 인자를 받아요!
# 어떤경우는 실인자의 데이터가 변하는 경우가 있어요
# 어떤 경우는 실인자의 데이터가 변하지 않는 경우가 있어요!

# def my_func(tmp_number, tmp_list):
#     tmp_number = tmp_number + 100
#     tmp_list.append(100)
#
# data_x = 10         #Numeric
# data_list = [10]    #list
#
# my_func(data_x, data_list)
#
# print(data_x)       # 변화가 없어요 10 immutable (숫자, 문자열, tuple)
# print(data_list)    # 변화가 있어요! [10,100] mutable (list, dict)

##################################################################

# 사용자 정의함수가 끝났으니 이제 내장함수에 대해서 알아보아요!!
# id()라는 함수는 좀 알아둘 필요가 있어요!!
# id : 객체의 고유 주소값을 return하는 함수에요!
# my_list1 = [1, 2, 3, 4]
# my_list2 = [1, 2, 3, 4]
# print(id(my_list1))    #140661387559392  // id 값은 다름
# print(id(my_list2))    #140661387561952
#
# # 숫자인 경우에는 0 ~ 256까지는 너무나 많이 사용하는 객체(값) pycharm에서는 256 이후의 값도 동일하게 처리
# my_list3 = 100
# my_list4 = 100
# print(id(my_list3))    #4486059904
# print(id(my_list4))    #4486059904

# 내장함수쪽은 너무 많고 주요한 함수는 알아둬야 하지만 일반적으로 코드를 작상해 나가면서 하나씩 알아가는 방법이 가장 좋아요 !!


# 함수와는 다르지만 함수의 역할을 수행하는 lambda expression (람다표현식)
# lambda : 한줄로 함수를 정의하는 방법
#          함수의 이름이 없어요!!(anonymous function)
#          이름이 없는데 어떻게 사용하나요?
#          이름이 없기 때문에 변수에 저장, 함수의 인자로 사용
#          함수의 결과값(리턴값)으로 함수를 리턴
#          > first class (1급)

# my_lambda = lambda x1, x2, x3 : x1 + x2 + x3   #인자를 입력하고, : 뒤에 해야하는 일을 적음 (return과 비슷하지만 않음)
# result = my_lambda(10, 20, 30)       # 10 + 20 + 30 (이러한 식으로 바뀜)
# print(result)       #60

# 결정적으로 람다가 함수와 다른점은... 람다는 대체식입니다.