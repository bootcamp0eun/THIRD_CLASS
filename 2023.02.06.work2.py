# 2023.02.06.
# Chapter04 . 응용예제 01

class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()


def insert(name_email):
    global head, current, pre
    new_node = Node()
    new_node.data = name_email
    if head == None:
        head = new_node
        return
    current = head
    if new_node.data[1] < current.data[1]:
        new_node.link = head
        head = new_node
        return
    while current.link != None:
        pre = current
        current = current.link
        if new_node.data[1] < current.data[1]:
            new_node.link = current
            pre.link = new_node
            return
    current.link = new_node


if __name__=="__main__":
    head, current, pre = None, None, None

    while True:
        name = input("이름--> ")
        if name == '':
            break
        email = input("이메일--> ")
        insert([name, email])
        print_nodes(head)
