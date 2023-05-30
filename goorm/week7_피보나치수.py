
# 최종답안
n = int(input())
fibo_results = [0] * (n + 1)
fibo_results[0] = 1
fibo_results[1] = 1

for i in range(2, n):
	fibo_results[i] = fibo_results[i - 1] + fibo_results[i - 2]
result = fibo_results[n-1]
print(result % 1000000007)

# 테스트 케이스 3,4 번 오류
n = int(input())
fibo_results = [0] * (n + 1)
fibo_results[0] = 1
fibo_results[1] = 1

for i in range(2, n):
    fibo_results[i] = fibo_results[i - 1] + fibo_results[i - 2]
    result = fibo_results[i]
print(result % 1000000007)
"""
0~2 에 사이에 있는 값으로 n 값이 지정 되어서 안되는 것으로 확인
그래서 result 함수를 for loop 밖으로 처리 했음.
"""