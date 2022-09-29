"""
음양더하기
https://school.programmers.co.kr/learn/courses/30/lessons/76501
"""
# 제출답안
def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] != True:
            absolutes[i] = (-absolutes[i])

    return sum(absolutes)


absolutes=[4,7,12]
signs=[True,False,True]
# result=9

# absolutes=[1,2,3]
# signs=[False,False,True]
# result=0

print(solution(absolutes,signs))
"""
문제 설명
어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

제한사항
absolutes의 길이는 1 이상 1,000 이하입니다.
absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
signs의 길이는 absolutes의 길이와 같습니다.
signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.
입출력 예
absolutes	signs	result
[4,7,12]	[true,false,true]	9
[1,2,3]	[false,false,true]	0
입출력 예 설명
입출력 예 #1

signs가 [true,false,true] 이므로, 실제 수들의 값은 각각 4, -7, 12입니다.
따라서 세 수의 합인 9를 return 해야 합니다.
입출력 예 #2

signs가 [false,false,true] 이므로, 실제 수들의 값은 각각 -1, -2, 3입니다.
따라서 세 수의 합인 0을 return 해야 합니다.


case#1 "!=True"
테스트 1 〉	통과 (0.08ms, 10.4MB)
테스트 2 〉	통과 (0.09ms, 10.1MB)
테스트 3 〉	통과 (0.10ms, 10.1MB)
테스트 4 〉	통과 (0.09ms, 10.2MB)
테스트 5 〉	통과 (0.09ms, 10.3MB)
테스트 6 〉	통과 (0.08ms, 10.1MB)
테스트 7 〉	통과 (0.08ms, 10.1MB)
테스트 8 〉	통과 (0.09ms, 10.1MB)
테스트 9 〉	통과 (0.09ms, 10MB)

case#2 "==False"
테스트 1 〉	통과 (0.08ms, 10.1MB)
테스트 2 〉	통과 (0.14ms, 10.2MB)
테스트 3 〉	통과 (0.09ms, 10.2MB)
테스트 4 〉	통과 (0.10ms, 10.2MB)
테스트 5 〉	통과 (0.16ms, 10.1MB)
테스트 6 〉	통과 (0.14ms, 10.1MB)
테스트 7 〉	통과 (0.08ms, 10.4MB)
테스트 8 〉	통과 (0.09ms, 10.2MB)
테스트 9 〉	통과 (0.09ms, 10.2MB)

#정리 
!= , ==의 차이를 더욱 확인해봐도 될듯
한줄도 좋지만 아직은 나는 눈에 보이는 코드가 낫다고 생각 

#다른 사람풀이

case #1

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
"""