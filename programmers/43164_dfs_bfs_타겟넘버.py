"""
타겟 넘버
https://school.programmers.co.kr/learn/courses/30/lessons/43165
"""
# 제출답안
def solution(numbers,target):
    result_list=[0]
    for i in numbers:
        temp=[]
        for j in result_list:
            temp.append(j-i)
            temp.append(j+i)
        result_list = temp
    return result_list.count(target)
            
# 재귀적
# def recursive(numbers, sum, target):
#     if numbers == []:
#         if sum == target:
#             print('!진입')
#             return 1
#         else:
#             return 0
#     return recursive(numbers[1:], sum + numbers[0], target) + recursive(numbers[1:], sum - numbers[0], target)

# def solution(numbers, target):
#     return recursive(numbers, 0, target)


def iterative_solution(numbers, target):
    # result_list는 0부터 시작한다. 그리고, [0, 0-a, 0+a, 0-a-b, 0-a+b, 0+a-b, 0+a+b, ... ] 이런 식으로 간다.
    result_list = [0]

    # i는 numbers의 각 원소들
    for i in range(len(numbers)):
        temp_list = []
        # result_list는 0부터 numbers의 각 원소들을 빼고 더한 값들이 있다.
        for j in range(len(result_list)):
            temp_list.append(result_list[j] - numbers[i])
            temp_list.append(result_list[j] + numbers[i])
        print('#',temp_list)
        result_list = temp_list
        print(result_list)

    return result_list.count(target)
# numbers = [4, 1, 2, 1]
# target = 4 # 2
numbers = [1, 1, 1, 1, 1]
target = 3 # 5
print(iterative_solution(numbers,target))
"""
# 다른 풀이

# case 1
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

# case 2
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
"""
"""
정리
1. 처음에 리스트 안에 리스트를 넣어서 홀수 리스트에 있는 것만 바꾸는 것을 생각함.
"""
"""
문제
n개의 음이 아닌 정수들이 있습니다. 
이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers,
 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.
입출력 예
numbers	         target	return
[1, 1, 1, 1, 1]	 3	    5
[4, 1, 2, 1]	 4	    2
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.

입출력 예 #2
+4+1-2+1 = 4
+4-1+2-1 = 4
총 2가지 방법이 있으므로, 2를 return 합니다.
"""