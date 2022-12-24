"""
큰 수 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/42883
"""
import itertools
# number = "1924" # 94
# k = 2
# number = "1231234" #"3234"
# k = 3
number = "4177252841" # "775841"
k= 4

def solution(number, k): # 시간초과 실패
    return max(list(map(''.join, itertools.combinations(number, k))))

# 최종 제출 답안
def solution1(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0 :
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

# 강사님

def solution2(number, k):
    answer = ''
    # 문자열 내 요소를 숫자로 변환
    number = list(map(int, number))

    now_index = 0
    # 배열 길이 - k만큼 돌고 만약 남으면, 더이상 볼 필요 없음
    for i in range(len(number) - k):
        # 내가 볼 수 있는 부분만 (k+1만큼만 가져옴)
        remains = number[now_index: now_index + k + 1]
        max_value = -1
        max_index = 0
        # 해당 부분 확인하면서 가장 큰 값, index 확인
        for j, v in enumerate(remains):
            # 만약 현재 값이 저장해둔 max_value보다 크면,
            if v > max_value:
                # 최신화
                max_value = v
                max_index = j
            # 단일자리에서 가장 큰 수는 9이기 때문에, 바로 break
            if max_value == 9: break

        # nox_index, k, answer 최신화
        # max_index는 remains의 index니까 (0부터 시작하기 때문에)
        # now_index + max_index 그 다음꺼부터 보기 위해 +1 해줌
        now_index += max_index + 1
        k -= max_index
        answer += str(max_value)

    return answer


print(solution1(number,k))

"""
풀이.
number 를 k만큼 탐색? 완전 탐색 한다면 k만큼이면 시간초과가 날 것이라는 것을 생각해야 함.
1. k개의 숫자를 제거
2. 순서는 보장
  

"""
"""
첫 풀이 과정에서 시간초과가 나서 다른 방법을 찾았음
stack 을 사용하여 진행하는 것으로 다시 진행함 
스택이 쌓이는 것과 동시에 K의 값의 변화를 다뤄주고, 만약에 k가 0이 되지 않으면 
(즉, 앞 숫자와의 관계가 성립되지 않으면 k 가 낮아지지 않고 뒤에 나머지 숫자로 가능한 경우를 적어줌) 
"""

"""
큰 수 만들기

문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
입출력        예
number	       k	return
"1924"	       2	"94"
"1231234"	   3	"3234"
"4177252841"	4	"775841"

"""
"""참고사이트
https://hjp845.tistory.com/158

"""