# 원형 연결 리스트

# 원형 연결 리스트에 원하는 위치에 데이터 삽입하고, 원하는 데이터 삭제하는 함수 만들기
# 원형 연결 리스트 출력하는 함수 만들기
head, current, pre = None, None, None


class Node:
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes():
    global head, current, pre
    current = head
    if current == None:
        return
    print(current.data, end=' -> ')
    while current.link != head:
        current = current.link
        print(current.data, end=' -> ')
    print()


def add(new_data):
    global current, head, pre
    current = head
    new = Node()
    new.data = new_data
    if head == None:
        head = new
        head.link = head
        return
    while current.link != head:
        current = current.link
    current.link = new
    new.link = head


def insert(find_data, new_data):
    global current, head, pre
    current = head
    new = Node()
    new.data = new_data
    last = current
    if head.data == find_data:
        new.link = head
        head = new
        while last.link != head:
            last = current.link
        last.link = head
        return
    while current.link != head:
        pre = current
        current = current.link
        if current.data == find_data:
            pre.link = new
            new.link = current
            return


def delete(delete_data):
    global head, pre, current
    current = head
    last = current
    if head.data == delete_data:
        head = head.link
        del current
        while last.link != head:
            last = last.link
        last.link = head
        return
    while current.link != head:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del current
            return


for data in ["오리사", "메르시", "겐지", "둠피스트", "키리코", "레킹볼"]:
    add(data)

print_nodes()
insert("겐지", "파라")
print_nodes()
delete("둠피스트")
print_nodes()






