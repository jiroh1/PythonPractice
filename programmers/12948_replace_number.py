'''
핸드폰 번호 가리기
https://programmers.co.kr/learn/courses/30/lessons/12948

프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
phone_number는 길이 4 이상, 20이하인 문자열입니다.
입출력 예
phone_number	return
"01033334444"	"*******4444"
"027778888"	"*****8888"

'''


# 제출 후 다시 푼 답안


def solution(phone_number):
    return phone_number.replace(phone_number[:-4], '*' * (len(phone_number) - 4))


print(solution("027778888"))

'''
제출답안 :
def solution(phone_number):
    phone_number = str(phone_number)
    len_phone = len(phone_number)
    answer = phone_number.replace(phone_number[:-4], '*' * (len_phone - 4))
    return answer

정리 :
1. phone_nubmer가 어떻게 들어오는지 이미 봤으면 굳이 str으로 형변환 안했어도 됬음.
2. 그렇게 되면 바로 len(phone_number) 했으면 됬음
다른 풀이:
# case 01
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]
     
'''
