# 2023.02.06.
# Chapter04 . 응용예제 02

import random


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


def insert(num):
    '''
    주어진 원소를 연결 리스트에 삽입한다. 연결리스트의 정렬 순서는 원소 값의 순서대로
    :param num:
    :return:
    '''
    global head, current, pre
    new_node = Node()
    new_node.data = num
    if head == None:
        head = new_node
        return
    current = head
    if new_node.data < current.data:
        new_node.link = head
        head = new_node
        return
    while current.link != None:
        pre = current
        current = current.link
        if new_node.data < current.data:
            pre.link = new_node
            new_node.link = current
            return
    current.link = new_node


def find_true(num):
    '''
    주어진 num이 연결 리스트에 있는지 확인
    :param num:
    :return: 연결 리스트 안에 있으면 True, 없으면 False
    '''
    global head, current
    if head == None:
        return False
    if head.data == num:
        return True
    current = head
    while current.link != None:
        current = current.link
        if current.data == num:
            return True
    return False


if __name__=="__main__":
    head, current, pre = None, None, None
    i = 1
    while i <= 6:
        num = random.randint(1, 46)
        if not find_true(num):
            insert(num)
            i = i + 1
    print_nodes(head)
