## 함수 선언부 (클래스 선언)
class Node() :
    def __init__(self):
        self.data =None
        self.link = None


def printNodes (start) :
    current = start
    print(current.data, end='  ')
    while current.link !=None :
        current = current.link
        print(current.data, end='  ')



def insert_node(findData, insertData):  #누구를 찾아서, 그애 앞에 삽입해서 입력해
    global memory, head, current, pre
    # 예) 다현앞에 화사를 삽입(3가지)
    if head.data == findData : # 첫 노드를 삽입
        node = Node()   #새로운 데이터 만들어(빈노드 만들기)
        node.data = insertData  # 화사를 집어넣고
        node.link = head  #화사.링크를 헤드로 넣고
        head = node   # 헤드는 노드
        return

#중간노드삽입 (사나 찾아서 솔라 집어넣기)
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

# 마지막 노드 삽입

    node = Node()
    node.data = insertData
    current.link = node


## 첫노드 삭제
def delete_node(deleteData):
    global memory, head, current, pre

    if head.data == deleteData :
        current = head
        head = head.link
        del(current)
        return

        # 그외 노드 삭제
    current = head  # 찾아보기
    while current.link != None:  # 커런트가 none이 아닌동안에
        pre = current  # 프리 이리와 .. 현재로 가
        current = current.link  # 현재인 나는 다음으로 갈께
        if current.data == deleteData:
            pre.link = current.link
            del (current)
            return


## 전역 변수부
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']  # DB에서 읽기, 크롤링된 데이터

node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:]:  # 두번째부터['정연','쯔위','사나','지효']
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)


printNodes(head)

insert_node('다현','화사')
printNodes(head)

insert_node('사나','솔라')
printNodes(head)

insert_node('재남','문별')
printNodes(head)


delete_node('화사')
printNodes(head)
delete_node('쯔위')
printNodes(head)
