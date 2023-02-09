import random


class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(head):
    current = head
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != head:
        current = current.link
        print(current.data, end=' ')
    print()


def insert(new_data):
    global head, current
    current = head
    new_node = Node()
    new_node.data = new_data
    if head == None:
        head = new_node
        new_node.link = head
        return
    if head.link == head:
        head.link = new_node
        new_node.link = head
        return
    last = current.link
    while last.link != head:
        last = last.link
    last.link = new_node
    new_node.link = head


def count_odd_even():
    global head, current
    odd, even = 0, 0
    if head == None:
        return 0, 0
    current = head
    while True:
        if current.data % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
        if current.link == head:
            break
        current = current.link
    return odd, even


def make_minus(odd, even):
    global head, current
    if odd > even:
        remainder = 1
    else:
        remainder = 0
    current = head
    while True:
        if current.data % 2 == remainder:
            current.data = current.data * -1
        if current.link == head:
            break
        current = current.link


if __name__=="__main__":
    head, current = None, None
    for _ in range(7):
        insert(random.randint(1, 100))
    print_nodes(head)
    odd, even = count_odd_even()
    print(f"odd number : {odd}, even number : {even}")
    make_minus(odd, even)
    print_nodes(head)