"""
이상한 문자 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12930
풀이 및 정리 : https://hoon2.notion.site/lv1_12930_-_-_-0813f45ff1304af0a999180286958e59
"""

def solution(s):
    # s : 한개 이상의 단어
    # 문자열 전체의 짝/ 홀수 인덱스가 아님
    # ! 단어( 공백을 기준) 별로 짝/ 홀수 인덱스 를 판단 -> split ?
    # 첫번째는 0번째 인덱스 짝수로 처리

    # 공백을 기준으로 나눈 다음
    word = s.split(" ")
    print(word)
    answer = []
    for i in range(len(word)):
        re_word = ''
        for j in range(len(word[i])):
            if j % 2 == 1:
                re_word += word[i][j].lower()
                # print(re_word)
            else:
                re_word += word[i][j].upper()
        answer.append(re_word)

    answer = ' '.join(answer)
    # 인덱싱에 따라서 대소문자 구분
    # 다시 넣을 때 공백을 추가

    return answer


# s =  " try hello       world" # split(" ") -> TrY HeLlO       WoRlD # split() -> TrY HeLlO WoRlD
s =  "try hello world"      # split(" ") -> TrY HeLlO WoRlD       # split () -> TrY HeLlO WoRlD
     #"TrY HeLlO WoRlD"

print(solution(s))
"""
문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 
각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

입출력 예
s	return
"try hello world"	"TrY HeLlO WoRlD"
입출력 예 설명
"try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다. 
각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 "TrY", "HeLlO", "WoRlD"입니다. 
따라서 "TrY HeLlO WoRlD" 를 리턴합니다.

# 다른 사람 풀이 
def toWeirdCase(s):
    res = []
    for x in s.split(' '):
        word = ''
        for i in range(len(x)):
            c = x[i].upper() if i % 2 == 0 else x[i].lower()
            word = word + c
        res.append(word)
    return ' '.join(res)
    
-> 중간에 if 문 한줄로 하는 것 참고 

def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
    -> 한줄풀이 
"""