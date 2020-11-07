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