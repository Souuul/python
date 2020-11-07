katok = ['다현', '정연', '쯔위', '사나', '지효']

def delete_data(position):
    KLen = len(katok)
    katok[position] = None
    for i in range(position, KLen-1):
        katok[i] =  katok[i+1]
    del(katok[KLen-1])


delete_data(2)
print(katok)
