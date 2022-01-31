'''
평균 구하기
https://programmers.co.kr/learn/courses/30/lessons/12944?language=python3

문제 설명
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

제한사항
arr은 길이 1 이상, 100 이하인 배열입니다.
arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

입출력 예
arr	return
[1,2,3,4]	2.5
[5,5]	5

'''
arr = [1, 2, 3, 4]


def solution(arr):
    answer = 0

    for i in range(len(arr)):
        answer += arr[i] / len(arr)
    return answer


a = solution(arr)
print(a, 'answer')

'''
정리 : +=가 생각이 안나다가 생각이 났다.
앞으로 list가 아니라 단순 숫자를 그냥 'answer = 0' 형태로 할 진행할 떄 
+= 와 같은 기호를 까먹지 않으면 됨
case 1 에서 볼 수 있듯, sum 함수 쓰면 된다...
case 2 에서는 zerodivisionerror 피할 수 있다. (분모 0)
case 3 statistics module을 사용해서 기입하였다. 

다른사람 답 
case #1
def average(list):
    return (sum(list) / len(list))

=======
case #2    
def average(list):
    # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
    if len(list) == 0:
        return 0

    return sum(list) / len(list)
    
=====
case #3
import statistics

def average(list):
    # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
    return statistics.mean(list)
'''