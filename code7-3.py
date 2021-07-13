## 함수, 클래스(대문자)
## C, C++  -->  변수이름 규칙의 원본
## 실무 : 변수이름 규정  ---> 지정
## 구글링을 통해서 좋은 변수명 규칙  ---> 적용

def isQueueFull() :
    global SIZE, queue, front, rear
    if(rear != SIZE-1):    # 초기화
        return False
    if (rear == SIZE -1) and (front == -1) :   #꽉찬상태
        return True
    else :
        for i in range(front+1, SIZE) :
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
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
    front += 1
    data = queue[front]
    queue[front] = None
    return data



def enQueue(data) :
    global SIZE,queue, front, rear
    if(isQueueFull()):
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data



def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐 꽉!')
        return None
    return queue[front+1]



## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = -1, -1

## 메인
queue =[None, None, '화사', '솔라', None]
front = 1
rear = 3

print(queue)
enQueue('선미')
print(queue)
enQueue('재남')


# queue =['화사', None, None, None, None]
# front = -1
# rear = 0
# print(queue)
# retData = deQueue()
# print('추출 -->', retData)
# retData = deQueue()
# print('추출 -->', retData)
# print(queue)