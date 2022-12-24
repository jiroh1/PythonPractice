"""
예제 : 피보나치 수열
- 피보나치 수열을 재귀함수로 구현
- 피보나치 수열을 동적계획법으로 구현 (계산된 결과를 저장해놓고, 꺼내서 사용) - 시간비교
"""


# 재귀함수로 구현
def fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 1

    return fibo(n - 1) + fibo(n - 2)

N = 10

# DP 구현
fibo_results = [0] * (N + 1)
fibo_results[0] = 1
fibo_results[1] = 1

# fibo_results[2] = ??
for i in range(2, N + 1):
    fibo_results[i] = fibo_results[i - 1] + fibo_results[i - 2]
    print('확인',i,'번째',fibo_results[i])

# fibo_results[-1]
# fibo_results[11]