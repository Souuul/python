katok = ['다현', '정연', '쯔위', '사나', '지효']

def insert_data(position, friend):
    # position이 선형리스트의 범위에 있나?
    katok.append(None)
    KLen = len(katok)
    # 칸이동
    for i in range(KLen-1, position, -1):
        katok[i] =  katok[i-1]
        katok[i - 1] = None

    katok[position] = friend

insert_data(2, '화사')
print(katok)