# 포켓몬 이름 삽입하기
pokemons = [['잉어킹', 50], ['삐삐', 100], ['따라큐', 150], ['폴리곤', 350], ['나옹', 500]]


def insert(new_name, new_num):
    new = [new_name, new_num]
    for i in range(len(pokemons)):
        if new_num <= pokemons[i][1]:
            pokemons.append(None)
            for k in range(len(pokemons)-1, i, -1):
                pokemons[k] = pokemons[k-1]
                pokemons[k-1] = None
            pokemons[i] = new
            break
    else:
        pokemons.append(None)
        pokemons[-1] = new


print(f"현재 포켓몬 리스트\n{pokemons}")
print("새로운 포켓몬을 입력합니다.")
new_name = input("이름을 입력하세요 : ")
new_num = int(input("체력을 입력하세요 : "))
insert(new_name, new_num)
print(f"\n변경된 포켓몬 리스트\n{pokemons}")
