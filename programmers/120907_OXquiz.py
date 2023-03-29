"""
OX퀴즈
https://school.programmers.co.kr/learn/courses/30/lessons/120907
"""

def solution(quiz):
    return ["O" if eval(q.split('=')[0])==int(q.split('=')[-1]) else "X" for q in quiz ]


"""
정리
1. 한번에 잘 풀었지만 남긴 이유는 list comprehension에 대해서 for loop 안에 if 를 쓸 경우 안된적이 있어서 그냥 풀었는데 해결하기 위함.
2. for 문을 맨 뒤로 넣고 그안에 있는 if 문을 앞에 넣는 식으로 하면 될 듯.
3. 이전은 ["O" for q in quiz if eval(q.split('=')[0])==int(q.split('=')[-1]) else "X" ] 이렇게 썼었다.
"""