## 메인코드 부분##
SIZE = int(input("큐 크기를 입력하세요 ===> "))
queue = [None for _in range(SIZE)]
front = rear = -1

## 메인코드부분 ##

if __name__=="__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    while(select != 'X' and select != 'x') :
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            enQueue(data)
            print("큐 상태 : ", queue)
        elif select == 'E' or select == 'e':
            data = deQueue()
            print("추출된 데이터 : ==> ", data)
            print("스택 상태 : ", queue)
        elif select == 'V ' or select == 'v':
            data = peek()
            print("확인된 데이터 : ==>", data)
            print("스택 상태 : ",  queue)
        else :
            print("입력이 잘못됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    print("프로그램 종료!")
