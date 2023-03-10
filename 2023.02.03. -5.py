
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None
    # def __init__(self, data):로 해서 만들어도 됨

    def __repr__(self):
        return f'포켓몬스터!'


def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link  # 다음 노드로 이동
        print(current.data, end=' ')
    print()


memory = []
head, current, pre = None, None, None
dataArray = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]


if __name__ == "__main__":

    node = Node()		# 첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:  # 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    print_nodes(head)
    print(memory)
    print(node.data)
    print(pre.data)
