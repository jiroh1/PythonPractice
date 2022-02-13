'''
문자열 다루기 기본
https://programmers.co.kr/learn/courses/30/lessons/12918

문제 설명
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.

입출력 예
s	return
"a234"	false
"1234"	true
'''
import math
def solution(s):
    if len(s) == 4 or len(s) ==6:
        return s.isdigit()
    else :
        return False
print(solution("123b4"))

'''
정리: 1. 갑자기 isdigit의 기능이 생각나서 검색해서 찾아냄.
2. case#2 처럼 try , except 도 생각 했으나, isdigit 생각나서 쉽게 끝남.
3. 그러나 문자열 길이 4혹은 6 이것 때문에 첨에 안됫었음.
4. case#3 은 정규식 이용 인데 , 알고 있으면 좋을 듯함. 

다른 풀이:
case #1
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)


case#2
def alpha_string46(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 

case #3
def alpha_string46(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))
    
# ^와 $는 문자열의 처음과 끝을 의미합니다. \d는 숫자를 의미하구요, {4}|{6}은 숫자가 4번 혹은 6번 반복되는 것을 찾는 거구요, 결과를 bool로 true/false로 리턴하게 하는 코드입니다
'''