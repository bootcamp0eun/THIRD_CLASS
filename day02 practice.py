# secret을 랜덤으로 지정하기
import random
secret = random.randint(1, 10)
# guess 값 입력받기
guess = int(input("1부터 10까지의 숫자 중 하나가 있습니다. 이 숫자가 무엇일지 추측해서 입력하십시오."))
# secret과 guess 비교해서 출력하기
if secret == guess:
    print("정확합니다.")
elif guess > secret:
    print("너무 큽니다.")
elif guess < secret:
    print("너무 작습니다.")