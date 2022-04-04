"""
나누어 떨어지는 숫자 배열
https://programmers.co.kr/learn/courses/30/lessons/12910

문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

제한사항
arr은 자연수를 담은 배열입니다.
정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
divisor는 자연수입니다.
array는 길이 1 이상인 배열입니다.

입출력 예
arr	             divisor	return
[5, 9, 7, 10]   	5	   [5, 10]
[2, 36, 1, 3]	    1	   [1, 2, 3, 36]
[3,2,6]	            10	    [-1]

입출력 예 설명

입출력 예#1
arr의 원소 중 5로 나누어 떨어지는 원소는 5와 10입니다. 따라서 [5, 10]을 리턴합니다.

입출력 예#2
arr의 모든 원소는 1으로 나누어 떨어집니다. 원소를 오름차순으로 정렬해 [1, 2, 3, 36]을 리턴합니다.

입출력 예#3
3, 2, 6은 10으로 나누어 떨어지지 않습니다. 나누어 떨어지는 원소가 없으므로 [-1]을 리턴합니다.

"""

#제출 답안
def solution(arr, d):
    answer = []
    for i in range(len(arr)):
        if arr[i] % d == 0:
            answer.append(arr[i])

    if len(answer) > 0:
        return sorted(answer)
    else:
        return [-1]


# def solution(arr, divisor): return sorted([n for n in arr if n % divisor == 0]) or [-1]
#
def solution(arr, divisor):
    # print([n for n in arr if n % divisor == 0],'1')
    for n in arr :
        if n % divisor == 0:
            return n
    return sorted([n for n in arr if n % divisor == 0]) or [-1]

# def solution(arr, divisor):
#     answer = []
#     for n in arr:
#         if n % divisor == 0:
#             answer.append(n)
#
#     answer.sort()
#     return answer or [-1]

print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6]	, 10))

a = [1,2,3,4,5]
b = [1,2]

def k (a, b):
     return [n for n in a if n % b == 0]

print(k([1,2,3],2),'k')

"""
정리:
1. 크게 어렵지 않은 난이도.
2. len(answer) >0: 말고 다른 방법이 있을지 확인
-> case #2 로 가능할듯
3. 확실히 #case01이 속도 면이나 용량 면에서 조금 더 좋은 결과가 있음. 한줄로 쓰는 연습을 해야겠다.

다른풀이:
#case01:
def solution(arr, divisor): return sorted([n for n in arr if n % divisor == 0]) or [-1]


#case02:
def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if not answer:
        answer = [-1]

    answer.sort()        
    return answer 
"""