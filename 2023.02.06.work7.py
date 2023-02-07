class Node():
    def __init__(self):
        self.data = None
        self.link = None
        self.re_link = None


def print_nodes(start):
    global head, current, pre
    current = start
    print("정방향 : ", end='')
    print(current.data, end=' ')
    while current.link != None:
        pre = current
        current = current.link
        print(current.data, end=' ')
    print()
    print("역방향 : ", end='')
    print(current.data, end=' ')
    while current.re_link != None:
        pre = current
        current = current.re_link
        print(current.data, end=' ')


namelist = ["다현", "정연", "쯔위", "사나", "지효"]
head, current, pre = None, None, None

def make_nodes(namelist):
    global head, current, pre
    first = Node()
    first.data = namelist[0]
    head = first
    current = head
    for i in range(1, len(namelist)):
        new = Node()
        new.data = namelist[i]
        current.link = new
        new.re_link = current
        current = current.link


make_nodes(namelist)
print_nodes(head)
