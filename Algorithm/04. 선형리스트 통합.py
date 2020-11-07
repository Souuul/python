#  함수 및 클래스 선언문
katok = [] # 빈배열 리스

def add_data(friend):
    katok.append(None) # 빈칸추가
    KLen = len(katok) # 배열의 크기
    katok[KLen-1] = friend # 친구를 선형 리스트에 추가




def insert_data(position, friend):
    # position이 선형리스트의 범위에 있나?
    katok.append(None)
    KLen = len(katok)
    # 칸이동
    for i in range(KLen-1, position, -1):
        katok[i] =  katok[i-1]
        katok[i - 1] = None

    katok[position] = friend





def delete_data(position):
    KLen = len(katok)
    katok[position] = None
    for i in range(position, KLen-1):
        katok[i] =  katok[i+1]
    del(katok[KLen-1])



# 전역 변수부
katok = []


# 메인 코드부
if __name__ == '__main__':
    add_data('다현')
    add_data('정연')
    add_data('쯔위')
    print(katok)

    insert_data(2, '화사')
    print(katok)


    delete_data(2)
    print(katok)