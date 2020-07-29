# Magic Function, First Class, Closure



# Magic function
"""
 1. method의 이름 앞뒤에 더블 언더스코어(__)가 붙어있는 method를 지칭해요!
    대표적인 magic function > __init__ (생성자)
 2. class안에 정의되어 있는 특수한 형태의 method
 3. 특수한 상황에서 그에 맞는 magic function이 호출됩니다. !!


"""

# class Student(object):
#     def __init__(self, name, dept):     #생성자, constructor, initializer
#         self.name = name
#         self.dept = dept
#         print("{}학과 {} 학생이 생성되었습니다.".format(self.dept, self.name))
#
#     def __del__(self):
#         print("소멸자가 호출되었어요!")
#
# stu1 = Student("홍길동", "심리")
# # print(type(stu1))   # <class '__main__.Student'>
# print(stu1)
# print(stu1)
# del stu1        #객체를 메모리에서 삭제해요!! __del__호출되요!
#print(stu1)     #NameError: name 'stu1' is not defined
# ############################################################################
#
# a = 100
# print(type(a))      #<class 'int'>
#
# class MyInt(int):       # 숫자 assign을 이용해서 매번 숫자나 문자를 이용하여 class를 호출하여 사용해야하나 자주사용하기 때문에 사용하지 않음
#     pass
#
# my_num = MyInt(100)     # 정수객체 생성
# print(my_num + 200)     # 300
# print(my_num.__add__(200))
#
# class Student(object):
#     def __init__(self, name, dept):
#         self.name = name
#         self.dept = dept
#         print("{}학과 {}학생이 생성되었습니다.".format(self.dept, self.name))
#     def __repr__(self):
#         return self.name
#
#
# stu2 = Student("홍길동", "심리")
# print(stu2) # instance의 class정보와 저장되어 있는 메모리 주소가 출력
#             # <__main__.Student object at 0x7fef081d2c50>
#
#
# class Car(object):
#     def __init__(self, model, price):
#         self.model = model
#         self.price = price
#
#     def __lt__(self, other):        #self = car1 / other = car2
#         if self.price < other.price:
#             return "{}가격이 더 낮아요!!".format(self.model)
#         else:
#             return "{}가격이 더 높아요!!".format(self.model)
#
#
#
# car1 =Car("G70", 5000)
# car2 =Car("Sonata", 3000)
#
# print(car1.price < car2.price)      #False
# print(car1 < car2)      # __lt___ 적용 전 // TypeError: '<' not supported between instances of 'Car' and 'Car'
#                         # __lt___ 적용 후 // G70가격이 더 높아요!!
                          # less than
############################################################################################################



