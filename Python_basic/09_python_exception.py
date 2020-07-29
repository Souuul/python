'''
exception
Error - compile time error : 문법오류
        runtime error : 실행시 발생하는 오류
어떤 runtime error 들은 비정상 종료되지 않고 프로그램을 지속적으로 수행시킬수 있는 방법이 있어요!
exception 처리는 하나의 구문 밖에 없어요!!

try~
except
else
finally
'''

def my_func(my_list):

    total_sum = 0       # list안의 숫자들을 누적해요!

    try:
        total_sum = my_list[0] + my_list[1] + my_list[2]

    except Exception:               # 발생할 수 있는 모든오류
        print("오류가 존재합니다.")     # 예외처리를 해야 해요!

    else:                           # except에 걸리지 않았을 경우
        print("오류가 없어요!!")

    finally:                        #오류가 있던 없던 무조건 수행
        print("무조건 수행되요!")

my_list1 = [1, 2]
my_list2 = [1, 2, 3]

my_func(my_list1)
'''
오류가 존재합니다.
무조건 수행되요!
'''
my_func(my_list2)
'''
오류가 없어요!!
무조건 수행되요!
'''

