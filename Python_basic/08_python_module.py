'''
module
python에서 module은 함수나 변수 또는 클래스를 모아놓은 파일을 지칭
다른 python파일에서 불러와서 사용할 수 있어요!


module을 사용하는 이유는 코드의 재사용성과 관리목적

python 모듈은 크게 2가지가 있어요!!
- C언어로 구성된 binary module
- python 언어로 구현된 일반 module !!

module을 사용하기 위해서 사용하는 keyword : import  # 해당모듈을 객체화시켜서 해당 namespace로 끌어오는 역할
module도 파이썬 입장에서는 객체로 관리되요!!

'''
# import sys
# print(sys.path) # list
#
# sys.path.append("/Users/admin/PycharmProjects/Python_basic")        #module을 저장할 폴더를 지정
#
# #sys.path.append("/Users/admin/PycharmProjects/Python_basic/module1.py")
# # module을 하나 만들어보아요(python_module)
# # module을 만들었으니 가져다가 사용해 보아요!
#
# # 가장 기본적인 import 기능을 사용하는 방법
# import module1 as m1 # m1으로 별명을 지어줌
# print(m1.my_pi)     #3.1415926535 // module1으로는 호출 불가능 !! m1으로 변경하였기 때문에
# print(m1.my_adder(10,20))       # 30


# from module1 import my_adder  # from 모듈 import (함수 , 변수 etc...)
# print(my_adder(10,20))        # 30


# from module1 import *    # * 모듈안의 모든것을 다 받아올 수 있음 * (모든 것의 의미)
# print(my_adder(10,20))   # 30

# /Users/admin/PycharmProjects/Python_basic 안에 module1.py를 저장해 놨어요!!
# 모듈을 관리할때 계층별 폴더를 관리를 할수 있어요!!
# 하위폴더를 만들면서 자료를 정리할 수 있어요!!
# /Users/admin/PycharmProjects/Python_basic/test_module/module1.py 로 다시 저장해요!



#  패키지 !!
import test_module.module1
print(test_module.module1.my_adder(10,20)) # 30

import test_module.module1 as my_module1
print(my_module1.my_adder(10,20)) # 30

