memo = list()  # 전역 변수로 한번 처리한 결과 값을 저장
def fibo_memo(n):
    """
    Memoization(DP)을 사용한 피보나치 수열 처리 함수
    :param n: 
    :return: 
    """
    global count_memoization
    count_memoization = count_memoization + 1
    memo = [0, 1]
    if n <= 1:
        return memo[n]
    else:
        for i in range(2, n+1):
            memo.append(memo[i-1] + memo[i-2])
        return memo[n]


memos = [None for _ in range(100)]  # 전역 리스트
memos[0], memos[1] = 0, 1
def fibo_memo_recu(n):
    """
    재귀 함수에 Memoization(DP)을 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """
    global memos, count_memo_recu
    count_memo_recu = count_memo_recu + 1
    if n <= 1:
        return memos[n]
    if memos[n] is not None:  # 전역 메모리 memos에 이전에 계산한 결과 값이 존재하면
        return memos[n]
    memos[n] = fibo_memo_recu(n-2) + fibo_memo_recu(n-1)  # 처음 방문하는 n이면


def fibo_recu(n):
    """
    재귀 함수를 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """
    global count_recursion
    count_recursion = count_recursion + 1
    if n <= 1:
        return n
    else:
        return fibo_recu(n-1) + fibo_recu(n-2)


def fibo_iter(n):
    r = list()
    p1, p2 = 1, 1
    for _ in range(n):
        r.append(p1)
        p1, p2 = p2, p1+p2
    return r[-1]


count_memoization = 0
count_recursion = 0
count_memo_recu = 0

print('피보나치 수 --> 0 1 ')
for i in range(2, 30):
    print(f'{i} : {fibo_memo(i)}')

for i in range(2, 30):
    #print(f'{i} : {fibo_iter(i)}')  # repetition
    print(f'{i} : {fibo_recu(i)}')   # recursion

for i in range(2, 30):
    print(f'{i} : {fibo_memo_recu(i)}')  # memo + recu

print(f"재귀 : {count_recursion}, 메모 : {count_memoization}, 재귀메모 : {count_memo_recu}")

# => 재귀 메모 : 메모리를 조금 더 쓰더라도 속도 개선을 할 수 있담.