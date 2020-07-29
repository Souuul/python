# # 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
# # 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.
#
# # manufacturer,model,displ,year,cyl,trans,drv,cty,hwy,fl,class
#

# # filter 함수 이용
# def filter_displ_4_lower(tmp):
#     return tmp.displ <= 4
#
# def filter_displ_5_uppder(tmp):
#     return tmp.displ >= 5





# class Mpg(object):
#     def __init__(self, manufacturer, model, displ, year, cyl, trans, drv, cty, hwy, fl, class_1):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.displ = float(displ)
#         self.year = int(year)
#         self.cyl = float(cyl)
#         self.trans = trans
#         self.drv = drv
#         self.cty =float(cty)
#         self.hwy = float(hwy)
#         self.fl = fl
#         self.class_1 = class_1
#
#
#     def __repr__(self):
#         return self.hwy
#
# hwy_4 = 0
# tmp_4 = 0
# hwy_5 = 0
# tmp_5 = 0
# file1 = open("/Users/admin/PycharmProjects/Python_basic/mpg.txt", "r", encoding='euc-kr') # 맥
# mpg_list = list()
# while True:
#     line = file1.readline()
#     if not line:
#         break
#     x = line[:-1]
#     mpg_data = x.split(',')
#     if float(mpg_data[2]) <=4:
#         hwy_4 += float(mpg_data[8]) #
#         tmp_4 += 1
#
#     elif float(mpg_data[2]) >=5:
#         hwy_5 += float(mpg_data[8])
#         tmp_5 += 1
#
#
# everage_displ4 = hwy_4/tmp_4
# everage_displ6 = hwy_5/tmp_5
#
# if everage_displ4 > everage_displ6:
#     print("배기량이 4 이하인 자동차의 고속도로 연비는 배기량인 5이하인 자동차의 고속도로 연비보다 높습니다.")
# else:
#     print("배기량이 5 이인 자동차의 고속도로 연비는 배기량인 4이하인 자동차의 고속도로 연비보다 높습니다.")

#


# # 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# # "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# # 평균적으로 더 높은지 확인하세요.
#
#
# audi_cty = 0
# number_of_audi = 0
# toyota_cty = 0
# number_of_toyata = 0
#
# file1 = open("/Users/admin/PycharmProjects/Python_basic/mpg.txt", "r", encoding='euc-kr') # 맥
# mpg_list = list()
# while True:
#     line = file1.readline()
#     if not line:
#         break
#     x = line[:-1]
#     mpg_data = x.split(',')
#
#     if mpg_data[0] == "audi":
#         audi_cty += float(mpg_data[7])
#         number_of_audi += 1
#
#     elif mpg_data[0] == "toyota":
#         toyota_cty += float(mpg_data[7])
#         number_of_toyata += 1
#
# #    mpg_list.append(Mpg(mpg_data[0], mpg_data[1], mpg_data[2], mpg_data[3], int(mpg_data[4]), mpg_data[5], mpg_data[6], mpg_data[7], int(mpg_data[8]), mpg_data[9], mpg_data[10])) # \n이 처리가됨
# file1.close()
#
#
# everage_audi_cty = audi_cty/number_of_audi
# everage_toyota_cty = toyota_cty/number_of_toyata
#
#
# if everage_audi_cty > everage_toyota_cty:
#     print("audi의 도시연비가 toyota의 도시연비보다 높다")
# else:
#     print("toyota의 도시연비가 audi의 도시연비보다 높다")
#
#
#
#
# # 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다.
# # 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.
#
# hwy_41 = 0
# tmp_41 = 0
# hwy_51 = 0
# tmp_51 = 0
# hwy_61 = 0
# tmp_61 = 0
#
# file1 = open("/Users/admin/PycharmProjects/Python_basic/mpg.txt", "r", encoding='euc-kr') # 맥
# mpg_list = list()
# while True:
#     line = file1.readline()
#     if not line:
#         break
#     x = line[:-1]
#     mpg_data = x.split(',')
#     if mpg_data[0] == "chevrolet":
#         hwy_41 += float(mpg_data[8])
#         tmp_41 += 1
#
#     elif mpg_data[0] == "ford":
#         hwy_51 += float(mpg_data[8])
#         tmp_51 += 1
#
#     elif mpg_data[0] == "honda":
#         hwy_61 += float(mpg_data[8])
#         tmp_61 += 1
#
#
# #    mpg_list.append(Mpg(mpg_data[0], mpg_data[1], mpg_data[2], mpg_data[3], int(mpg_data[4]), mpg_data[5], mpg_data[6], mpg_data[7], int(mpg_data[8]), mpg_data[9], mpg_data[10])) # \n이 처리가됨
# file1.close()
#
# everage_chevrolet = hwy_41/tmp_41
# everage_ford = hwy_51/tmp_51
# everage_honda = hwy_51/tmp_51
#
# print("chevrolet의 평균연비는 : {} , ford의 평균연비는 {} ,honda의 평균연비는 {}".format(round(everage_chevrolet),round(everage_ford),round(everage_ford)))
#
#
# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요.



# class Mpg(object):
#     def __init__(self, manufacturer, model, displ, year, cyl, trans, drv, cty, hwy, fl, class_1):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.displ = displ
#         self.year = year
#         self.cyl = cyl
#         self.trans = trans
#         self.drv = drv
#         self.cty =cty
#         self.hwy = hwy
#         self.fl = fl
#         self.class_1 = class_1
#
#
#     def __repr__(self):
#         return "{} {} {} {}".format(self.manufacturer, self.model, self.year, self.hwy)
#
#
# file1 = open("/Users/admin/PycharmProjects/Python_basic/mpg.txt", "r", encoding='euc-kr') # 맥
# mpg_list = list()
# while True:
#     line = file1.readline()
#     if not line:
#         break
#     x = line[:-1]
#     mpg_data = x.split(',')
#     if mpg_data[0] == "audi":
#         mpg_list.append(Mpg(mpg_data[0], mpg_data[1], mpg_data[2], mpg_data[3], int(mpg_data[4]), mpg_data[5], mpg_data[6], mpg_data[7], int(mpg_data[8]), mpg_data[9], mpg_data[10])) # \n이 처리가됨
#
# file1.close()
# result = reversed(sorted(mpg_list, key=lambda Mpg: Mpg.hwy))
#
# print("3번문제")
# idx = 1
# for tmp in result:
#     print("{}등 {}".format(idx, tmp))
#     idx += 1
#
#
#
#
#
#
# # 5. mpg 데이터는 연비를 나타내는 변수가 2개입니다.
# # 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다.
# # 평균 연비 변수는 두 연비(고속도로와 도시)의 평균을 이용합니다.
# # 회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요.

# class Mpg(object):
#     def __init__(self, manufacturer, model, displ, year, cyl, trans, drv, cty, hwy, fl, class_1):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.displ = float(displ)
#         self.year = int(year)
#         self.cyl = float(cyl)
#         self.trans = trans
#         self.drv = drv
#         self.cty =float(cty)
#         self.hwy = float(hwy)
#         self.fl = fl
#         self.class_1 = class_1
#
#
#     def __repr__(self):
#         return "{}".format(self.manufacturer)
#
# mpg_list = list()
# file1 = open("/Users/admin/PycharmProjects/Python_basic/mpg.txt", "r", encoding='euc-kr') # 맥
#
#
# while True:
#     line = file1.readline()
#     if not line:
#         break
#     x = line[:-1]
#     mpg_data = x.split(',')
#     if mpg_data[10] == "suv":
#         mpg_list.append(Mpg(mpg_data[0], mpg_data[1], mpg_data[2], mpg_data[3], mpg_data[4], mpg_data[5], mpg_data[6], mpg_data[7], mpg_data[8], mpg_data[9], mpg_data[10])) # \n이 처리가됨
# file1.close()
#
#
# my_list = list()
# for j in mpg_list:
#     a = str(j)
#     my_list.append(a)
#
# manufacture_list = set(my_list)
# hwy_list_manufacture = []
# for i in manufacture_list:
#     hwy_list = [tmp.hwy for tmp in mpg_list if tmp.manufacturer == i]
#     average_hwy = sum(hwy_list) / len(hwy_list)
#     cty_list = [tmp.cty for tmp in mpg_list if tmp.manufacturer == i]
#     average_cty = sum(cty_list) / len(cty_list)
#     sum_y = (average_cty + average_hwy)/2
#     print ("{} 제조사의 평균 연비는 {} ".format(i,sum_y))
#     hwy_list_manufacture.append([i,sum_y])
#
# hwy_list_manufacture.sort(reverse=True, key=lambda x:x[1])
# print(hwy_list_manufacture[0:5])





# # 6. mpg 데이터의 class_1는 "suv", "compact" 등 자동차의 특징에 따라
# # 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다.
# # class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.

# class Mpg(object):
#     def __init__(self, manufacturer, model, displ, year, cyl, trans, drv, cty, hwy, fl, class_1):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.displ = float(displ)
#         self.year = int(year)
#         self.cyl = float(cyl)
#         self.trans = trans
#         self.drv = drv
#         self.cty =float(cty)
#         self.hwy = float(hwy)
#         self.fl = fl
#         self.class_1 = class_1
#
#
#     def __repr__(self):
#         return "{}".format(self.class_1)
#
# mpg_list = list()
# file1 = open("/Users/admin/PycharmProjects/Python_basic/mpg.txt", "r", encoding='euc-kr') # 맥
#
#
# while True:
#     line = file1.readline()
#     if not line:
#         break
#     x = line[:-1]
#     mpg_data = x.split(',')
#     mpg_list.append(Mpg(mpg_data[0], mpg_data[1], mpg_data[2], mpg_data[3], mpg_data[4], mpg_data[5], mpg_data[6], mpg_data[7], mpg_data[8], mpg_data[9], mpg_data[10])) # \n이 처리가됨
# file1.close()
#
#
# my_list = list()
# for j in mpg_list:
#     a = str(j)
#     my_list.append(a)
#
# class_1_list = set(my_list)
# cty_list_class_1 = []
# for i in class_1_list:
#     cty_list = [tmp.cty for tmp in mpg_list if tmp.class_1 == i]
#     average_cty = sum(cty_list) / len(cty_list)
#     print ("{} class_1의 cty는 {} ".format(i,average_cty))
#     cty_list_class_1.append([i,average_cty])
#
#
# cty_list_class_1.sort(reverse=True, key=lambda x:x[1])
# print(cty_list_class_1)
#
#
#
#
#
#
#
#
#
#
#
# # # 7. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다.
# # # hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.
#
# class Mpg(object):
#     def __init__(self, manufacturer, model, displ, year, cyl, trans, drv, cty, hwy, fl, class_1):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.displ = float(displ)
#         self.year = int(year)
#         self.cyl = float(cyl)
#         self.trans = trans
#         self.drv = drv
#         self.cty =float(cty)
#         self.hwy = float(hwy)
#         self.fl = fl
#         self.class_1 = class_1
#
#
#     def __repr__(self):
#         return "{}".format(self.manufacturer)
#
# mpg_list = list()
# file1 = open("/Users/admin/PycharmProjects/Python_basic/mpg.txt", "r", encoding='euc-kr') # 맥
#
#
# while True:
#     line = file1.readline()
#     if not line:
#         break
#     x = line[:-1]
#     mpg_data = x.split(',')
#     mpg_list.append(Mpg(mpg_data[0], mpg_data[1], mpg_data[2], mpg_data[3], mpg_data[4], mpg_data[5], mpg_data[6], mpg_data[7], mpg_data[8], mpg_data[9], mpg_data[10])) # \n이 처리가됨
# file1.close()
#
#
# my_list = list()
# for j in mpg_list:
#     a = str(j)
#     my_list.append(a)
#
# manufacture_list = set(my_list)
# hwy_list_manufacture = []
# for i in manufacture_list:
#     hwy_list = [tmp.hwy for tmp in mpg_list if tmp.manufacturer == i]
#     average_hwy = sum(hwy_list) / len(hwy_list)
#     print ("{} 제조사의 평균 고속도로 연비는 {} ".format(i,average_hwy))
#     hwy_list_manufacture.append([i,average_hwy])
#
#
# hwy_list_manufacture.sort(reverse=True, key=lambda x:x[1])
# print(hwy_list_manufacture[0:3])
#
# # 8. 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다.
# # 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.
# #
# class Mpg(object):
#     def __init__(self, manufacturer, model, displ, year, cyl, trans, drv, cty, hwy, fl, class_1):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.displ = float(displ)
#         self.year = int(year)
#         self.cyl = float(cyl)
#         self.trans = trans
#         self.drv = drv
#         self.cty =float(cty)
#         self.hwy = float(hwy)
#         self.fl = fl
#         self.class_1 = class_1
#
#
#     def __repr__(self):
#         return "{}".format(self.manufacturer)
#
# mpg_list = list()
# file1 = open("/Users/admin/PycharmProjects/Python_basic/mpg.txt", "r", encoding='euc-kr') # 맥
#
#
# while True:
#     line = file1.readline()
#     if not line:
#         break
#     x = line[:-1]
#     mpg_data = x.split(',')
#     if mpg_data[10] == "compact":
#         mpg_list.append(Mpg(mpg_data[0], mpg_data[1], mpg_data[2], mpg_data[3], mpg_data[4], mpg_data[5], mpg_data[6], mpg_data[7], mpg_data[8], mpg_data[9], mpg_data[10])) # \n이 처리가됨
#
# file1.close()
#
# from collections import Counter
# my_list = list()
# for z in mpg_list:
#     my_txt = str(z)
#     my_list.append(my_txt)
# # print(my_list)
# count = Counter(my_list)
# print(count)        #순서는 랜덤 .... Counter({'audi': 15, 'volkswagen': 14, 'toyota': 12, 'subaru': 4, 'nissan': 2})
#
#
#
# for k, v in count.items():
#     print(k, ":", v)
#
# '''
# audi : 15
# nissan : 2
# subaru : 4
# toyota : 12
# volkswagen : 14
# '''
#
#
# '''
# 참고 : dict 함수 추가기능 !!!
# 결과
# Counter()
# Counter({'f': 1, 'e': 1, 'b': 1, 'g': 1, 'c': 1, 'a': 1, 'd': 1})
# a.update({'f':3, 'e':2})  # 뎃셈으로 추가 가능함 f +3,  e +2
# print(a)
#
# 결과
# Counter({'f': 4, 'e': 3, 'b': 1, 'g': 1, 'c': 1, 'a': 1, 'd': 1})
# '''




