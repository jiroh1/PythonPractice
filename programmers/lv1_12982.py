"""
예산
https://school.programmers.co.kr/learn/courses/30/lessons/12982
"""
# 제출 답안
def solution(d,budget):
    d.sort()
    while budget < sum(d):
        d.pop()
        print(d)
    return len(d)

d = [1,3,2,5,4]
budget = 9	#3
# d = [2,2,3,3]
# budget = 10
#4

print(solution(d,budget))
"""
문제 설명
S사에서는 각 부서에 필요한 물품을 지원해 주기 위해 부서별로 물품을 구매하는데 필요한 금액을 조사했습니다. 
그러나, 전체 예산이 정해져 있기 때문에 모든 부서의 물품을 구매해 줄 수는 없습니다. 
그래서 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.

물품을 구매해 줄 때는 각 부서가 신청한 금액만큼을 모두 지원해 줘야 합니다. 
예를 들어 1,000원을 신청한 부서에는 정확히 1,000원을 지원해야 하며, 1,000원보다 적은 금액을 지원해 줄 수는 없습니다.

부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.

제한사항
d는 부서별로 신청한 금액이 들어있는 배열이며, 길이(전체 부서의 개수)는 1 이상 100 이하입니다.
d의 각 원소는 부서별로 신청한 금액을 나타내며, 부서별 신청 금액은 1 이상 100,000 이하의 자연수입니다.
budget은 예산을 나타내며, 1 이상 10,000,000 이하의 자연수입니다.

입출력 예
d	budget	result
[1,3,2,5,4]	9	3
[2,2,3,3]	10	4

입출력 예 설명
입출력 예 #1
각 부서에서 [1원, 3원, 2원, 5원, 4원]만큼의 금액을 신청했습니다. 만약에, 1원, 2원, 4원을 신청한 부서의 물품을 구매해주면 예산 9원에서 7원이 소비되어 2원이 남습니다. 
항상 정확히 신청한 금액만큼 지원해 줘야 하므로 남은 2원으로 나머지 부서를 지원해 주지 않습니다. 위 방법 외에 3개 부서를 지원해 줄 방법들은 다음과 같습니다.

1원, 2원, 3원을 신청한 부서의 물품을 구매해주려면 6원이 필요합니다.
1원, 2원, 5원을 신청한 부서의 물품을 구매해주려면 8원이 필요합니다.
1원, 3원, 4원을 신청한 부서의 물품을 구매해주려면 8원이 필요합니다.
1원, 3원, 5원을 신청한 부서의 물품을 구매해주려면 9원이 필요합니다.
3개 부서보다 더 많은 부서의 물품을 구매해 줄 수는 없으므로 최대 3개 부서의 물품을 구매해 줄 수 있습니다.

입출력 예 #2
모든 부서의 물품을 구매해주면 10원이 됩니다. 따라서 최대 4개 부서의 물품을 구매해 줄 수 있습니다.의

문제풀이 시  찾아본 것
# 조합 방법 
# https://ourcstory.tistory.com/414
# combination과 permutation은 iterable 객체임 
# enumberate
# https://www.daleseo.com/python-enumerate/

제출답안 
# case 1 -> 시간초과 
from itertools import combinations
def solution(d, budget):
    answer = 0
    booseo_number = 1
    while booseo_number <= 100:
        booseo = list(combinations(d, booseo_number))
        for i, part in enumerate(booseo,start=1):
            sum_part = sum(part)
            if sum_part <= budget:
                print(i,part)
                answer = len(part)
        booseo_number += 1

    # answer = 지원할 수 있는 부서 개수
    return answer
    
# -> enumerate 필요 없는듯 굳이 

# case 2 

def solution(d, budget):
    d.sort()
    cnt = 0
    for i in d :
        budget -= i
        if budget < 0 :
               break
        cnt += 1
    answer = cnt
    return answer
    
# 정리 
1. combination 을 쓸 필요가 없었던 문제, combination을 쓰다보니 시간이 많이 걸림
2. 가장 적은 부서부터 물품을 구매해 주는 방법으로 진행하기 위해서 sort
3. 다 더하면서 뒤에서 부터 하나씩 가능한지 빼가는 방법
"""