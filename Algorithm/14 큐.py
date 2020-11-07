## 함수 선언부
def isQueueFull() :
    if (rear == SIZE -1) :
        return  True
    else :
        return  False

def isQueueEmpty() :
    if (rear == front) :
        return  True
    else :
        return  False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('꽉참')
        return
    rear += 1
    queue[rear] = data

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('없음')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data




## 전역 변수부
SIZE = 3
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인 코드부
enQueue('A')
enQueue('B')
print(deQueue())
enQueue('C')
print(deQueue())
print(deQueue())
enQueue('D') # 실패