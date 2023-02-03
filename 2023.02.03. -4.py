first_list = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]


def insert(new_1, new_2):
    new = (new_1, new_2)
    for i in range(0, len(first_list)-1):
        if new_2 >= first_list[i][1]:
            first_list.append(None)
            for k in range(len(first_list)-1, i, -1):
                first_list[k] = first_list[k-1]
                first_list[k-1] = None
            first_list[i] = new
            break
        if i == len(first_list)-1:
            first_list.append(new)


print(first_list)
new_1 = input("추가할 친구 : ")
new_2 = int(input("카톡 횟수 : "))
insert(new_1, new_2)
print(first_list)
