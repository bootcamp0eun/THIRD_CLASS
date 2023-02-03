def print_Poly(p_x):
    term = len(p_x) - 1  # 최고차항 숫자 = 배열길이-1
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = p_x[i]  # 계수

        if coef == 0:
            term = term - 1
            continue
        elif i != 0 and coef > 0:
            poly_str += "+"
        poly_str = poly_str + f"{coef}x^{term} "
        term = term - 1

    return poly_str


def calc_poly(x_val, p_x):
    ret_value = 0
    term = len(p_x) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = p_x[i]  # 계수
        ret_value = ret_value + coef * x_val ** term
        term -= 1

    return ret_value


## 전역 변수 선언 부분 ##
px = [3, -4, 0, 6]  # = 7x^3 -4x^2 +0x^1 +5x^0

## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = print_Poly(px)
    print(pStr)

    x_value = int(input("X 값 : "))

    print(calc_poly(x_value, px))



