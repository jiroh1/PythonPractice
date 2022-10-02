# Ascii code
"""
시저 암호
https://school.programmers.co.kr/learn/courses/30/lessons/12926
풀이 및 정리 : https://hoon2.notion.site/LV1_12926_-0f1c9260a9254018a21ddce57304cb41
"""
# https://m.post.naver.com/viewer/postView.nhn?volumeNo=9638345&memberNo=34331610

# 풀이 전 생각
# s는 알파벳(소문자,대문자) 공백 으로 이루어져잇다.
# 공백은 공백이다.


def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)

# s = "AB"
# n = 1
# result "BC"
#
# # s = "z"
# # n = 1
# # result "a"
#
s = "a B z"
n = 4
# result "e F d"
print(solution(s, n))

# s에 대해서 n만큼 움직이면 s가 다르게 출력
# 대문자, 소문자 구별 해야됨
# z에서 밀면 a가 됨 -> 한 뭉텅이의 string이 아니라 각각의 자리의 알파벳의 순서가 변하는 것임. 번호 좌물쇠 같이


"""
문제 설명
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.
입출력 예
s	n	result
"AB"	1	"BC"
"z"	1	"a"
"a B z"	4	"e F d"

참고 사이트
https://angelplayer.tistory.com/193

진행할 때 확인 했던 것들
스트링의 인덱싱되는지 프린트 찍어
소,문자 대문자 할때 함수뒤에 ()안 붙여서 찍어봄 

#정리
1. ascii code 를 사용해서 a-z list 로 인덱싱을 할 생각 이엇다.
2. 그러면 ord()도 검색 시 알 수 있었을텐데 그것을 알지 못해서 정확한 길로 갈 수 없었다.
3. 마지막 예시 보면 a B z 이므로 그냥 각각의 자리에서 밀려지는 것이었는데, 세개를 동시에 미루는 것으로 생각해서 애초에 잘못 생각함.
-> 번호 좌물쇠 움직이는 방식으로 생각했어야 함. 

# 다른 사람 풀이
def caesar(s, n):
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = []

    for i in s:
        if i is " ":
            result.append(" ")
        elif i.islower() is True:
            new_ = lower_list.find(i) + n
            result.append(lower_list[new_ % 26])
        else:
            new_ = upper_list.find(i) + n
            result.append(upper_list[new_ % 26])
    return "".join(result)
"""
# 참고함수

# ord
def ord(__c: [str, bytes]) -> int:
    pass
#Return the Unicode code point for a one-character string.

# chr
def chr(__i: int) -> str:
    pass
# Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10 ffff.


# 풀이 실패

from string import ascii_lowercase

alpha_list = list(ascii_lowercase)


def my_answer(s, n):
    # 들어오는 문자열의 대,문자 구분
    alp_check = []
    for alphabet in s:
        if alphabet.isupper() == True:
            alp_check.append(True)
        else:
            alp_check.append(False)

    # s의 첫번째 문자를 alph_list에서 찾기
    for point in range(len(alpha_list)):
        if s[0].lower() == alpha_list[point]:
            starting_point = point

    # n 더한 후 시작 지점 지정
    answer_starting = starting_point + n
    # 지정한 위치의 대,소문자 구분전 답안
    len_s = len(s) + 1
    before_answer = alpha_list[answer_starting:len_s]

    # 대소문자 구별
    answer = ''
    for i in range(len(alp_check)):
        if alp_check[i]:
            answer += before_answer[i].upper()
        else:
            answer += before_answer[i].lower()

    return answer
# -> 이렇게 하니깐 안되는 이유는 z -> a로 넘어가는 것이 안됨.