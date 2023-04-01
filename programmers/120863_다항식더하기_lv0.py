"""
다항식 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/120863
"""
# 제출답안
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
        if sum(list(map(int,cons))) == 0:
            answer=t_num
        elif len(cons) > 0 :
            answer+=t_num+' '+ '+' + ' ' + str(sum(list(map(int,cons)))) 
    # 상수만
    elif len(x_var) == 0:
        if len(cons) > 0 :
            answer+=str(sum(list(map(int,cons))))
            
    return answer
"""
정리
1. 총 네번에 제출에 걸쳐서 문제풀이를 끝냈음.
2. 반례를 생각해 내긴 했으나, 힌트를 몇개 보면서 겨우 풀었던 것 같다.
3. 그래도 어느정도는 접근 한 것은 맞았고, 단지 split을 좀 디테일 하게 했으면 조금더 편하게 풀었을 수 있다.
4. 숫자 검색하는 것은 isdigit()을 이용하는 것을 더욱 좋을 듯 매번 try 문으로 int 인지 확인 하는 것으로 했던 것 같다.
5. 3번을 잘했으면 전체적인 코드가 간단해졌을 것 같다.
"""

"""
다른풀이
def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'

"""
"""
# 세번째 문제풀이 10개 통과 ,2개 실패
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
    # 상수만
    elif len(x_var) == 0:
        if len(cons) > 0 :
            answer+=str(sum(list(map(int,cons))))
            
    return answer

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
"""
