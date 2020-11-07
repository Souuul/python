## 함수 선언부
def isstackempty():
    global size, stack, top
    if (top <= -1):
        return True
    else:
        return False

def isstackfull():
    global size, stack, top
    if top == size-1:
        return True
    else:
        return False

def push(data):
    global size, stack, top
    if isstackfull():
        print('스택 꽉참!')
        return
    top += 1
    stack[top] = data

def pop():
    global size, stack, top
    if (isstackempty()):
        print('스택에 없어요!')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

## 전역 변수부
size = 5
stack = [None for _ in range(size)]
top = -1

## 메인 코드부
if __name__ == '__main__':
    push('A')
    push('B')
    push('C')

    print(pop())
    print(pop())
    print(pop())
    print(pop())
'''
C
B
A
스택에 없어요!
None
'''

