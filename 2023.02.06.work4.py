def is_stack_empty():
    global SIZE, stack, top
    if top == -1:
        return True
    return False


def is_stack_full():
    global SIZE, stack, top
    if top == SIZE-1:
        return True
    return False


def push(new):
    global SIZE, stack, top
    if is_stack_full():
        return
    top = top + 1
    stack[top] = new


def peek():
    global stack, top
    if is_stack_empty():
        return None
    return stack[top]


def pop():
    global SIZE, stack, top
    if is_stack_empty():
        return None
    temp = stack[top]
    top = top - 1
    return temp


SIZE = 10
stack = [None for i in range(SIZE)]
top = -1

if __name__=="__main__":
    stone = ["주황", "초록", "파랑", "자주", "빨강", "노랑"]
    for i in stone:
        push(i)
    print("과자집에 가는 길 : ", end='')
    while not is_stack_empty():
        print(pop(), end=" --> ")
    print("과자집")

    i = -1
    while i >= -len(stone):
        push(stone[i])
        i = i - 1
    print("우리집에 오는 길 : ", end='')
    while not is_stack_empty():
        print(pop(), end=" --> ")
    print("우리집")

