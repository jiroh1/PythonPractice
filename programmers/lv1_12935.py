"""
제일 작은 수 제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/12935
"""

# 제출답안
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        find_num = min(*arr)
        arr.remove(find_num)
    return arr


arr = [4, 3, 2, 1]
# arr = [10]

print(solution(arr))
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0
"""
문제 설명
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

제한 조건
arr은 길이 1 이상인 배열입니다.
인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.
입출력 예
arr	return
[4,3,2,1]	[4,3,2]
[10]	[-1]

다른 풀이:
#case1

def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)] or [-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4,3,2,1]
print("결과 {} ".format(rm_small(my_list)))

->아마 문제 변형 전 인 것 같음 -1 return에 대한 예제가 없었던 것 같다.
테스트 1 실패 하는 풀이
채점 결과
정확성: 93.8
합계: 93.8 / 100.0
"""
