import random

class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(start):
    current = start
    street = (current.data[1] ** 2 + current.data[2] ** 2) ** (1 / 2)
    print(f"{current.data[0]}, 거리: {street}")
    while current.link != start:
        current = current.link
        street = (current.data[1]**2 + current.data[2]**2) ** (1/2)
        print(f"{current.data[0]}, 거리: {street}")


def insert(data):
    global head, current, pre
    new = Node()
    new.data = data
    km_new = (new.data[1] ** 2 + new.data[2] ** 2) ** (1 / 2)
    if head == None:
        head = new
        new.link = head
        return
    current = head
    km_current = (current.data[1] ** 2 + current.data[2] ** 2) ** (1 / 2)
    if km_new < km_current:
        new.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = new
        head = new
        return
    while current.link != head:
        pre = current
        current = current.link
        km_current = (current.data[1] ** 2 + current.data[2] ** 2) ** (1 / 2)
        if km_new < km_current:
            pre.link = new
            new.link = current
            return
    current.link = new
    new.link = head


head, current, pre = None, None, None


for i in range(10):
    name = chr(65 + i) + " 편의점"
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    data = (name, x, y)
    insert(data)

print_nodes(head)



