## 함수
def isStackFull() :
    global SIZE, stack, top
    if top >= SIZE -1 :
        return True
    else :
        return False

    def push(data):
        global SIZE, stack, top
        if (isStackFull()):
            print('스택 꽉!')
            return
        top += 1
        stack[top] = data


def isStackEmpty() :
    global SIZE, stack, top
    if top <= SIZE - 1:
        return True
    else:
        return False

def pop() :
    global SIZE, stack, top
    if (isStackEmpty()):
        print('스택 텅!')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data






## 전역
SIZE = 5
stack =[None for _ in range(SIZE)]
top = -1


## 메인
stack = ['커피','녹차','꿀물', '콜라','환타']
top = 4
stack = ['커피','녹차','꿀물', '콜라','None']
top = 3


## 메인
print(stack)
push('게코레이')
print(stack)
push('파워에이드')
print(stack)

stack = ['커피',None,None,None,None]
top = 0
retData = pop()
print(retData)
retData = pop()
print(retData)







