# 1. 주석
# Python의 주석 : 1줄 주석은 > #
# 여러줄 주석은 """ """

"""

여기는 몽땅
주석이에요 !!

"""

'''
이것도 주석입니다.
여기도 주석입니다.
'''

# 2. Python의 Keyword
# import keyword
# print (keyword.kwlist)
# 어떤 키워드를 사용할 수 있는지 확인해 봅시다 !!

# 3. 변수의 생성과 삭제 C와는 다르게 데이터 타입없이 변수명만 입력가능
#my_var = 100
#print(my_var)

# 4. 변수를 삭제할 수 있어요 !!
#del my_var
#print(my_var)

# Python의 데이터 타입(data type)
# Python의 built-in data type (이미 정의되어있는 데이터 타입)
# - Numeric (숫자)
# - Text sequence (문자열)
# - Sequence (순서가 있는것 _List, tuple)
# - Set
# - Mapping
# - Bool (True, False)


# 1) Numeric Data Type (숫자형)
# int(정수)
# float(실수)
# complex(복소수)

# a = 100 # 정수
# b = 3.14159265358979 # 실수
# c = 1+ 2j
# d = 0o34 # 8 진수
# e = 0xAB # 16 진수


# 데이터 타입을 알고싶어요!
# print (type(a)) # class int
# print (type(b)) # class float
# print (type(c)) # class complex
# print (type(d)) # class int
# print (type(e)) # class int

# my_result = 3 / 4 # 0이 아니라 0.75  프로그래밍에서는 버림으로 표시
# print(my_result) # 0.75


# my_result = 10 % 3 #나머지 연산자
# print(my_result) # 1
#
# my_result = 10 // 3 #몫 연산자
# print(my_result) # 3

###########################################################


# 2) Text sequence (문자열, str)
# 다른 언어는 문자와 문자열을 구분
# 문자는 한글자, 문자열은 두글자 이상으로 구성
# 문자를 표현할때 다른 언어는 ''
# 문자열을 표현할 때 다른 언어는 ""
# Python은 문자열을 표현할 때 ('',"")
# a = 'Hello'
# b = "K"
# c = 'python'

# 문자열 연산
# first = 'haha'
# second = 'hoho'
#
# print(first + second) #hahahoho
# print(first + str(10)) # error 자동으로 숫자를 문자로 변경 X ( Java 에서는 가능)
# print(first*3) #hahahahahaha

#indexing_python은 배열이 존재 X / 다른언어에서는 - index 사용가능
# my_var = 'HELLO'
# print(my_var[1])

# slicing 범위를 정하고 영역을 추출하는 ( 시작과 끝의 범위를 설정해야함)
# my_var = 'HELLO'
# print(my_var[0:3]) #HEL
# print(my_var[0:]) #HELLO
# print(my_var[0:-1]) #HELL
# print(my_var[-2:]) #LO
# print(my_var[:]) # HELLO

# in , not in 연산자
# myStr = "This is a sample Test"
# print("sample" in myStr) # True / 대소문자 구별
# print("sample" not in myStr) #False / 대소문자 구별

# formatting // %d (숫자)
# num_of_apple = 10
# myStr = "나는 사과를 %d개 가지고 있어요!" % num_of_apple
# myStr1 = "나는 사과를 {}, 바나나 {}개 가지고 있어요!" .format(num_of_apple, 20)
# myStr2 = "나는 사과를 {1}, 바나나 {0}개 가지고 있어요!" .format(num_of_apple, 20)
# print(myStr) #나는 사과를 10개 가지고 있어요!
# print(myStr1) #나는 사과를 10, 바나나 20개 가지고 있어요!
# print(myStr2) # 나는 사과를 20, 바나나 10개 가지고 있어요!

# 문자열 method를 이용해서 문자열 처리를 할 수 있어요!! (함수 vs method)
# myStr = "cocacola"
#
# # 문자열의 길이를 알고 싶으면??
# print(len(myStr)) #len() 함수를 이용 // 8
# print (myStr.count('c')) #str의 method인 count()를 이용 // 3
# print (myStr.find('o')) #str의 method인 find()를 이용 // 1(가장 첫번째 발견된 곳 찾아줌)

# myStr = "   myHobby"
# print(myStr.upper()) #대문자 변환
# print(myStr.lower()) #소문자 변환
# print(myStr.strip()) #앞뒤의 공백 날리기

# 3. Sequence type
# list
# 임의의 객체(데이터)를 순서대로 저장하는 집합 자료형
# Java의 ArrayList와 유사
# List는 literal로 표현할 때 [] (대괄호로 표현)
# my_list = []
# print(type(my_list))
# my_list = list() # 함수를 이용하여 리스트를 제작
# my_list = [1, 2, 3] # ~ : code convention _ 가독성이 좋게 표현하게 Hint 기능 제공
# my_list = [1, 2, 3.14, "Hello", [5, 6, 7], 100] # 중첩리스트, 2차원이 아님
#
# #indexing 과 Slicing을 할 수 있어요!!것
# print(my_list[1]) #2
# print(my_list[-2]) #[5, 6, 7]
# print(my_list[4:5]) #[5, 6, 7] // list의 Slicing 은 list
# print(my_list[-2][1]) #6
# print(my_list[0:2]) #[1, 2]

# list 연산
# a = [1, 2, 3]
# b = [4, 5, 6]
# print (a + b) # [1, 2, 3, 4, 5, 6] list 의 합은 하나의 리스트로 생성
# # 단 행렬에서의 연산은 [5,7,9] numpy에서 사용시 주의 할 것
# print (a*3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# a = [1, 2, 3]
# a[0] = 5
# print(a) # [5, 2, 3]
#
# a[0] = [7, 8, 9]
# print(a) # [[7, 8, 9], 2, 3]
#
# a[0:1] = [7, 8, 9]
# print(a) # [7, 8, 9, 2, 3]

# a = [1, 2, 3]
# # a.append(4) 끝에 추가하는 것
# # print(a) #[1, 2, 3, 4]
# a.append([5, 6, 7])
# print(a) #[1, 2, 3, [5, 6, 7]]

# my_list = ["홍길동", "아이유", "강감찬", "신사임당", "Kim"]
# result = my_list.sort() # 리스트를 오름차순으로 정렬_ 1 2 3 4 5
# print(result) # Nono
# print(my_list) # ['Kim', '강감찬', '신사임당', '아이유', '홍길동']

# Python
# Data type
# Built-in data type
# 1. Numeric (int, float, complex)
# 2. Text Sequence Type(str) : 문자열
# 3. Sequence (list )
# 4. Mapping( dict)



# Sequence type (tuple)
# list는 []로 표현, tuple은 ()로 표현
# a = (1, 2, 3)  # tuple
# # tuple은 일단 만들어지면 내용 변경이 안되요!!, 불변의 데아터를 보호할 경우 tuple로 사
# a[0] = 100
# print[a] # error

#a = (1, ) # 요소가 1개만 존재하는 tuple의 경우에 (1, ) 표현 _계산 우선인지, tuple인지 구분하기 위해
#a = (1, 2, 3) #일반적인 tuple 의 경우 괄호 생략 가능
#a = 1, 2 ,3
#print(type(a)) # <class 'tuple'>

# a = (1, 2, 3)
# b = (5, 6, 7)
# print(a+b) # tuple의 요소들이 변경이 되지 않는 이상 연산가능

# a = (1, 2, 3)
# my_list = list(a) # tuple을 list로 변환 가능
# print(my_list) #[1, 2, 3]
#
# my_tuple = tuple(my_list)
# print(my_tuple) # (1, 2, 3)

# range
# 주로 for문에서 사용
# 같은 데이터를 적응양의 데이터로 표현이 가능
# my_range = range(10) # range(처음, 끝, 증감) , 실제로 숫자를 넣지 않아도 표현이 가능
# # 적은 메모리로 처리가 가
# print(type(my_range)) #<class 'range'>
# print(my_range) #range(0, 10)
# print(my_range[2]) # 2
# print(my_range[2:7]) # range(2, 7)
# print(3 in my_range) # True


# 4. Mapping(dict)
# Dictionary는 key와 value로 데이터를 저장하는 구조
# { }로 표현해요!!
# a = { "name" : "홍길동", "age" : 40} #Json 표
# print(type(a)) #<class 'dict'>
# print(a['name'])
# a["address"] = "서울"
# print(a) #{'name': '홍길동', 'age': 40, 'address': '서울'}
# print(a.get("age")) # 40

#dict에서 많이 사용하는 대표적인 method 3개
# a = { "name" : "홍길동", "age" : 40, "address": "서울"}
# print(a.keys()) # dict_keys(['name', 'age', 'address']) // 리스트는 아님
# print(type(a.keys())) #<class 'dict_keys'>
# print(list(a.keys())) # ['name', 'age', 'address']
# print(a.values()) #dict_values(['홍길동', 40, '서울'])
# print(a.items()) #dict_items([('name', '홍길동'), ('age', 40), ('address', '서울')]) // tuple로 표현

########################################
#Bool data type > Boolean(True, False)
#사용하는 연산자 > and, or, not 연산자를 사용할 수 있어요
#(&, |, ~ 연산자를 이용해 비트연산을 해요!)

# 다음의 경우는 Python에서 False로 간주
# 1. 빈 문자열은 False로 간주 > "", ''
# 2. 빈 리스트는 False로 간주 > []
# 3. 빈 tuple도 False로 간주 > ()
# 4. 빈 dict도 False로 간주 > {}
# 5. 숫자 0은 False로 간주
# 6. None은 당연히 False로 간주

# a = 5
# b = 0
# print(a & b) # 0 // & : bitwise 연산
#              # 0101 & 0000 > 0000
#
# print(a | b) # 5 // | : bitwise 연산
#              # 0101 | 0000 > 0101

##############################################################

# Set data type
# 집합 자료형이고 중복을 허용하지 않아요!
# 순서가 존재하지 않는 자료형

# {} > dict 중괄호로 표현 > {"key": "value"}
# {} > set  중괄호로 표현 > {1, 2, 3}

# my_set = {1, 2, 3, 4, 1, 2}
# print(my_set) #{1, 2, 3, 4} 중복을 제거
#
# my_list = [1, 2, 3, 4, 1, 2]
# my_set2 = set(my_list)
# print(my_set2) # {1, 2, 3, 4}

# my_str = "Hello"
# my_set = set(my_str)
# print(my_set) #{'H', 'e', 'l', 'o'}

# set에서 사용하는 연산자
# 합집합(unino : |), 교집합(intersection : &), 차집합(difference : -)

# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# print (s1 | s2) #{1, 2, 3, 4, 5, 6}
# print (s1 & s2) #{3, 4}
# print (s1 - s2) #{1, 2}

############################################################


# 추가적으로 날짜관련 사항도 알아보아요!!
# date와 datetime에 대해서 알아보아요!

# from datetime import date, datetime
# today = date.today()
# print(today) # 2020-07-15
# # 오늘 날짜는 : 2020년 07월 15일 입니다.
#
# my_str = '오늘 날짜는 : {}년 {}월 {}일 입니다.'
# my_str.format(today.year, today.month, today.day)
# print (my_str) #오늘 날짜는 : {}년 {}월 {}일 입니다.
#
# my_str = '오늘 날짜는 : {}년 {}월 {}일 입니다.'
# my_str = my_str.format(today.year, today.month, today.day)
# print (my_str) #오늘 날짜는 : 2020년 7월 15일 입니다.
#
# my_datetime = datetime.today()
# print(my_datetime) #2020-07-15 10:43:36.211811
# print("현재시간은 :{}시 입니다.".format(my_datetime.hour)) #현재시간은 :10시 입니다.
# print("현재시간은 :{}분 입니다.".format(my_datetime.minute)) #현재시간은 :43분 입니다.

#오늘이 07월 15일이에요
#내일의 날짜는 07월 16일 이에요. > 초

#오늘이 01월 31일에에요.
#내일의 날짜는 02월 1일이에요. > 중급

# 오늘이 03월 01일이에요.
# 어제의 날짜는 02월 29일이에요. > 어려움

## 결론은 날짜 연산은 처리하기가 너무 힘들어서 계산을 통해 처리하는게 아니라 delta를 이용해서 처리해요!

#from datetime import date, datetime ,timedelta
# today = date.today() # 오늘 날짜를 구함 2020-07-15
# days = timedelta(days = -1) # 하루전에 delta 값을 생성
# print (today + days) #2020-07-14 // delta 가 - 이므로 days의 delta를 더함

# today = datetime.today()
# hours = timedelta(hours = -5)
# print(today + hours) #2020-07-15 05:57:12.784611

# 1달전 날짜를 알아보아요
# 예) 오늘 날짜가 3월 31일 > 1달전 날짜는?

# from datetime import date
# today = date.today()
# days = timedelta(years=-1)
# print (today + days) #TypeError: 'years' is an invalid keyword argument for __new__()
# time data는 year와 month 가 들어올 수 없음

# 연도와 월에 대한 timedelta는 존재하지 않아요!
# 그래서 새로운 외부 module을 또 사용해야 해요!

# from datetime import date
# from dateutil.relativedelta import relativedelta # 기본 python 모듈에는 포함되어 있지 않음
# today = date.today()
# months = relativedelta(months=-1)
# print (today + months) #2020-06-15

# 현재 날짜와 시간만 하고 있어요 !!
# 문자열로 되어 있는 날짜를 진짜 날짜로 변환해서 연산을 하고 싶어요!
# from dateutil.parser import parse # parser : 분해해서 조립하는것
# my_date = parse("2019-01-30")
# print(my_date) #2019-01-30 00:00:00

# from datetime import datetime
# from dateutil.parser import parse
# my_date = parse("2019-01-30")
# print(my_date) #2019-01-30 00:00:00
# my_date = datetime(2019, 1, 30)
# print(my_date) #2019-01-30 00:00:00

############################################################

# python의 Data type은 여기까지 정리해보아요!!
