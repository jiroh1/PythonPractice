"""
옹알이
https://school.programmers.co.kr/learn/courses/30/lessons/120956
"""

def solution(babbling):
    answer = 0
    can_m=["aya", "ye", "woo", "ma"]
    result=[]
    for word in babbling:
        for can in can_m:
            if can in word:
                word=word.replace(can," ")
        result.append(word)
    for res in result:
        res=res.replace(" ","")  # wyeoo 같은 것은 ye를 없애고 돌면서 woo가 되서 " "를 바꾸고 그냥 다음 for문에서 바꾸면서 찾음
        if len(res)<1:
            answer+=1
    return answer

# 수정
def solution(babbling):
    answer = 0
    result=[]
    for word in babbling:
        for can in ["aya", "ye", "woo", "ma"]:
            if can in word:
                word=word.replace(can," ")
        if len(word.strip())==0:
            answer+=1
    return answer


"""
정리
정답률 29 %라서 우선 기록해봄
1. for loop 두개를 써서 각각 비교하면서 하는 것으로 생각 후 아래와 같이 logic 설정
    # babbling 요소 하나씩 꺼내서
    # 그 요소가 can_m에 있는거면 없애면 됨
    # ayaye -> replace 이용해서 can_m을 돌리면서 word랑 비교
    # 그리고 각요소의 len이 0 이상이면 answer + 해서 return 
2. 가능한 발음을 바로 없애니깐 wyeoo같은 것 때문에 발음을 바로 공백으로 변경
3. 받은 결과물을 가지고 다시 공백 없애고 길이로써 체크 해서 풀었음
4. 내가 한 방법을 간단히 한 것이 case 1 인 것 같다.
5. 코드를 조금더 간단히 수정 버젼을 만들 었다.
"""

"""
다른 풀이
# case 1
def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c

# case 2
import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt
"""