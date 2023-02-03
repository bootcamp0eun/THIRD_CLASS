
"""
pokemons = list()


def add_data(pokemon):
    pokemons.append(None)
    #pokemons[len(pokemons) - 1] = pokemon
    pokemons[-1] = pokemon


add_data('피카츄')
add_data('라이츄')
add_data('파이리')
add_data('꼬부기')
add_data('이상해')

print(pokemons)
"""


def add_data(pokemon):
    '''
    선형 리스트의 맨 뒤에 원소 삽입
    :param pokemon:
    :return:
    '''
    pokemons.append(None)
    pokemons[len(pokemons)-1] = pokemon


def insert_data(idx, pokemon):
    '''
    선형 리스트의 idx 위치에 원소 삽입
    :param idx:
    :param pokemon:
    :return:
    '''
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가


def delete_data(idx):
    '''
    선형 리스트 idx 위치의 원소 삭제
    :param idx: int
    :return: void
    '''
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None  # 데이터 삭제

    for i in range(idx + 1, len_pokemons):
        pokemons[i] = None

    for i in range(idx, len_pokemons):
        pokemons.pop()

    temp = pokemons[:idx]
    '''
    for i in range(len_pokemons - idx)
        pokemons.pop()
    '''


pokemons = []

if __name__ == "__main__":
    while True:

        select = input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> ")

        if (select == '1'):
            data = input("추가할 데이터--> ")
            add_data(data)
            print(pokemons)
        elif (select == '2'):
            idx = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(idx, data)
            print(pokemons)
        elif (select == '3'):
            idx = int(input("삭제할 위치--> "))
            delete_data(idx)
            print(pokemons)
        elif (select == '4'):
            print(pokemons)
            #exit()
            break
        else:
            print("메뉴에서 고르세요")
            continue


    """
    pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]
    print(pokemons)
    delete_data(1)
    print(pokemons)
    delete_data(3)
    print(pokemons)
    '''
    pokemons.insert(2, '어니부기')
    #insert_data(2, '어니부기')
    print(pokemons)
    insert_data(6, '거북왕')
    print(pokemons)
    '''
    add_data('터검니')
    print(pokemons)
    """



