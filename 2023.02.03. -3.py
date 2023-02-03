def print_Poly(px, tx):
    '''
    다항식을 포맷에 맞게 출력하는 함수
    :param px: 계수를 원소로 가지고 있는 리스트
    :param tx: 차수를 원소로 가지고 있는 리스트
    :return: 다항식 문자열
    '''
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]
        term = tx[i]

        if coef == 0:
            continue
        elif i != 0 and coef > 0:
            poly_str += "+"
        poly_str = poly_str + f"{coef}x^{term} "

    return poly_str


def calc_poly(x_val, px, tx):
    '''
    다항식의 산술연산을 하는 함수
    :param x_val: x값 integer
    :param px: 계수를 원소로 가지고 있는 리스트
    :param tx: 차수를 원소로 가지고 있는 리스트
    :return: 다항식 계산 결과 값 integer
    '''
    ret_value = 0

    for i in range(len(px)):
        term = tx[i]
        coef = px[i]
        ret_value = ret_value + coef * x_val ** term
        term -= 1

    return ret_value


tx = [300, 20, 0]
px = [7, -4, 5]


if __name__ == "__main__":
    print(print_Poly(px, tx))

    x_value = int(input("X 값 : "))

    print(calc_poly(x_value, px, tx))



