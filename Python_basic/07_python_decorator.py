
'''
decorator
decorator의 사전적 의미는 장식가, 도배업자
python에서 Decorator는 기존의 코드에 여러가지 기능을 추가하는 python구문이라고 이해하면 편해요!

Closure
first class에 대해서 알아보았어요
first class function(일급함수) : 파이썬은 일급함수를 지원하는 언어
1. 파이썬의 함수는 변수에 저장할 수 있어요!
2. 함수의 인자로 함수를 이용할 수 있어요! > decorator / 프로그램의 확정성 생산성을 높이기 위함
3. 함수의 결과값(리턴값)으로 함수를 이용할 수 있어요! > closure

'''



# # def my_outer_func(func):
# #     def my_inner_func():
# #         func()
# #     return my_inner_func    #해당함수 코드를 리턴 // ()해당함수의 실행의 결과를 리턴
# #
# # def my_func():
# #     return print("my_func() 함수가 호출되었어요!!")
# #
# # decorated_my_func = my_outer_func(my_func)
# # decorated_my_func()     #my_func() 함수가 호출되었어요!!
# # my_func()               #my_func() 함수가 호출되었어요!!
#
# import time
#
# def my_outer_func(func):        # 목적은 my_func의 기능을 확장시키기 위함!
#     def my_inner_func():
#         print("{} 함수 수행 시간을 계산합니다.".format(func.__name__))
#         start = time.time()     # 1970년 1월 1일 0시 0분 0초 0
#         func()
#         end = time.time()
#         print("함수 수행 시간은 {} 계산합니다.".format(start-end))
#     return my_inner_func    #해당함수 코드를 리턴 // ()해당함수의 실행의 결과를 리턴
#
# # def my_func():
# #     return print("my_func() 함수가 호출되었어요!!")
#
# # decorated_my_func = my_outer_func(my_func)
# # decorated_my_func()     #my_func() 함수가 호출되었어요!!   // 함수자체의 기능을 수정하지 않고 함수의 기능을 수정할 수 있
# # my_func()               #my_func() 함수가 호출되었어요!!
#
# # closure vs decorator // 새로운 기능 추가되는 것을 리턴하는것
#
# @my_outer_func      # decorator 기능을 추가한 my_func를 리턴
# def my_func():
#     return print("my_func() 함수가 호출되었어요!!")
#
#
# my_func()
# '''
# my_func 함수 수행 시간을 계산합니다.
# my_func() 함수가 호출되었어요!!
# 함수 수행 시간은 -5.7220458984375e-06 계산합니다.
# '''


#############################################################

# def print_user_name(*args):   # 인자로 들어온 사람의 이름을 출력 / 정해지지 않는
#     # args는 tuple로 받아요!
#     for name in args:
#         print(name)
# print_user_name("홍길동", "신사임당")      #이렇게도 가능
# print_user_name("홍길동", "신사임당", "유관순")       #이렇게도 가능
'''
홍길동
신사임당
홍길동
신사임당
유관순

'''

# def print_user_name(**kwargs):   # 관용적으로 **kwargs 표기
#     # kkargs는 dict로 받아요!
#     for name in kwargs.values():    # key, value로 구분
#         #print(kwargs.get(name))    # get 을 통해서 추출가능
#         print(name)
# print_user_name(name1 = "홍길동", name2= "신사임당")      #이렇게도 가능


## 받는 함수의 인자의 개수가 다를경우

# def my_outer(func):
#     def my_inner(*args, **kwargs):   # decorator의 인자의 개수를 예측하기 힘들기에 *args, **kwargs 를 적용하여 인자문제 해결
#         print("데코레이터!! 시작")
#         func(*args, **kwargs)        # *args, **kwargs
#         print("데코레이터!! 끝")
#
#     return my_inner
#
# @my_outer
# def my_func():
#     print("이것은 소리없는 아우성!!")
# @my_outer
# def my_add(x,y):
#     print("두 수의 합은 : {}".format(x+y))
#
#
# my_func()
# '''
# 데코레이터!! 시작
# 이것은 소리없는 아우성!!
# 데코레이터!! 끝
# '''
#
# my_add(1,2)
#
# '''
# 데코레이터!! 시작
# 두 수의 합은 : 3
# 데코레이터!! 끝
# '''

# 블로그!!
## 티스토리추천
##http://moon9342.github.io

