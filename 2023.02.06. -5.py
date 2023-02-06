import random


class Node():
    def __init__(self, data):
        self.data = data
        self.link = None


def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link  # 다음 노드로 이동
        print(current.data, end=' ')
    print()


def insert_nodes(find_data, insert_data):
    global head, current, pre
    if head.data == find_data:  # 첫 번째 노드 삽입
        node = Node(insert_data)
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node(insert_data)
            node.link = current
            pre.link = node
            return

    node = Node(insert_data)  # 마지막 노드 삽입
    current.link = node
    node.link = head


def delete_nodes(delete_data):
    global head, current, pre

    if head.data == delete_data:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del current
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del current
            return

    # 삭제할 데이터를 못찾은 경우에는 함수 종료


def find_nodes(find_data):
    global head, current, pre

    current = head
    if current.data == find_data:
        return current

    while current.link != head:
        current = current.link
        if current.data == find_data:
            return current

    return Node(None)


def is_find(find_data):
    '''
    연결 리스트 안에서 원소가 존재 여부 판정 함수
    :param find_data: 찾고자 하는 원소. str
    :return: 연결 리스트 안에서 원소가 존재하면 True 리턴 아니면 False
    '''
    global head, current, pre

    current = head
    if current.data == find_data:
        return True

    while current.link != head:
        current = current.link
        if current.data == find_data:
            return True

    return False


def count_plus_minus():
    global head, current
    plus, minus, zero = 0, 0, 0

    current = head
    while True:
        if current.data > 0:
            plus = plus + 1
        elif current.data < 0:
            minus = minus + 1
        else:
            zero = zero + 1
        if current.link == head:
            break
        current = current.link

    return plus, minus, zero


def makeSignToggle():
    global head, current
    current = head
    while True:
        current.data = current.data * -1
        if current.link == head:
            break
        current = current.link


head, current, pre = None, None, None
data_array = list()


if __name__ == "__main__":
    for _ in range(7):
        data_array.append(random.randint(-100, 100))
    node = Node(data_array[0])
    head = node
    node.link = head

    for data in data_array[1:]:
        pre = node
        node = Node(data)
        pre.link = node
        node.link = head

    print_nodes(head)

    plus_minus_zero = count_plus_minus()
    print(f"양수 {plus_minus_zero[0]}개, 음수 {plus_minus_zero[1]}개, 0 {plus_minus_zero[2]}개")
    makeSignToggle()
    print_nodes(head)
