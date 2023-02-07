SIZE = 6
queue = [None for _ in range(SIZE)]
front = rear = 0


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
        print("queue is full")
        return
    rear = (rear + 1) % SIZE
    queue[rear] = new_data


def dequeue():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("queue is empty")
        return
    front = (front + 1) % SIZE
    temp = queue[front]
    queue[front] = None
    return temp


def peek():
    global SIZE, queue, front, rear
    if is_queue_empty():
        return None
    return queue[(front + 1) % SIZE]


def timesum():
    global SIZE, queue, front, rear
    if is_queue_empty():
        return 0
    sum = 0
    for i in range((front+1)%SIZE, (rear+1)%SIZE):
        sum = sum + queue[i][1]
    return sum


calls = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]

for call in calls:
    print(f"귀하의 대기 예상 시간은 {timesum()}분입니다.")
    print("현재 대기콜 : ", queue)
    enqueue(call)
    print()

print("최종 대기콜 : ", queue)
print("프로그램 종료")



