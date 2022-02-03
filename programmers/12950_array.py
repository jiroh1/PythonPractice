'''
행렬의 덧셈
https://programmers.co.kr/learn/courses/30/lessons/12950
문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

입출력 예
arr1	arr2	return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	[[3],[4]]	[[4],[6]]
'''
arr1 = [[1],[2]]
arr2 = [[3],[4]]
# arr1 = [[1,2],[2,3]]
# arr2 = [[3,4],[5,6]]
#
# print(len(arr1[0]), arr1[1][1])

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr_sum = []
        for j in range(len(arr1[0])):
            sum = arr1[i][j]+arr2[i][j]
            arr_sum.append(sum)
        answer.append(arr_sum)
    return answer


print(solution(arr1,arr2))
'''
정리 : 
1. for 문 두번 돌리면 되는 것을 처음에 arr1[i][j] 형태로 바로 풀어 버려서 index 오류가 발생했다.
그래서 검색으로 for 문 두번 돌리는 것 확인하고 다시풀이 
2. numpy 써도되는 것이었다... 

다른 답 :
case #1 , 참고 : https://wikidocs.net/32#zip
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

case #2
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A
    
case #3
def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]

case #4
def sumMatrix(A,B):
    answer = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    return answer
    
case #5
import numpy as np
def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()
'''