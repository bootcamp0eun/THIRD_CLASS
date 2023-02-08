# practice ex 01 . 허니버터칩이 가장 많이 남은 편의점 찾기

class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(graph):
    print('\t\t\t', end='')
    for n in range(graph.size):
        print("%9s " % store_array[n][0], end=' ')
    print()
    for n in range(graph.size):
        print("%9s" % store_array[n][0], end='   ')
        for i in range(graph.size):
            print("%8d" % graph.graph[n][i], end='   ')
        print()
    print()





store_array = [["GS25", 30], ["CU", 60], ["emart24", 40], ["MiniStop", 90], ["seven11", 10]]
g = Graph(5)
gs, cu, emart, mini, seven = 0, 1, 2, 3, 4

g.graph[gs][cu], g.graph[gs][seven] = 1, 1
g.graph[cu][gs], g.graph[cu][seven], g.graph[cu][mini] = 1, 1, 1
g.graph[emart][mini] = 1
g.graph[mini][emart], g.graph[mini][cu], g.graph[mini][seven] = 1, 1, 1
g.graph[seven][gs], g.graph[seven][cu], g.graph[seven][mini] = 1, 1, 1

print("## 편의점 그래프 ##")
print_graph(g)
print()


stack = []
visit = []

current = 0
find = current
find_count = store_array[current][1]
stack.append(current)
visit.append(current)

while len(stack) != 0:
    next = None
    for v in range(g.size):
        if g.graph[current][v] == 1:
            if v in visit:
                pass
            else:
                next = v
                break
    if next != None:
        current = next
        stack.append(current)
        visit.append(current)
        if store_array[current][1] > find_count:
            find_count = store_array[current][1]
            find = current
    else:
        current = stack.pop()


print(f"허니버터칩 최대 보유 편의점(개수) -->  {store_array[find][0]} ( {find_count} ) ")