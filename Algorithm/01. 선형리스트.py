katok = [] # 빈배열 리스

def add_data(friend):
    katok.append(None) # 빈칸추가
    KLen = len(katok) # 배열의 크기
    katok[KLen-1] = friend # 친구를 선형 리스트에 추가

add_data('다현')
add_data('정연')
add_data('쯔위')

print(katok)
