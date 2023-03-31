"""
다항식 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/120863
"""


# 두번재 문제풀이 7개 통과, 5개 실패 
def solution(polynomial):
    var=[]
    cons=[]
    
    # 변수, 상수 나누기
    for i in polynomial.split(" "):
        try:
            temp=int(i)
            cons.append(i)
        except:
            var.append(i)
            
    # 연산자 없애주기
    x_var=[v for v in var if "x" in v]

    # 변수 더하기
    t_num = 0
    answer = ''
    if len(x_var) > 1:
        for x in x_var:
            if len(x) == 1:
                t_num += 1
            elif len(x) > 1:
                t_num+=int(x[:-1])
        # 상수가 있는지 없는지 확인과 변수가 있는지 없는지 확인
        if t_num > 0 :
            answer=str(t_num)+'x'
        if len(cons) > 0 :
            answer+=' '+ '+' + ' ' + str(sum(list(map(int,cons))))

    elif len(x_var) == 1:
        t_num=x_var[0]
        if len(cons) > 0 :
            answer+=t_num+' '+ '+' + ' ' + str(sum(list(map(int,cons))))

    return answer

# 첫번째 문제풀이  여섯개 통과 , 3개 런타임 에러 , 3개 실패 
def solution(polynomial):
    # x, + , digit
    # 공백이 있다고 하니 split
    var=[]
    cons=[]
    
    # 변수, 상수 나누기
    for i in polynomial.split(" "):
        try:
            temp=int(i)
            cons.append(i)
        except:
            var.append(i)
            
    # 연산자 없애주기
    x_var=[v for v in var if "x" in v]

    # 변수 더하기
    t_num=0
    for x in x_var:
        if len(x) == 1:
            t_num += 1
        elif len(x) > 1:
            t_num+=int(x[:-1])

    # 상수가 있는지 없는지 확인과 변수가 있는지 없는지 확인
    if t_num > 0 :
        answer=str(t_num)+'x'
    if len(cons) > 0 :
        answer+=' '+ '+' + ' ' + str(sum(list(map(int,cons))))
        
    return answer