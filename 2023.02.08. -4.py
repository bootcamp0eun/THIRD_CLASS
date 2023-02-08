## BFS
from collections import deque


class Graph() :
    def __init__ (self, size) :
        self.SIZE = size
        self.graph = [[0 for x in range(size)] for x in range(size)]


g = None
#queue = []
queue = deque([])
visited_array = []


g = Graph(4)
g.graph[0][2] = 1; g.graph[0][3] = 1
g.graph[1][2] = 1
g.graph[2][0] = 1; g.graph[2][1] = 1; g.graph[2][3] = 1
g.graph[3][0] = 1; g.graph[3][2] = 1


for row in range(4):
    for col in range(4):
        print(g.graph[row][col], end=' ')
    print()

current = 0
queue.append(current)     # enqueue
visited_array.append(current)

while len(queue) != 0:
    next = None
    for vertex in range(4):
        if g.graph[current][vertex] == 1:
            if vertex in visited_array:
                pass
            else:
                next = vertex
                break

    if next is not None:
        current = next
        queue.append(current)   # enqueue
        visited_array.append(current)
    else:
        #current = queue.pop(0)  # O(n), OVERHEAD 발생
        current = queue.popleft()  # O(1)


print('방문 순서 : ', end='')
for i in visited_array:
    print(i, end=' --> ')
print("END")
