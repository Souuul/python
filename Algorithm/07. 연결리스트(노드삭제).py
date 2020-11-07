class Node() :
    def __init__(self):
        self.data = None
        self.link = None #손



node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3


## 정연과 쯔위사이에 연결
newnode = Node()
newnode.data = '솔'
newnode.link = node2.link
node2.link = newnode



current = node1
print(current.data, end='-->')
while True:
    if current.link == None:
        break
    current = current.link
    print(current.data, end='-->')
print()

# 솔을 삭제
node2.link = newnode.link
del(newnode)

current = node1
print(current.data, end='-->')
while True:
    if current.link == None:
        break
    current = current.link
    print(current.data, end='-->')