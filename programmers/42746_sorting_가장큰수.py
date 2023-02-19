"""
가장 큰 수
https://school.programmers.co.kr/learn/courses/30/lessons/42746
"""
# numbers=[6, 10, 2]	# "6210"
numbers=[3, 30, 34, 5, 9]	# "9534330"

def solution(numbers):
    numbers = list(map(str, numbers))
    print('1:',numbers)
    numbers.sort(key=lambda x: x * 3, reverse=True)
    print('2:',numbers)
    return str(int(''.join(numbers)))

print("정답은 : ",solution(numbers))

"""
정리
1. 첫번째 제출 답안에서 시간초과로 오답이 나온 것을 확인해서 permutations 을 쓰면 안된다고 생각.
2. 결국 이런 경우엔 ascii code 를 많이 쓰는 것 같아서 생각 했는데, 생각만 하고 실행하지 못함.
3. 제약 조건에서 원소가 총 1,000 이하이니깐 3자리로 맞춰서 sorting 함
    3을 곱하는 이유는 2번째 예시를 풀 때 이유를 알게 된다.
    계산할 때 사전값으로만 정렬을 한다면 [9,5,34,30,3] 이렇게 정렬된다.
    하지만 3이 30보다 앞에 와야한다.
    number는 1000이하의 숫자이므로 최대값을 생각해 3을 곱해줬고,
    3을 곱하게 되면 [999, 555, 343434, 303030, 333] 이렇게 될 것이고, 정렬을 하게 되면 [999, 555, 343434, 333, 303030]이 된다.
"""
"""
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
"""
"""
첫번째 제출 답안 -  시간 초과로 오답 / 답은 나옴
from itertools import permutations

def solution(numbers):
    checklist=[]
    mixed_number=permutations(numbers)
    for mix in mixed_number:
        number_per=''.join(map(str,mix))
        checklist.append(number_per)
    answer=max(checklist)       
    return answer

print("정답은 : ",solution(numbers))
"""
"""
error:
TypeError: sequence item 0: expected str instance, int found
https://steadily-worked.tistory.com/717
"""