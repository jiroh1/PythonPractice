"""
소인수분해
https://school.programmers.co.kr/learn/courses/30/lessons/120852
"""
n=12

def solution(n):
    answer = []
    
    x = 2
    while x <= n:
        if n % x == 0:
            if x not in answer:
                answer.append(x)
            n //= x
        else:
            x += 1
    return answer

"""
테스트 케이스만 통과되고 제출 시 몇개 안됨.
def solution(n):
    answer = []
    for i in range(2,n+1):
        if n % i ==0:
            if i not in answer:
                answer.append(i)
            n //=i
        else:
            i+=1
    return sorted(set(answer))

print(solution(n))
"""

"""
정리
1. 소인수 분해 문제들에 대해서 항상 애를 먹으니 자세히 봐야할듯
2. for 문 사용한 것은 안됨, while문에 대한 것에 매커니즘을 정확히 확인해야 할듯 
"""

"""
참고
- 프로그래머스 질문 게시판에 나와 있는 좋은 설명
2부터 시작해서 n까지 범위로 잡고 n에서 나누기 시작합니다.
물론 같은수가 여러번 나누어 질 수 있기 때문에 while문으로 조건에 맞는 동안에는 계속 나눕니다.
그렇게 n이 1이 될 때까지 나누게 된다면,
정답에 추가된 값은 자연스럽게 소수가 됩니다.
왜냐구요?
어떤 수가 나눠진다고 했을 때, 나누어질때까지 while문을 계속 돌리기 때문입니다.
합성수의 원천은 소수의 곱으로 이루어져있기 때문에, 첫 소수인 2부터 시작해서 2로 나눌 수 있을 때 까지
계속 n으로 나누고, 그 다음 수로 올려서 반복하면, 자연스럽게 나누어지는 수는 소수만 해당됩니다.
애초부터 소수의 정의가 그러기에, 당연한 결과가 됩니다.
이 문제는 이런 기본적인 수학적 바탕을 깔고, 그걸 코드로 구현가능한지를 물어보고 싶어하는 것 같습니다.

"""