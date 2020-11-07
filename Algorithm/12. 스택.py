# 스택의 크기를 제한해서 생성 (5개 짜리)
stack = [None, None, None, None, None]
stack = [ None for _ in range(5)]
top = -1
# Push (데이터)
top += 1
stack[top] = 'A'

top += 1
stack[top] = 'B'

top += 1
stack[top] = 'C'

# Pop()

data = stack[top]
stack[top] = None
top -= 1

data = stack[top]
stack[top] = None
top -= 1

data = stack[top]
stack[top] = None
top -= 1

print(top)

