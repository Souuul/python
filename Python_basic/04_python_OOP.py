# 1990년도 이전
# 가장 대표적인 프로그램 작성 방식
# 구조적 프로그래밍(절차적 프로그래밍)
# 프로그램 작성시 기능으로 세분화해서 각각의 기능을 모듈로 제작 프로그램을 작성

'''
절차적 프로그램 !!
                      은행업무
        예금        대출       외환      펀드 ..
    입금 출금 이체
자행입금 타행입급 ....

세분화 시켜서 분리하는 것
더이상 세분화가 불가능하면 module (function) 로 작성
모듈을 공유하여 사용가능 (입금에서도 사용가능하고 펀드에서도 사용가능하고 모듈을 공유가 가능)
모듈을 수정하면 전부다 수정을 해야하는 소요가 있음!!

절차적 프로그램의 장점
설계하기가 쉬움 ( 사람마다 거의 유사한 설계가 가능)
프로그램을 쉽고 빠르게 만들 수 있음.

절차적 프로그램의 단점
수정 및 유지보수가 어려움
'''

'''
세상이 변하고 프로그램의 유지보수가 중요하게 대두됨!
현실세계의 해결해야하는 문제에 대한 구성요소를 파악 (사람마다 설계가 달라짐, 설계에 대한 어려움)

유지보수가 좋아짐 

은행
은행지점    고객    텔러      ATM    계좌   >  개체(object)
객체지향프로그램(OOP_Object Oriented Programming)
개체를을 파악해서 그 개체들간의 관계를 프로그래밍 하는 방식을 객체지향 프로그래밍 이라고한다

개체들을 파악한 후 이 각각의 개체를 프로그램적으로 묘사해야 해요
객체 모델링

ex) 사람을 프로그램적으로 묘사해보아요 (객체모델링을 해 보아요!)
추상화(Abstraction) 과정을 거쳐서 사람을 객체모델링 할 꺼에요!!
이런 개체들은 속성, 행위가 있드라!! (단순화)
           속성 - 변수 (property,meber field, field) 
           행위 - 함수 (method) # 누군가에게 종속되어야 함
class라는 걸 이용해서 추상화과정을 거친 개체를 프로그램적으로 표현하게되요!

class 
1. 객체 모델링의 수단

class 사람    #키, 몸무게, 나이, 이름등 다양한 변수를 모아서 새로운 data type(추상데이터 타입)인 사람을 만드는 것...
      - 키(변수)       heigth  > float
      - 몸무게(변수)    weight  > float
      - 나이(변수)      age    > int
      - 이름(변수)      name   > str
      - 걷는다(메소드)
      - 말한다(메소드)
      - 잔다(메소드)
      
class는 data type 관전에서 봤을때는 기존 데이터타입을 이용해서 새로운 data type을 만드는 것이라고 볼 수 있어요
class > 추상적인 데이터 타입이라고 불러요 (Abstract data type _ ADT)
'''

''' 요약 !!!!!
구조적 프로그래밍 (절차적 프로그래밍)
프로그램 작성 시 기능으로 세분화해서 각각의 기능을 모듈화(함수화)해서 구현
프로그램 구조를 이해하기 쉽고 프로그램을 빠르게 만들 수 있어요!
프로그램 규모가 커지면 유지보수와 코드의 재사용에 한계가 오게됩니다.

객체지향 프로그래밍
현실세계의 해결해야 하는 문제를 그대로 프로그램으로 묘사(표현)
프로그램을 구성하는 주체들(개체, 객체, object)을 파악하고
그 객체들간의 데이터 흐름에 초점을 맞추어서 프로그램을 작성
프로그램을 설계하고 작성이 상대적으로 어려움!(구조적 프로그래밍에 비해)
일단 제대로 작성된 객체지향 프로그램은 유지보수와 재사용성에 상당한 이점
'''

###########################################################
#학생의 이름, 학과, 학번, 평균평점을 저장하는 방법
# stu_name = "홍길동"
# stu_dept = "심리학과"
# stu_number = "20201134"     # 숫자보다는 문자열이 처리하기 편함 _숫자를 쓰는 이유는 연산하기 위함
# stu_grade = 3.5
#
#
# #만약 3명의 학생이 있으면 어떻게 하나요??
# stu1_name = "홍길동"
# stu1_dept = "심리학과"
# stu1_number = "20201134"
# stu1_grade = 3.5
#
# stu2_name = "김길동"
# stu2_dept = "컴퓨터"
# stu2_number = "20201135"
# stu2_grade = 2.0
#
# stu3_name = "신사임당"
# stu3_dept = "경영학과"
# stu3_number = "20201136"
# stu3_grade = 4.0
#
# #  코드가 너무 불필요하게 반복적이고 확장성이 없는 코드가 됬어요.....
# stu_name = ["홍길동", "김길동", "신사임당"]
# stu_dept = ["심기학과", "컴퓨터", "경영학과"]
# stu_num = ["20201134", "20201135", "20201136"]
# stu_grade = ["3.5", "2.0", "4.0"]

# index를 이용해 처리하는게 쉬운작업은 아니고 코드에 모든 의미가 다 내포되어 있는게 아닌 문제가 발생
# 다른사람이 보기에 분석하기 쉬운코드

# 어떻게 하면 이런내용을 class 이용해서 객체지향적으로 표현할수 있을까?
# 학생이라는 개념을 프로그램적으로 모델링을 해 보아요!

# class Student(object):  #class 이름은 관용적으로 첫 글자는 대문자로 작성
#     def __init__(self, name, dept, num, grade): #모든 class가 가지고 있음 __init__(self): 인스턴스를 초기화 하는 것
#         self.name = name #. 연산자 //인스턴스안에 또다른 저장공간 사각형안에 4개의 사각형 다시생성
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#              # instance variable
# students = []
# students.append(Student("홍길동", "심리학과", "20201134", 3.5))
# students.append(Student("김길동", "컴퓨터", "20201135", 2.0))
# students.append(Student("신사임당", "경영학과", "20201136", 4.0))
# print(students[0].name) #홍길동
        #    name dept num grade # instance variable
        # | ㅁ    ㅁ   ㅁ   ㅁ   | # instance
# self 객체를 가르치는 주소값
# 클래스 기반으로 저장공간(instance)을 확보하고 클래스의 매소드를 활용하여 저장 // 저장됨


##########################################################
## Python은 객체지향 언어에요!!
## Python에서 나오는 모든것은 다 객체(instance)에요

# a = 10
# print(type(a))      #<class 'int'>
# my_list = [10]
# print(type(my_list))    #<class 'list'>

# class list(object):
#       ~~~~
#       ~~~~
#       ~~~~

# 숫자도 객체(instance)고, 리스트도 객체(instance)고 str(문자열)도 객체고, 함수도 객체에요!

# 객체(instance)가 있다는건 > class가 존재한다는 얘기에요!
# 객체(instance) > 변수, method

# my_list = [10, 20]
# my_list.append() # list 가 가지고 있는 append() method!!!!!
# 객체(instance)란 속성과 같은 여러가지 데이터 + 메소드를 가지고 있는 데이터 구조를 지칭해요!


# class Student(object):
#     def __init__(self, name, dept, num, grade):     # constructor(생성자)_java, c, __init__
#         self.name = name                            # initializer _ python 에서만
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
#     def __repr__(self):     #주소가 아닌 바로 출력되게끔 하는 메소드
#         return self.name
#
#     def change_dept(self, tmp_dept):
#         #tmp_dept가 정상적인 학과인지 check하는 코드
#         self.dept = tmp_dept

# student = Student("홍길동", "심리학과", "20201133", 4.5)

# print(student)      #홍길동
# print(student.name) #홍길동
# print(student.dept) #심리학과
#
# # information hiding () 정보은닉  // 데이터가 오염되는 것을 막기위하여 사용
# student.change_dept("컴퓨터학과")
# print(student.dept)    #컴퓨터학과
#
# student.dept = "컴퓨터학과" #객체에서는 direct로 수정하는 것을 권장하지 않음
# print(student.dept) #컴퓨터학과

################################################################

# python이 제공하는 내장함수 중 dir() 에 대해서 알아보아요!!
# 객체가 인자로 들어오면 해당 객체의 모든 속성과 메소드를 알려줘요!

# student = Student("홍길동", "심리학과", "20201133", 4.5)   #상기 Student class 그대로 사용
# print(dir(student))
#
#
# student.depts = "철학과"   # 오타가 나서 갑자기 다른 instance variable 이 추가됨 (java, c++...은 안됨)
# print(student.depts)     # 철학과
# print(dir(student))      # depts 추가

# 한가지를 더 생각해보아요!!

#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__','__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
# 'change_dept', 'dept', 'grade', 'name', 'num']
# 특별하게 가지고 있는 것은 magic function!!!!

## python의 함수도 객체에요!!
# def my_func(a,b):
#     return a+b
#
# print(dir(my_func))
#
# my_func.myName = "홍길동"      #함수 조차 클래스의 범주안에 포함되어 정의되지않은 것도 추가가 가능
# print(dir(my_func))


# class Student(object):
#     scholarship_rate = 3.0      # class variable 모든 instance에서 공유함
#
#     def __init__(self, name, dept, num, grade):
#         self.name = name
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
#     def is_scholarship(self):
#         if self.grade > Student.scholarship_rate:
#             return True
#         else:
#             return False
#
# student = Student("홍길동", "심리학과", "20201133", 4.5)
# print(student.is_scholarship())     #True


#################################
# 절차적 프로그래밍 vs 객체지향 프로그래밍
# 절차적 프로그래밍 (구조적 프로그래밍)
# 구현하고자 하는 문제를 "기능"단위로 세분화해요!
#"기능"으로 세분화 시켜서 더 이상 세부기능으로 분할할 수 없는
#단위기능을 코드로 구형(함수)
# > divide and conquer
# 장점 : 프로그램을 쉽고 빠르게 구현할 수 있어요 > 비용절감효과
# 단점 : 프로그램을 재사용하거나 유지보수하기가 힘들어요!

# - 객체지향 프로그래밍
# 장점 : 프로그램의 유지보수성과 재사용성이 높아져요!
# 단점 : 프로그램을 설계, 구현하기가 힘들어요!
# 내가 해결해야 하는 문제 (구현해야 하는 시스템)을 그대로 프로그램을
# 모델링하는 방식, 그렇기 때문에 기능으로 세분화 하지않고 구성요소를
# 파악한 후 구성요소간의 데이터 흐름에 집중해서 구현하게 되요!
# > 객체 모델링
# 객제 모델링을 하기 위해서 현실 세계의 객체를 단순화(abstraction- 추상화)
# 필요있는 것만 두고 필요없는 것은 날림
# class를 이용해서 객체 모델링을 수행!
# class ??? > 1. 객체 모델링의 수단
# class는 기존 데이터타입을 이용해서 새로운 데이터 타입을 만드는 도구
# 1. 객체모델링의 수단
# 2. ADT (abstraction data type !! 강조)
# class와 instance 를 생성해야 해요!
#        instance는 객체(object) > 메모리 공간


#class 와 instance 기본적인 코드작성
# class Student(object):          # object 향후 설명
#     scholarship_rate = 3.0      # class variable
#
#     def __init__(self, name, dept, num, grade):   # contructor(생성자), initializer
#         self.name = name                          # instance variable을 선언하고 초기화
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
#     def __repr__(self):     # magic function 이미 하는일이 정해져있음
#         return self.name    # def 와 return !! 기본적으로 생각할 것
#
#     def is_scholarship(self):   #instance method (instance variable를 handling 하는 method)
#         if self.grade > Student.scholarship_rate:
#             return True
#         else:
#             return False
#
# students = Student("아무개", "경영학과", "213123", 3.1)
# print (students.is_scholarship())


#####################################################

# namespace(네임스페이스)
# 객체가 가지는 데이터를 나누어서 관리하는 공간
# instance namespace
# class namespace
# superclass namespace // 상속이후 생각할 것 !

# instance namespace < class namespace < superclass namespace  ( < 포함 )
# ㅁ<ㅁ<ㅁ N.S


# class Student(object):
#     scholarship_rate = 3.0      # class namespace
#
#     def __init__(self, name, dept, num, grade):
#         self.name = name        # istance namespace
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
#     def __repr__(self):
#         return self.name
#
#     def is_scholarship(self):
#         if self.grade > self.scholarship_rate: # instance namespace 에는 없지만 상위
#             return True                        # namespace에서 존재하기 때문에 자동적으로 찾음
#         else:                                  # 하지만 class variable을 사용하는 것을 권장
#             return False
#
# students = Student("아무개", "경영학과", "213123", 4.0)
# print (students.is_scholarship())   # True
#
# students.scholarship_rate = 4.5     # instance namespace에 생성
# print (students.is_scholarship())   # False _self.scholarship_rate 로 코드를 변경했기 때문에
#
#
#
# # python은 동적으로 속성이나 method를 추가할 수 있어요!!
#
# print(students.dept)
# students.depts = "컴퓨터학과"    #depts 속성이 추가되요!!
# print(students.depts)


##############################################################
'''
instance method(self 인자를 가지고 있는 method)는 하나의 
인스턴스에 한정된 데에티럴 생서, 변경 참조하기 위해서 사용되요!
class method는 클래스를 인자로 받아서 class variable을
생성, 변경, 참조하기 위해서 사용 @classmethod 

static method # class 안에서 정의된 일반 함수
@staticmethod 
'''
# class Student(object):
#     scholarship_rate = 3.0
#
#     def __init__(self, name, dept, num, grade):
#         self.name = name
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
#     @classmethod        # class method decorator // 필수로 붙여야함
#     def change_sholarship(cls, rate):     # class 자체를 인자로 받아서 처리
#         cls.scholarship_rate = rate
#         print("장학금 기준이 변경되었어요!")
#
#     @staticmethod       #
#     def is_valid_schlarship(rate):
#         if rate < 0:
#             print("장합금 기준 학점은 음수가 될 수 없습니다.")
#
#
#     def is_scholarship(self):
#         if self.grade > Student.scholarship_rate:
#             return True
#         else:
#             return False
#
# students = Student("아무개", "경영학과", "213123", 4.0)
# Student.change_sholarship(4.5)      # class에서 method 바로 찾아야 함
#                                     # 장학금 기준이 변경되었어요!
# change_rate = -3.0
# Student.is_valid_schlarship(change_rate) # 장합금 기준 학점은 음수가 될 수 없습니다.
# print (students.is_scholarship())   # False




###############################################################
'''
information hiding (정보은닉)
instance가 가지는 속성은 매우 매우 중요한 데이터이기 때문에
외부에서 직접적으로 access 하는 건 좋지 않아요!
어떻게 외부에서 직접적으로 access 하는 것을 막을 수 있는가?
프로그래밍 언어마다 달라요!!
Java > access modifier(접근제어자)
       public vs private

Python에서 속성에 직접적으로 접근하는 것을 막기위해서는 어떻게 해야하나요??

'''

# class Student(object):
#
#     def __init__(self, name, dept, num, grade):
#         self.name = name
#         self.__dept = dept
#         self.num = num
#         self.grade = grade
#     # private으로 처리된 속성이 있으면 외부에서 직접적인
#     # access가 안되기 때문에 method를 이용해서 사용하도록 처리
#     # private으로 되어 있는 속성의 값을 알아오는 용도의 method가 필요하고
#     # 이런 method는 getter (getter의 이름을 짓는 방법이 정해져 있어요 !!)
#     def getDept(self):      #첫문장을 대문자 권장사항이며 강제사항은 X
#         return self.__dept  #class 내부에서는
#     # > setter는 값을 설정해주는 method
#     def set_dept(self, dept):   # dept 를 변경
#         self.__dept = dept
#
#     def __print_date(self): # 클래스 내부에서 method를 감출수 있어요!
#         return self.name
#
#
# students = Student("아무개", "경영학과", "213123", 4.0)
# # print(students.__dept)      # private 처리를 한거에요! 접근불가
# print(students.getDept())     # 경영학과
# students.set_dept("컴퓨터학과")
# print(students.getDept())     # 컴퓨터학과
# print(Student.__name)   #type object 'Student' has no attribute '__name'
# 여기까지가 단일 class에 대한 이론적인 내용이에요!


##########################################################
# 상속 # 객체지향의 꽃!!
# 객체지향을 하는 이유는 > 유지보수와 재사용성!
# 재사용성을 위한 대표적인 객체지향 기법 > Inheritance(상속)
# A의 클래스르 B의 클래스에서 사용할 경우
# parent class, super class, upper class (부모 class) // A class
# child class, sub class (자식 class) // B class

# Is - A 관계 # 같다의 관계
# sub clss is a superclass 역은 성립하지 않음!
# 포유류 (super class) 사람(sub class)

# 두 개의 class를 이용해서 우리 상속을 알아보아요!!
# Unit class, Marine class
# Unit class > 모든 unit이 공통으로 가지고 있는 속성과 method로 구성
#              super class로 사용, base class
# Marine > sub class로 사용

# class object():
#       ~
#       ~
# python의 모든 class는 object class에요!!
# python의 모든 class는 object class를 상속해야 해요 !! # IS-A 관계때문에

# class Unit(object):      #괄호는 상속의 의미 // object class에서 상속을 받을 거에요!!
#     def __init__(self, demage, life):
#         self.utype = self.__class__.__name__ #클래스의 이름을 호출
#         self.demage = demage
#         self.life = life
#
#     def show_status(self):
#         print("직업 : {}".format(self.utype))
#         print("공격력 : {}".format(self.demage))
#         print("생명력 : {}".format(self.life))
#
# class Marine(Unit):
#     pass
#
# marine_1 = Marine("100", "100")
# marine_1.show_status()
# '''
# 직업 : Marine
# 공격력 : 100
# 생명력 : 100
# '''

####################################################
# 상속 추가 !!!!
#
# class Unit(object):      #괄호는 상속의 의미 // object class에서 상속을 받을 거에요!!
#     def __init__(self, demage, life):
#         self.utype = self.__class__.__name__ #클래스의 이름을 호출
#         self.demage = demage
#         self.life = life
#
#     def show_status(self):
#         print("직업 : {}".format(self.utype))
#         print("공격력 : {}".format(self.demage))
#         print("생명력 : {}".format(self.life))
#
#
# class Marine(Unit):      #괄호는 상속의 의미 // object class에서 상속을 받을 거에요!!
#     def __init__(self, demage, life, range_upgrade):   # 값을 반는것은 그대로 표시
#         super(Marine, self).__init__(demage, life)    # self.utype = self.__class__.__name__ #클래스의 이름을 호출
#                                                       # self.demage = demage
#                                                       # self.life = life
#         self.range_upgrade = range_upgrade
#
#     def show_status(self):
#         super(Marine, self).show_status() # print("직업 : {}".format(self.utype))
#         # print("공격력 : {}".format(self.demage))
#         # print("생명력 : {}".format(self.life))
#         print("사거리 업그레이드 유무 : {}".format(self.range_upgrade))
#
#
# marine_1 = Marine("100", "100", True)
# marine_1.show_status()
# '''
# 직업 : Marine
# 공격력 : 100
# 생명력 : 100
# 사거리 업그레이드 유무 : True
# '''

###############################################################

#사용할 유닛들은 Marine, Medic, Vulture, Dropship 4종류의 unit

# super class
# class Unit(object):
#     def __init__(self, demage, life):
#         self.utype = self.__class__.__name__
#         self.demage = demage
#         self.life = life
#
#     def show_status(self):
#         print("직업 : {}".format(self.utype))
#         print("공격력 : {}".format(self.demage))
#         print("생명력 : {}".format(self.life))
#
#     def attack(self):
#         pass
#
# class Marine(Unit):
#     def __init__(self, demage, life, range_upgrade):
#         super(Marine, self).__init__(demage,life)
#         self.range_upgrade = range_upgrade
#     # overriding
#     def show_status(self):
#         super(Marine, self).show_status()
#         print("사정거리 업그레이드 유무 : {}".format(self.range_upgrade))
#     # overriding
#     def attack(self):
#         print("마린이 총으로 공격합니다.")
#
#     def stimpack(self):
#         if self.life < 20:
#             print("체력이 낮아서 스팀팩 수행이 불가능 합니다.")
#         else:
#             self.life -= 10
#             self.demage *= 1.5
#             print("마린이 스팀팩을 사용했어요!!")
#
# # marine_1 = Marine(5, 40, True)
# # marine_1.show_status()
# '''
# 직업 : Marine
# 공격력 : 5
# 생명력 : 40
# 사정거리 업그레이드 유무 : True
# '''
# # marine_1.stimpack() # 마린이 스팀팩을 사용했어요!!
# # marine_1.stimpack() # 마린이 스팀팩을 사용했어요!!
# # marine_1.stimpack() # 마린이 스팀팩을 사용했어요!!
# # marine_1.stimpack() # 체력이 낮아서 스팀팩 수행이 불가능 합니다.
# #
# # marine_1.attack() # 마린이 총으로 공격합니다.
#
#
# class Medic(Unit):
#     #overriding
#     def attack(self):
#         print("메딕이 치료합니다. 힐힐!!!")
# # medic_1 = Medic(0,50)
# # medic_1.show_status()
# '''
# 직업 : Medic
# 공격력 : 0
# 생명력 : 50
# '''
# # medic_1.attack()    #메딕이 치료합니다. 힐힐!!!
#
#
# class Vulture(Unit):
#     def __init__(self, demage, life, amount_of_mine):
#         super(Vulture, self).__init__(demage, life)
#         self.amount_of_mine = amount_of_mine
#
#     # overriding
#     def attack(self):
#         print("벌쳐가 공격합니다. ~~~")
#
# class Dropship(Unit):
#     #overriding
#     def attack(self):
#         print("특정 목표지점을 이동합니다. 슝!!")
#
#     def board(self, unit_list):
#         self.unit_list = unit_list
#         print("유닛들을 드랍쉽에 태워요!!")
#
#     def drop(self):
#         print("모든 Unit이 드랍쉽에서 내립니다.")
#         return self.unit_list
#
# # marine을 생성합니다. 3마리
# marine_1 = Marine(100, 100, False)
# marine_2 = Marine(100, 100, False)
# marine_3 = Marine(100, 100, False)
#
# # medic을 생성합니다. 1마리
# medic = Medic("0", "100")
#
# # vulture를 생성합니다. 2마리
# vilture_1 = Vulture("200", "100", 3)
# vilture_2 = Vulture("200", "100", 3)
#
#
# # list를 이용해서 여러개의 객체를 저장할꺼에요!
# troop = list()
# troop.append(marine_1)
# troop.append(marine_2)
# troop.append(marine_3)
# troop.append(medic)
# troop.append(vilture_1)
# troop.append(vilture_2)
#
# # Dropship 생성
# dropship = Dropship("0", "100")
#
# # Dropship에 유닛들을 태워요!
# dropship.board(troop)
#
# # 공격지점으로 이동
# dropship.attack()
#
# # 공격지점에서 내리기
# my_list = dropship.drop() # my_list 는 주소
# my_list = dropship.drop() # my_list 는 주소
#
# #스팀팩을 쓰고 공격하기
# for unit in my_list:
#     if isinstance(unit, Marine):    #인스턴스인지 확인
#         unit.stimpack()
#     unit.attack()
'''
유닛들을 드랍쉽에 태워요!!
특정 목표지점을 이동합니다. 슝!!
모든 Unit이 드랍쉽에서 내립니다.
마린이 스팀팩을 사용했어요!!
마린이 총으로 공격합니다.
마린이 스팀팩을 사용했어요!!
마린이 총으로 공격합니다.
마린이 스팀팩을 사용했어요!!
마린이 총으로 공격합니다.
메딕이 치료합니다. 힐힐!!!
벌쳐가 공격합니다. ~~~
벌쳐가 공격합니다. ~~~
'''

# 공유폴더에 들어가시면 student_score.txt라는 파일이 있어요!
# 각사람에 대한 데이터를 읽어서
#성적순으로 출력하시면 되요! 출력양식은 다음과 같습니다.
# 1등 아이유 95.6
# 2등 홍길동 89.3
# 3등 최길동 88.2



class Student(object):
    def __init__(self, name, kor, eng, math):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__math = math
        self.avg = round((kor + eng + math) / 3)

    def __repr__(self):
        return "{} {}".format(self.__name, self.avg)


file1 = open("/Users/admin/PycharmProjects/Python_basic/student_score.txt", "r", encoding='euc-kr') # 맥
students = list()
while True:
    line = file1.readline()
    if not line:
        break
    x = line[:-1]
    stu_data = x.split(',')
    students.append(Student(stu_data[0], int(stu_data[1]), int(stu_data[2]), int(stu_data[3]))) # \n이 처리가됨
file1.close()
result = reversed(sorted(students, key=lambda students: students.avg))   #객체가 아닌 평균값을 가지고 정렬하세요

idx = 1
for tmp in result:
    print("{}등 {}".format(idx, tmp))
    idx += 1
'''
1등 아이유 95
2등 강감찬 60
3등 최길동 48
4등 이선희 38
5등 신사임당 23
6등 김연아 20
7등 홍길동 15
'''


