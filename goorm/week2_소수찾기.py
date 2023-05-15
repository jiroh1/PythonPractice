# 기초 수학과 구현

# def Sieve(N):
#     is_prime = [1 for _ in range(N + 1)] # [1, 1, 1, 1, 1, 1, 1, 1]
#     prime = []
#     for i in range(2, N + 1):
#         print('for,',i, is_prime[i])
#         if not is_prime[i]: # 0 이면 for문 시작 하는 것으로 
#             print('i',i)
#             continue
#         prime.append(i)
#         print('p',prime)
#         for j in range(2 * i, N + 1, i): # 이 부분이 각 숫자의 배수를 0으로 하는 for 문
#             print('2nd for,', j)
#             is_prime[j] = 0
#     return prime


# ans=[1, 2, 3, 4, 5, 6, 7]
# n=7
# print(Sieve(n))

# 제출 답안
import sys
input = sys.stdin.readline

def Sieve(N):
    is_prime = [1 for _ in range(N + 1)]
    prime = []
    for i in range(2, N + 1):
        if not is_prime[i]:
            continue
        prime.append(i)
        for j in range(2 * i, N + 1, i):
            is_prime[j] = 0
    return prime

N = int(input())
A = [0] + list(map(int, input().split()))
ans = 0

primes = Sieve(N)
# 수열의 앞에서 소수 번째에 위치한 값
for prime in primes:
    ans += A[prime]
        
print(ans)