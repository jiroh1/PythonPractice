"""
컨트롤 제트
https://school.programmers.co.kr/learn/courses/30/lessons/120853
"""
# 제출 답안
def solution(s):
    stack=[]
    for num in s.split():
        try:
            stack.append(int(num))
        except:
            if stack:
                stack.pop()
    return sum(stack)


"""
정리
1. replace로 인덱싱의 -1을하여 대체하려고 했으나 안되었다.
2. try, except을 이용하여 음수 까지 해결 할 수 있는 방법으로 stack을 사용
"""
"""
다른풀이
# case1) 처음 생각한 문제풀이와 유사함
anwer이 있으니, 굳이 교체할 필요없이 앞에 것으로 빼면 되는 것이었다.
def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer


"""
"""
참고
stack의 개념을 잘 알 수 있게 해준 정리 글
https://chan-lab.tistory.com/30
"""