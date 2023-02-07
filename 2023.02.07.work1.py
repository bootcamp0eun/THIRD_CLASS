SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1


def is_queue_full():
    global SIZE, queue, front, rear
    if rear == SIZE-1:
        return True
    return False


def is_queue_empty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    return False


def enqueue(new_data):
    global SIZE, queue, front, rear
    if is_queue_full():
        print("대기줄에 빈 자리가 없습니다.")
        return
    rear = rear + 1
    queue[rear] = new_data


def dequeue():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("대기줄이 비었습니다.")
        return
    front = front + 1
    temp = queue[front]
    queue[front] = None
    for i in range(front+1, rear+1):
        queue[i-1] = queue[i]
        queue[i] = None
    front = -1
    rear = rear -1
    return temp


def peek():
    global SIZE, queue, front, rear
    if is_queue_empty():
        return None
    return queue[front + 1]


people = ["정국", "뷔", "지민", "진", "슈가"]
for person in people:
    enqueue(person)


while True:
    print(f"대기 줄 상태 : {queue}")
    if not peek():
        print("식당 영업 종료!")
        break
    print(dequeue(), "님 식당에 들어감")

