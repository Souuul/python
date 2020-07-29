# 제어문
# python의 입출력!
# 입력을 받고 싶어요!
# console 입력을 받으려면 input()을 이용하면 되요!

# my_input = input("입력값을 넣으세요!! : ") #1
# print(type(my_input)) # <class 'str'> 문자열로 변경하여 입력됨
# print(my_input) # 1

# 기본적으로 print() 함수는 한줄을 출력한 후 line feed(줄바꿈)를 수행
# 줄바꿈 대신 다른 문자를 출력하려면 'end' 속성을 이용

# my_input = input("입력값을 넣으세요!! : ") #1
# print(type(my_input), end="-") # <class 'str'> 문자열로 변경하여 입력됨
# print(my_input) # <class 'str'>-1

#Control Statement (제어문)
# 1. if문
# python의 조건문(if)은 두가지 방식으로 사용이 가능
# 전통적인 if~elif~else 구문이 있어요

# a = 15
# if a%3 ==0:
#     print('3의 배수입니다.') #3의 배수입니다.
# elif a%5 ==0:
#     print('5의 배수입니다.')
# else:
#     print('3의 배수도 5의 배수도 아닙니다.')
#
# if a%3 ==0:
#     pass # 아무것도안할경우 코드블럭에서 아무작업도 지시하지 않는경우 키워드로 해결

# in을 이용한 구문이 있어요!
# my_list = ["서울", "인천", "부산"]
#
# if "수원" in my_list:
#     pass
# else:
#     print("수원은 지역안에 없어요!") #수원은 지역안에 없어요!

##############################################

# for문 > 반복문
# for문은 두가지 형태로 사용을 해요!
# for ~ in range()   > 반복횟수를 지정할 경우
# for ~ in list, tuple, dict, .... > 가지고 있는 데이터 만큼 반복할 경우

#1 부터 100까지의 합을 구해보아요!!
# my_sum = 0
# for tmp in range(1, 101, 1):
#     my_sum += tmp
# print("누적값은 : {}".format(my_sum)) #누적값은 : 5050

# 집합자료형을 이용해서 for문을 수행
# my_list = ["서울", "인천", "부산"]
# for tmp in my_list:
#     print(tmp)
# #서울
# #인천
# #부산
#
# # tuple관련 예
# total = 0
# my_data = [(1, 2), (3, 4), (5, 6)]
# for (tmp1, tmp2) in my_data:
#     total += (tmp1 + tmp2)
# print(total) #21

###########################################
# python은 특이하게 list comprehension이라는게 있어요!
# 하나의 자료형으로 다른 list를 쉽게 생성하는 방법 중 하나에요!

# myList = [1, 2, 3, 4, 5]
# #goal = [2, 4, 6, 8, 10]
#
# goal = [] # goal
# for tmp in myList:
#     goal.append(tmp*2)
# print(goal) #[2, 4, 6, 8, 10]


# myList = [1, 2, 3, 4, 5]
# goal = [tmp * 2 for tmp in myList]
# print (goal)

#짝수만 뽑으려면
# myList = [1, 2, 3, 4, 5]
# goal = [tmp for tmp in myList if tmp%2 == 0] #if 문이 참일경우의 값만 사용
# print (goal) #[2, 4]

#################################################


# while

# idx = 0
# while  idx < 10:
#     print("현재 idx의 값은 : {}".format(idx)) # // 현재 idx의 값은 : 0 ~ 9
#     idx += 1 # 단조증가(++) 단조감소(--) 쓸수 없음

# 문제 1.
# 10보다 작은 자연수 중에서 3 또는 5의 배수는?
# 3, 5, 6, 9가 존재해요 이것들의 합은 23입니다.
### 1000보다 작은 자연수 중에 3 또는 5의 배수들을 구해서 모두 합하면 얼마인가요?

total1 = 0
for x in range(1000):
    if x%3 == 0:
        total1 += x
    elif x%5 == 0:
        total1 += x
print("1000보다 작은 자연수 중에 3 또는 5의 배수들을 구해서 모두 합하면 {} 입니다.".format(total1))
#1000보다 작은 자연수 중에 3 또는 5의 배수들을 구해서 모두 합하면 : 233168 입니다.


# 문제 2.
# 피보나치 수열의 문제 1,2,3,5 ... 앞에항 2개를 더한 것이 다음숫자
### 짝수면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

my_list=[1,2]
total2 = 0
final_number = 0
y=0
while final_number <= 4000000:
        final_number = my_list[y]+my_list[y+1]
        my_list.append(final_number)
        y += 1

for z in my_list:
    if z%2==0:
        total2 += z
print(total2) #4613732


# 문제 3.
# 문자열에서 가장많이 사용된 문자는 무엇인가요 ? 동률일 경우 알파벳 순으로 앞에있는 문자를 출력하세요
my_str1 = "This is a sample Program mississippi river"
my_str2 = "abcdabcdababccddcd"
#alpha_list = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
#alpha_list.sort()               #a,b,c,d,e,f순으로 배열
from string import ascii_lowercase  #알파벳 리스트
alpha_list = list(ascii_lowercase)

my_str1 = my_str1.lower()       #소문자로 변환
my_str2 = my_str2.lower()       #소문자로 변환
my_list1 = [0,0]
my_list2 = [0,0]
my_list3 = [0,0]
my_list4 = [0,0]

for h in alpha_list:
    my_list1 = [h, my_str1.count(h)]
    if my_list1[1] > my_list2[1]:   #어차피 a 부터 검사하기 떄문에 필요없음
        my_list2 = my_list1
print("제일많이 나온 알파벳은 {} 이고 개수는 {} 개입니다.".format(my_list2[0], my_list2[1]))
#제일 많이 나온 알파벳은 i 이고 개수는 7 개입니다.

for h in alpha_list:
    my_list3 = [h, my_str2.count(h)]
    if my_list3[1] > my_list4[1]:
        my_list4 = my_list3
print("제일많이 나온 알파벳은 {} 이고 개수는 {} 개입니다.".format(my_list4[0], my_list4[1]))
#제일 많이 나온 알파벳은 c 이고 개수는 5 개입니다.
