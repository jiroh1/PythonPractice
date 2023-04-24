"""
로그인성공
https://school.programmers.co.kr/learn/courses/30/lessons/120883
"""

def solution(id_pw, db):
    for info in db:
        if id_pw[0] == info[0]:
            if id_pw[1]== info[1]:
                return 'login'
            elif id_pw[1] != info[1]:
                return "wrong pw"
        else:
            pass
    return "fail"

"""
정리
1. 정답률이 높지 않아서 오래 걸릴 줄 알고 남겼는데, 생각보다 금방 해결.
2. :=연산자 공부 위해서 case 1 작성
"""
"""
다른풀이
# case 1
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"


"""