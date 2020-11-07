import random
# 함수 선언부
def findMinIndex(arr) :
    minIdx = 0
    for i in range(1, len(arr)) :
        if(arr[minIdx] > arr [i]) :
            minIdx = i
    return minIdx


# 전역 변수부
before = [ random.randint(1,99) for _ in range(20)]
after = []


# 메인 코드부
print('정렬전 -->', before)
for _ in range(len(before)) :
    minPosition = findMinIndex(before)
    after.append(before[minPosition])
    del(before[minPosition])
print('정렬후 -->', after)