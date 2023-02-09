# 원형 큐

# 원형 큐에 데이터 삽입, 추출, 확인하는 함수 만들기

size = 10
queue = [None for _ in range(size)]
front = rear = 0


def is_queue_full():
    global size, queue, front, rear
    if (rear+1) % size == front:
        return True
    return False


def is_queue_empty():
    global size, queue, front, rear
    if rear == front:
        return True
    return False


def enQueue(data):
    global size, queue, front, rear
    if is_queue_full():
        print("큐가 가득 찼습니다")
        return
    rear = (rear + 1) % size
    queue[rear] = data


def deQueue():
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    front = (front + 1) % size
    temp = queue[front]
    queue[front] = None
    return temp


def peek():
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[(front+1) % size]


for data in ["오리사", "메르시", "파라", "겐지", "둠피스트", "소전", "위도우"]:
    enQueue(data)
print(queue)
print("deQueue() -> ", deQueue())
print(queue)
print("peek() -> ", peek())
print("deQueue() -> ", deQueue())
print("deQueue() -> ", deQueue())
print(queue)
enQueue("윈스턴")
enQueue("정커퀸")
enQueue("키리코")
print(queue)
