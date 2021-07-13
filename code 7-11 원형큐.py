def isQueueFull() :
    global SIZE, queue, front, rear
    if ( (rear+1)%SIZE == front):    # 초기화
        return True
    else :
        return False


def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False



def deQueue():
    global SIZE, queue, front, rear
    if (deQueue()):
        print('큐 텅!')
        return None
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data



def enQueue(data) :
    global SIZE,queue, front, rear
    if(isQueueFull()):
        print('큐 꽉!')
        return
    rear = (rear+1) % SIZE
    queue[rear] = data



def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐 텅!')
        return None
    return queue[(front+1)%SIZE]



## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = 0,0 # 원형큐 초기화


## 메인코드
queue =[None, None, '화사', '솔라', None]
front = 1
rear = 3
print(queue)
enQueue('선미')
print(queue)
enQueue('재남')
print(queue)
enQueue('유정')
print(queue)
