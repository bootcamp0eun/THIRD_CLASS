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


SIZE = 20
stack = [None for i in range(SIZE)]
top = -1


text = "진달래꽃\n나 보기가 역겨워\n가실 때에는\n말없이 고이 보내드리오리다."
text_split = text.split("\n")
print("-----원본-----")
print(text)
for i in range(len(text_split)):
    look = list(text_split[i])
    temp_top = top
    temp_stack = stack
    top = -1
    stack = [None for _ in range(SIZE)]
    for k in range(len(look)):
        push(look[k])
    inner_stack = stack
    stack = temp_stack
    top = temp_top
    push(inner_stack)

print("\n-----거꾸로 처리된 결과-----")
while not is_stack_empty():
    temp_stack = stack
    stack = pop()
    temp_top = top
    for i in range(len(stack)):
        if stack[i] == None:
            top = i -1
            break
    while not is_stack_empty():
        print(pop(), end='')
    print()
    stack = temp_stack
    top = temp_top


