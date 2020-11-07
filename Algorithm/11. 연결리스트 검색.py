##  클래스 및 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None #손



def printNode(start):
    current = start
    print(current.data, end='-->')
    while True:
        if current.link == None:
            break
        current = current.link
        print(current.data, end='-->')
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre
    # 첫번째 데이터 앞에 삽입 될때
    if findData == head.data :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    # 중간에 삽입 될때
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    # 마지막에 추가할때 (= 못 찾을떄)
    node = Node()
    node.data = insertData
    current.link = node

def deletNode(deleteData):
    global memory, head, current, pre

    # 첫 노드 삭제
    if head.data == deleteData:
        current = head
        head = current.link
        del (current)
        return

    current = head
    while current.link !=None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del (current)
            return

def findNode(findData) :
    global memory, head, current, pre

    current = head
    if current.data == findData :
        return  current
    while current.link != None :
        current = current.link
        if current.data == findData:
            return current
    return Node()




# 전역변수부
memory = [] # 리스트 --> 도라에몽 (앞주머니)
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

# 메인 코드부
if __name__ == '__main__':
    # 첫번째 노드
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for tw in dataArray[1:]:
        pre = node
        node = Node()
        node.data = tw
        pre.link = node
        memory.append(node)

    printNode(head)


    # 연결 리스트 삽입 연산
    insertNode('다현', '화사')
    printNode(head)
    insertNode('사나', '마동석')
    printNode(head)
    insertNode('한솔', '문별')
    printNode(head)

    # 연결리스트 삭제 연산
    deletNode('다현')
    printNode(head)

    ## 찾기
    fnode = findNode('마동석')
    print(fnode.data)

    fnode = findNode('솔')
    print(fnode.data)


