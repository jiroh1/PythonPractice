'''
Step1-3. 문제 먼저 직접 풀어보기 "가장 큰 수"
프로그래밍1
27/ 100.0 미완료

문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
'''

#1 < len(numbers) < 100,000
#0 < numbers[i] < 1,000
# 문자열로 바꾸어 return

from itertools import permutations

def solution(numbers):
    # for i in range(len(numbers)): # numbers 요소를 int->str , join 사용을 위해
    #     numbers[i] = str(numbers[i])
    #numbers = list(map(str,numbers))
    #print(numbers,type(numbers),'numbers',type(numbers[0]))
    n = len(numbers)
    per = list(permutations(numbers,n))
    per_a = []
    # print(per,type(per),'per')
    answer = ''
    for i in range(len(per)):
       per[i] = list(per[i])
       print(per[i],'p',type(per[i]),per[i][0],type(per[i][0]) , 'check')
       for _ in range(len(per[i])):
           per[i][_] = str(per[i][_])
       a = ''.join(per[i])
       print(a,type(a))
       per_a.append(a)
       #print(per_a,'per_a')
    answer+=max(per_a)
    #print(answer,type(answer))
    return int(answer)


print(f'순서를 재배치하여 만들 수 있는 가장 큰 수는 : {solution([3, 30, 34, 5, 9])}')


#
# numbers = [1,2,3,4,5]
#
# for i in range(len(numbers)):
#     numbers[i]=str(numbers[i])
# print((''.join(numbers)),'예시')
# ls = list(combinations(numbers,3))
# print(ls,'ls')
# ls_b =[]
# ans = ''
# for i in range(len(ls)):
#     ls[i] = list(ls[i])
#     print(ls[i],type(ls[i]),'!')
#     b = ''.join(str(ls[i]))
#     print(b,'b')
#     ls_b.append(b)
# print(ls_b,'ls_b')
# print(max(ls_b), '최대값')
# ans+=max(ls_b)
#
# print(int("".join(ls)))

# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]

'''
제출 답안:
from itertools import permutations

def solution(numbers):
    numbers = list(map(str,numbers)) # numbers 요소를 int->str , join 사용을 위해
    n = len(numbers)
    per = list(permutations(numbers,n))
    per_a = []
    answer = ''
    for i in range(len(per)):
        per[i] = list(per[i])
        a = ''.join(per[i])
        per_a.append(a)
    answer+=max(per_a)
    return answer
    
참고 
순열 : https://potensj.tistory.com/110
최대 값 : https://devpouch.tistory.com/71
정답 : https://wooaoe.tistory.com/82

'''