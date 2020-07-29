# 문제 1.
# 10보다 작은 자연수 중에서 3 또는 5의 배수는?
# 3, 5, 6, 9가 존재해요 이것들의 합은 23입니다.
### 1000보다 작은 자연수 중에 3 또는 5의 배수들을 구해서 모두 합하면 얼마인가요?

# total1 = 0
# for x in range(1000):
#     if x%3 == 0:
#         total1 += x
#     elif x%5 == 0:
#         total1 += x
# print("1000보다 작은 자연수 중에 3 또는 5의 배수들을 구해서 모두 합하면 {} 입니다.".format(total1))
# #1000보다 작은 자연수 중에 3 또는 5의 배수들을 구해서 모두 합하면 : 233168 입니다.
#
#
# # 문제 2.
# # 피보나치 수열의 문제 1,2,3,5 ... 앞에항 2개를 더한 것이 다음숫자
# ### 짝수면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?
#
# my_list=[1,2]
# total2 = 0
# final_number = 0
# y=0
# while final_number <= 4000000:
#         final_number = my_list[y]+my_list[y+1]
#         my_list.append(final_number)
#         y += 1
#
# for z in my_list:
#     if z%2==0:
#         total2 += z
# print(total2) #4613732
#
#
# # 문제 3.
# # 문자열에서 가장많이 사용된 문자는 무엇인가요 ? 동률일 경우 알파벳 순으로 앞에있는 문자를 출력하세요
# my_str1 = "This is a sample Program mississippi river"
# my_str2 = "abcdabcdababccddcd"
# #alpha_list = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
# #alpha_list.sort()               #a,b,c,d,e,f순으로 배열
# from string import ascii_lowercase  #알파벳 리스트
# alpha_list = list(ascii_lowercase)
#
# my_str1 = my_str1.lower()       #소문자로 변환
# my_str2 = my_str2.lower()       #소문자로 변환
# my_list1 = [0,0]
# my_list2 = [0,0]
# my_list3 = [0,0]
# my_list4 = [0,0]
#
# for h in alpha_list:
#     my_list1 = [h, my_str1.count(h)]
#     if my_list1[1] > my_list2[1]:   #어차피 a 부터 검사하기 떄문에 필요없음
#         my_list2 = my_list1
# print("제일많이 나온 알파벳은 {} 이고 개수는 {} 개입니다.".format(my_list2[0], my_list2[1]))
# #제일 많이 나온 알파벳은 i 이고 개수는 7 개입니다.
#
# for h in alpha_list:
#     my_list3 = [h, my_str2.count(h)]
#     if my_list3[1] > my_list4[1]:
#         my_list4 = my_list3
# print("제일많이 나온 알파벳은 {} 이고 개수는 {} 개입니다.".format(my_list4[0], my_list4[1]))
# #제일 많이 나온 알파벳은 c 이고 개수는 5 개입니다.


## 문제 4.
# 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
# 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
# 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수를 구하세요




# def Palindrome_check(str):
#     for i in range(len(str)//2):
#         if str[i] != str[len(str)-1-i]:
#             return False
#     return True
#
# answer_4 = []
#
# for x in range(100, 1000, 1):
#     for y in range(100, 1000, 1):
#         z = str(x * y)
#         if Palindrome_check(z):
#             answer_4.append(z)
# answer_4.sort()
# print(answer_4[-1])



################################################

## 문제 5.
## 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

## 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까? # 최소공배수
################################################################


# def gcd(a, b):
#     if a % b == 0: return b
#     else: return gcd(b, a%b)
#
# def lcd(a, b):
#     return (a*b) // gcd(max(a, b), min(a, b))
#
# def solution(arr):
#     answer = 1
#     for num in arr:
#         answer = lcd(answer, num)
#     return answer
#
# number_list = []
# for i in range(1,21):
#     number_list.append(i)
#
# print(solution(number_list))


## 문제 4.
## 로또 프로그램 작성
## 5000원으로 로또복권을 5장 자동으로 구매합니다.
## 이번 주 로또 당첨번호를 생성하여 로또 당첨을 확인하세요!
## 쉬운버전으로 먼저 작성합니다.
## 6숫자가 다 맞으면 1등, 5개 맞으면 2등으로 처리합니다.
## 즉, 쉬운버전은 보너스 숫자는 없는 것으로 간주합니다.
## 쉬운버전을 해결했다면

# 로또 5장 자동 구매
# import random
# # i = random.randint(1, 46)  # 1부터 46 까지의 랜덤한 숫자
#
# ##### class도 사용가능 !! 함수를 묶어사용 가능
#
# def p_4_1():          # 로또 번호를 호출하는 함수
#     x = []
#     while len(set(x)) < 6:
#         i = random.randint(1, 46)
#         x.append(i)
#         x = set(x)
#         x = list(x)
#     return x
#
# def p_4_2(a, b):      # 당첨을 확인하는 함수
#     tmp = 0
#     win = ""
#     for i in range(6):
#         for j in range(6):
#             if a[i] == b[j]:
#                 tmp += 1
#     if tmp == 6:
#         win = "1등"
#     elif tmp == 5:
#         win = "2등"
#     elif tmp == 4:
#         win = "3등"
#     elif tmp == 3:
#         win = "4등"
#     else:
#         win = "꽝"
#
#     return win

############################# 로또 당첨 개수구하기
#a = p_4_1() # 당첨숫자
# print("당첨숫자는 : {}".format(a))
# y = []
# for _ in range(5):
#     num_try = p_4_1()
#     print("뽑은숫자는 : {}".format(num_try))
#     y.append(p_4_2(a, num_try))
#
# print("결과는 {}".format(y))
# my_list = ["1등", "2등", "3등", "4등", "꽝"]
#
# for x in my_list :
#     print("당첨결과는 {} : {}개".format(x, y.count(x)))

########################### 1등하기 위해 쓴 돈 ( IDEA !!! ROI 산출가능 투자대비 당첨금까지 확장가능)
# def p_4_3(place):
#     a = p_4_1()
#     my_money = 0
#     win = ""
#     while win != place:
#         num_try = p_4_1()
#         win = p_4_2(a, num_try)
#         my_money += 1000
#     return print("{} 하기위해 쓴돈은 {}원입니다.".format(place,my_money))
# print("n등하기 위하여 투자한 돈을 적으세요 ex) 1등, 2등, 3등, 4등, 꽝")
# place = input("입력:")
# p_4_3(place)



## 보너스 숫자를 이용하여 로또 당첨을 확인합니다. ## 마지막 뽑은숫자를 보너스 숫자라고 가정하고 and를 이용하여 1등 2등 3등처리가능!!!!
## 보너스 숫자를 제외한 모든 숫자가 다 맞으면 1등,
## 보너스 숫자를 포함하여 6개의 숫자가 맞으면 2등,
## 보너스를 제외하고 5개의 숫자가 맞으면 3등으로 처리합니다.

## 쉬운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개,
## 4등 몇개, 꽝 몇개로 출력
## 어려운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개,
## 4등 몇개, 5등 몇개, 꽝 몇개로 출력

## 랜덤값을 도출하기 위해서는 다음의 코드를 이용한다.
# import random
# i = random.randint(1, 100)  # 1부터 100 사이의 임의의 정수
# f = random.random()  # 0부터 1 사이의 임의의 float
# i = random.randrange(1, 101, 2)  # 1부터 100 사이의 임의의 짝수
# i = random.randrange(10)  # 0부터 9 사이의 임의의 정수

##### 추가문제
##### 1등에 당첨될려면 평균적으로 얼마만큼의 돈을 투자해야 할까요?   !! 확률문제 (1등은 한번만가능하고 경우의숫자에 곱하기 1000원을 해야함!)
##### 로또 1게임은 1000원입니다.

# 1등 로또 당첨될 확률  ===  1 / 45C6
# 45 44 43 42 41 40
# jj = 1
# for kk in range(40, 46):
#     jj *= kk
# average_1st = jj*1000
# print("1등을 당첨되기 위한 평균 금액은 {}".format(average_1st))



## 문제 8.
## 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다 (제곱의 합).
## 1**2 + 2**2 + ... + 10**2 = 385

## 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다 (합의 제곱).
## (1 + 2 + ... + 10)**2 = 552 = 3025

## 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의
## 차이는 3025 - 385 = 2640 이 됩니다.

## 그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는
## 얼마입니까?
# double_sum = sum_double = 0
# for i in range(101):
#     double_sum += i**2
# for j in range(101):
#     sum_double += j
#
# answer_8= sum_double**2 - double_sum
# print(answer_8) #25164150



## 문제 9.
## 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
## 이 때 10,001번째의 소수를 구하세요. # 1과 자기자신으로만 나눠지는


# n=10000000 #  에라토스테네스 채
# a = [False,False] + [True]*(n-1)
# primes=[]
#
# for i in range(2,n+1):
#   if a[i]:
#     primes.append(i)
#     for j in range(2*i, n+1, i):
#         a[j] = False
# print(primes[10000])



# ######
# n = 10000
# d=[]
# for i in range(2, n+1):
#     c=0
#     for j in range(2,i):
#         if i%j==0:
#             c=1
#     if c == 0:
#         d.append(i)
# print(d[1000])




## 문제 10.
## 세 자연수 a, b, c 가 피타고라스 정리 a**2 + b**2 = c**2 를 만족하면
## 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
## 예를 들면 3**2 + 4**2 = 9 + 16 = 25 = 5**2이므로
## 3, 4, 5는 피타고라스 수입니다.

## a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다.
## 이 때, a × b × c 는 얼마입니까?

# answer = [a*b*c for a in range(333) for b in range(a+1,500) for c in range(b+1, 500) if a**2 + b**2 == c**2 and a+b+c == 1000]
# print(answer[0]) #31875000


## 문제 11.
## 양의 정수 n에 대하여, 다음과 같은 계산 과정을 반복하기로 합니다.

## n → n / 2 (n이 짝수일 때)
## n → 3 * n + 1 (n이 홀수일 때)

## 13에 대하여 위의 규칙을 적용해보면 아래처럼 10번의 과정을 통해 1이 됩니다.

## 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

## 아직 증명은 되지 않았지만, 이런 과정을 거치면 어떤 수로 시작해도
## 마지막에는 1로 끝나리라 생각됩니다.
## (이런 수들을 우박수 hailstone sequence라 합니다.)

## 그러면, 백만(1,000,000) 이하의 수로 시작했을 때 1까지 도달하는데
## 가장 긴 과정을 거치는 숫자는 얼마입니까?
## 계산 과정 도중에는 숫자가 백만을 넘어가도 괜찮습니다.

#
# def hailstone_sequence(n):
#     tmp = 0
#     while n > 1:
#         if n % 2 ==0:
#             n = n/2
#         else:
#             n = 3*n +1
#         tmp += 1
#     return tmp
#
# my_list = []
# for n in range (1, 1000001):
#     my_list.append([n,hailstone_sequence(n)])
#
# my_list.sort(reverse=True, key=lambda x:x[1])
# print(my_list[0])       #[837799, 524]


## 문제 12.
## 다음과 같은 특성을 갖는 숫자의 개수를 찾는 기능을 구현합니다.
## 입력으로 두개의 숫자( x, y )를 이용합니다.
## - 두 개의 숫자 x와 y를 이용하여,
##   x초과 y미만의 숫자 중 각 자리의 숫자를 모두 더한 값이 5의 배수가
##   되는 숫자를 찾습니다.
## - 숫자들을 모두 찾은 후 해당 숫자가 총 몇 개인지를 출력합니다.

## 예1) 두 개의 숫자 1과 100이 주어졌을 경우,
##      1초과 100미만의 숫자 중 각 자리의 숫자를 모두 더한 값이 5의 배수가
##      되는 숫자를 찾습니다.
##      - 20의 경우 각 자리 숫자를 모두 더한 값이 2이므로, 적합하지 않다.
##      - 23의 경우 각 자리 숫자를 모두 더한 값이 5이므로, 적합하다.
##      [총 개수] 19

## 예2) 두 개의 숫자 5와 500이 주어졌을 경우,
##      5초과 500미만의 숫자 중 각 자리의 숫자를 모두 더한 값이 5의 배수가
##      되는 숫자를 찾습니다.
##      [총 개수] 98

## 입력으로 주어지는 두 개의 수 : 100 10000
# a = int(input("첫번째 수를 입력하세요"))
# b = int(input("두번째 수를 입력하세요"))
# my_list12 = []
# my_str12 = ""
# for i in range(a+1, b):
#     my_str12 = str(i)
#     sum_digit = 0
#     for x in my_str12:
#         sum_digit += int(x)
#     if sum_digit % 5 == 0:
#         my_list12.append(sum_digit)
# print("{}초과 {}미만의 숫자중 각 자리의 숫자를 모두 더한 값이 5의 배수가 되는 숫자를 찾습니다.".format(a, b))
# print("[총 개수] {}".format(len(my_list12)))







## 문제 13.
## 6자리 이상 9자리 미만의 수를 입력으로 사용합니다.

## 수의 중앙을 기준으로 두 개의 수로 분리한 후 큰 수를 선택한다.
## - 수의 숫자개수가 홀수 개인 경우 수의 중앙 숫자를 기준으로
##   왼쪽과 오른쪽 수로 분리
## - 수의 숫자개수가 짝수 개인 경우 수를 반으로 나누어
##   왼쪽과 오른쪽 수로 분리
## 예1) 1234567 -> (123, 567) -> (567)
## 예2) 34217869 -> (3421, 7869) ->(7869)

## 입력으로 제공된 수를 더 이상 두 개의 수로 분리할 수 없을 때까지
## 과정을 반복하여 남은 최종 숫자를 구해 출력한다.
## 예1) 567 -> (5, 7) -> (7)
## 예2) 7869 -> (78, 69) -> (78) -> (7, 8) -> (8)

# def p_13(answer):
#     while len(str(answer)) > 1:
#         c = int(str(answer)[:len(str(answer)) // 2])
#         d = int(str(answer)[-(len(str(answer)) // 2):])
#         if c > d:
#             answer = c
#         else:
#             answer = d
#     return answer
#
# print(p_13(1002))



## 문제 14.
## 2**15 = 32768 의 각 자리수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.

## 2**1000의 각 자리수를 모두 더하면 얼마입니까?


# def p_14(x):
#     answer_14 = 0
#     for i in str(x):
#         answer_14 += int(i)
#
#     return answer_14
# print(p_14(2**1000)) # 1366


## 문제 15.
## 각 부품의 생산정보가 문자열로 제공된다.
## [부품생산정보] : A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8

## 각 부품정보는 부품명과 품질데이터로 구성된다.
## - A,B,C 3개의 부품이 있으며 품질은 1이상 10미만의 정수.
##   예) A7 : A부품, 품질 7

## 생산정보에서 품질이 7이상인 부품만을 순서대로 선택한다.
## [생산정보] A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8
## [품질이 7이상인 부품 목록] A7A8B9A8B9C7C7B9A7B8C9A8

## 품질이 7이상인 부품들을 조립해 완성품을 만든다.
## A, B, C 세 부품이 순서대로 있을 때만 부품을 조립한다.
## A7A8B9A8B9C7C7B9A7B8C9A8 => A8B9C7, A7B8C9 2개 조립
## 조립한 부품의 목록과 전체 조립한 개수를 출력

# ass_str = "A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8"
# ass_list = []
# for n in range(0, len(ass_str)//2):
#     i = ass_str[2*n : 2*(n+1)]
#     if int(i[1]) >= 7:
#         ass_list.append(i)
#
#
# answer_15 = 0
# for n in range(-2 + len(ass_list)):
#     if ass_list[n][0] == "A" and ass_list[n+1][0] == "B" and ass_list[n+2][0] == "C":
#         print("조립 리스트 {} {} {}".format(ass_list[n],ass_list[n+1],ass_list[n+2]))
#         answer_15 += 1
# print("총 조립개수는 {}개 입니다. ".format(answer_15))        # 2
# '''
# 조립 리스트 A8 B9 C7
# 조립 리스트 A7 B8 C9
# 총 조립개수는 2개 입니다.
# '''


## 문제 16.
## n! 이라는 표기법은 n × (n − 1) × ... × 3 × 2 × 1을 뜻합니다.

## 예를 들자면 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 이 되는데,
## 여기서 10!의 각 자리수를 더해 보면 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 입니다.

## 100! 의 자리수를 모두 더하면 얼마입니까?

# def factorial_func(n):
#     w = 1
#     for k in range(1, n+1):
#         w *= k
#     return w
#
#
# def p_16(x):
#     answer_16 = 0
#     for i in str(x):
#         answer_16 += int(i)
#     return answer_16
#
# print(p_16(factorial_func(100))) #648


## 문제 17.
## 최소 10개 이상 최대 20개 이하의 숫자로 구성된 숫자목록이 배열 혹은 리스트 형태로 제공된다.
## 숫자목록 : 1,3,4,5,7,9,2,3,4,7

## 아래의 순서로 숫자목록의 숫자를 교환하여 재배치한다.
## 1) 숫자목록의 앞에서부터 4개의 숫자를 선택한다.
##    목록에서 숫자 선택 : [1,3,4,5],7,9,2,3,4,7
## 2) 선택된 4개의 숫자의 합을 구한다.
##    4개의 숫자 합 : [1,3,4,5],7,9,2,3,4,7 => 13
## 3) 첫 번째와 두 번째 숫자를 교환하고 세 번째와 네 번째 숫자를 교환한다.
##    숫자 교환 : [3,1,5,4],7,9,2,3,4,7
## 4) 오른쪽으로 한칸씩 이동하여 순서대로 1,2,3번 과정을 반복해 숫자목록의 숫자를 재배치한다.
## 예) [1,3,4,5],7,9,2,3,4,7 =>
##     [3,1,5,4],7,9,2,3,4,7 =>
##     3,[1,5,4,7],9,2,3,4,7 -> …

## 맨 마지막까지 도달했을 때 선택된 4개의 숫자의 합이 가장 큰 값과 그 때의 숫자목록을 출력


# def p_17(num_list):
#
#     num_list = num_list.split(" ")
#     max_add = []
#     a = b = c = d = tmp = 0
#
#     for n in range(-3 + len(num_list)):
#         a = num_list[n]
#         b = num_list[n+1]
#         c = num_list[n+2]
#         d = num_list[n+3]
#
#         num_list[n] = b
#         num_list[n+1] = a
#         num_list[n+2] = d
#         num_list[n+3] = c
#
#         tmp +=1
#         max_add.append([tmp,[b,a,d,c],int(a)+int(b)+int(c)+int(d)])
#     max_add.sort(reverse=True, key=lambda x:x[2])
#
#     returnmax_add
#
# my_list = input("초기데이터를 입력해주세요")
# max_add = p_17(my_list)
# print("[{}번째 선택되는 4개의 숫자] : {}".format(max_add[0][0], max_add[0][1]))
# print("선택된 4개의 수의 최대 합 : {}".format(max_add[0][2]))


## [초기 입력 데이터]
## 1 3 4 5 7 9 2 3 4 7
## ---------------------------------------------------------------
## [5번째 선택되는 4개의 숫자]: 2 1 3 4
## ---------------------------------------------------------------
## [선택된 4개의 수의 최대 합]: 21


## [초기 입력 데이터]
## 10 15 3 5 9 5 7 8 9 15 44 54 15 67 32 25 48 98 44 56
## ---------------------------------------------------------------
## [7번째 선택되는 4개의 숫자]: 9 10 15 3
## ---------------------------------------------------------------
## [선택된 4개의 수의 최대 합]: 159
## ---------------------------------------------------------------


## 문제 18.
## 어떤 대상을 순서에 따라 배열한 것을 순열이라고 합니다.
## 예를 들어 3124는 숫자 1, 2, 3, 4로 만들 수 있는 순열 중 하나입니다.

## 이렇게 만들 수 있는 모든 순열을 숫자나 문자 순으로 늘어놓은 것을
## 사전식(lexicographic) 순서라고 합니다.

## 0, 1, 2로 만들 수 있는 사전식 순열은 다음과 같습니다.
## 012   021   102   120   201   210


## 0, 1, 2, 3, 4, 5, 6, 7, 8, 9로 만들 수 있는 사전식 순열에서
## 1,000,000번째는 무엇입니까?

# from itertools import combinations, permutations
#
# items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = []
# for i in items:
#     x.append(str(i))
#
# answer_18 = list(map(''.join, permutations(x, 10)))
# print(answer_18[1000000-1]) #2783915460



# print(list(map(''.join, combinations(x, 2))))




## 문제 19.
## 입력으로 제공되는 숫자열에서 짝수와 홀수를 추출하여 새로운 숫자열을 생성한다.
## 1) 입력된 숫자열에서 짝수와 홀수를 순서대로 추출한다.
##    [입력] 78235169
##    [짝수 추출] 826
##    [홀수 추출] 73519
## 2) 추출된 짝수의 뒤에 추출된 홀수를 연결하여 새로운 숫자열을 생성한다.
##    [짝수와 홀수 연결] 82673519

## 결과숫자열을 앞에서부터 순서대로 뺄셈 연산 또는 덧셈 연산 한다.
## 숫자열의 앞에서 부터 순서대로 뺄셈 연산한다.
## 단, 앞선 연산 결과가 0 이하이면 그 차례에는 덧셈 연산한다.
## [결과 숫자열] 82673519
## [각 수의 연산 순서와 방법]
##   8 - 2 = 6
##   6 – 6 = 0
##   0 + 7 = 7 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
##   7 – 3 = 4
##   4 – 5 = -1
##  -1 + 1 = 0 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
##   0 + 9 = 9 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
## [연산 결과] 9

## [입력]: 78235169
## [출력]: 9

## [입력]: 693756874
## [출력]: 7




# def p_19(my_number):
#     my_str = str(my_number)
#     even_extract = ""
#     odd_extract = ""
#
#     for i in my_str:
#         if int(i) % 2 == 0:
#             even_extract = even_extract + i
#         else:
#             odd_extract = odd_extract + i
#
#     new_num = even_extract + odd_extract
#     answer_19 = int(new_num[0]) * 2
#     for x in new_num:
#         if answer_19 <= 0:
#             answer_19 = answer_19 + int(x)
#         else:
#             answer_19 = answer_19 - int(x)
#     return answer_19
#
# my_number = input("숫자를 입력해주세요")
# print("[입력]: {}".format(my_number))
# print("[출력]: {}".format(p_19(my_number)))