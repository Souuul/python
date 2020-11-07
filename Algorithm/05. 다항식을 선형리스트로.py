## 함수선언부
def printPoly(p_x):
    term = len(p_x) -1
    polystr = 'P(x) = '

    for i in range(len(p_x)):
        coef = p_x[i] # 계수
        if (coef >=0):
            polystr += '+'
        polystr += str(coef) + 'x^' + str(term) + ' '
        term -=1

    return polystr

def calcPoly(xval, p_x) :
    retval = 0
    term = len(p_x) -1
    for i in range(len(p_x)):
        coef = p_x[i]
        retval += coef * xval ** term
        term -= 1
    return retval


## 전역 변수부
px  = [7,-4,0,5] # = 7x^3 ....

print(printPoly(px))

xvalue = int(input('x값-->'))
pxValue = calcPoly(xvalue, px)
print(pxValue)

# 이렇게 옮기면 오버헤드로 원소의 개수가 많고 삽입 삭제 연산이 많이 발생하는 경우에 성능상의 문제 발생
