"""
H-Index
https://school.programmers.co.kr/learn/courses/30/lessons/42747
"""
# citation의 길이 = n
# 원소의 값이 인용된 수 
# 인용된 수와 그 수의 해당하는 값의 갯수가 같으면 그것이 H-INDEX
# H-INDEX : 인용된 수와 그 수의 해당하는 값의 갯수가 같은 수
 # n 안에서 원소 하나가 자기보다 같거나 큰 숫자의 갯수를 구하고 , 그 갯수가 자기랑 같의면 return


# 최종 제출 답안
def solution(citations):
    citations=sorted(citations)
    # [0, 1, 3, 5, 6]
    n=len(citations)
    print(n)
    for i in range(n):
        # print(i)
        if citations[i]>= n-i:
            return n-i
    return 0

# citations = [7,0,0]
citations = [3, 0, 6, 1, 5] # 	return 3

print(solution(citations))

"""
정리
1. 문제 자체를 제대로 이해하지 못해서 답보고 겨우 이해함
2. h가 증가함에 따라서 2가지 조건의 부합하는지 확인하여 max 값을 찾으면 된다.
2-1 조건 1) 인용횟수가 h보다 크거나 같은 논문이 h개이상, 조건 2) 나머지 논문의 인용횟수가 h보다 작거나 같아야함.
3. "citations[i]>= n-i" 은 문제에서 주어진 "h번 이상 인용된 논문이 h편 이상" 이라는 조건을 그대로 풀어쓴 것
3-1. "citations[i] "는 i번 논문이 인용된 횟수, "l-i"는 인용된 논문의 개수 를 최대값부터 하나씩 줄여나간 것.
"""
"""
H-Index
문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 
어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 
위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
입출력 예
citations	return
[3, 0, 6, 1, 5]	3
입출력 예 설명
이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 
그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.
"""
"""
첫번째 제출 답안 - 시간초과

def solution(citations):
    answer = 0

    # n 편 중
    for i in range(len(citations)):
        check = citations[i] # 3
        # citation 에서 check 보다 높거나 같은지 ?
        counting = 0
        for j in citations:
            # print('j :  ',j,' / check : ',check)
            if j >= check:
                # print('###')
                counting += 1
            # print('couting : ', counting)

        if counting == check:
            # print('!!!!')
            answer = counting
            return answer
        else:
            # print('@')
            answer = 0
            continue
    return answer
"""
"""
다른 사람 풀이

case1)
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

case2)
def solution(citations):
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        if i >=citation:
            return i
    return len(citations)

"""
"""
참고사이트
https://velog.io/@jiffydev/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-89-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-H-Index
https://jokerldg.github.io/algorithm/2021/06/01/h-index.html
https://walwalgabu.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%EC%A0%95%EB%A0%ACH-INDEX-%ED%8C%8C%EC%9D%B4%EC%8D%ACpython
"""