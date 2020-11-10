
# 제공된 데이터에서 숫자, 특수문자, 공백을 제거하고 소문자로 변환한다.
def makeNormalData(saleKind, saleNumber): # 판매된 물품 코드 문자열 배열, 판매된 물품의 개수
    retData = [] # 숫자, 공백, 특수문자가 제거된 소문자 문자열 배열.

    ################ 여기부터 코딩 (1) -------->
    for i in range(saleNumber) :
        newKind = ''
        for k in range(len(saleKind[i])) :
            if (saleKind[i][k].isalpha()) :
                newKind += saleKind[i][k].lower()
        retData.append(newKind)
    ################ <------------- 여기까지코딩 (1)
    return retData



# 순서가 바뀐 글자의 순서를 올바른 순서로 바로 잡는다.
def correctLetterOrder(saleKind, saleNumber, products): # 판매된 물품 코드 문자열 배열, 판매된 물품의 개수, 편의점에서 판매하는 물품 코드 배열 (13종 고정)
    retData = [] # 글자의 순서가 올바른 순서로 정돈된 문자열 배열.

    ################ 여기부터 코딩 (2) -------->
    # 13종 물품의 글자를 각각 정렬.
    tmpList = list(map(sorted,products))
    sortedProducts = list(map(''.join, tmpList))
    # print(tmpList)
    # print(sortedProducts)
    # 목록의 각 단어들을 정렬된 단어와 비교해서 교체하기
    count=0
    for kind in saleKind :
        kind = ''.join(sorted(kind))
        # 정렬된 한 단어(ceeffo)가 미리 정렬된 sortedProducts(ceeffo)의 어느것과 같은지 찾아서,
        # 원래인 products(coffee)의 이름으로 교체
        idx = sortedProducts.index(kind)
        saleKind[count] = products[idx]
        count += 1

    retData =saleKind
    ################ <------------- 여기까지코딩 (2)

    return retData



# 중복된 물품을 제거하고 정렬한다.
def makeDistinctedData(saleKind, saleNumber): # 소문자로만 구성된 물품 코드 문자열 배열, 	판매된 물품의 개수
    retData = [] # 중복이 제거된 문자열 배열

    ################ 여기부터 코딩 (3) -------->
    kindSet = set(saleKind)
    kindList = list(kindSet)
    # print(kindSet)
    # print(kindList)

    def findMinIndex(arr):
        minIdx = 0
        for i in range(1, len(arr)):
            if (arr[minIdx][1] > arr[i][1]):
                minIdx = i
            elif (arr[minIdx][1] == arr[i][1]):
                if (arr[minIdx][0] > arr[i][0]):
                    minIdx = i
        return minIdx

    newList = []
    for _ in range(len(kindList)):
        minPosition = findMinIndex(kindList)
        newList.append(kindList[minPosition])
        del (kindList[minPosition])

    retData = newList[:]
    ################ <------------- 여기까지코딩 (3)

    return retData