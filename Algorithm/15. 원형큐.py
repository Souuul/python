## 함수 선언부
def isQueueFull() :
    if ( (rear + 1) % SIZE == front) :
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
    rear = (rear + 1) % SIZE
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
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인 코드부
enQueue('A')
print(queue)
enQueue('B')
print(queue)
enQueue('C')
print(queue)
enQueue('D')
print(queue)
enQueue('E') # 실패
print(queue)
print(deQueue())
enQueue('E') # 성공
print(queue)