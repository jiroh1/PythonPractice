"""
직사각형 별찍기
문제 설명
이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

제한 조건
n과 m은 각각 1000 이하인 자연수입니다.

예시
입력
5 3
출력
*****
*****
*****
"""

a, b = map(int, input().strip().split(' '))
# 위에 줄을 쓰니깐 바로 정답 됬음.
for b in range(b):
#for _ in range(b): # 이렇게 썼어도 됫음 왜냐면 in 앞은 받아 줄 필요가 없는 부분이니깐.
    print(a * '*')

'''
정리: map 하는 것 외에 그냥 for 문 돌렸을 때 정답이 나와서 맞다고 생각했는데, 안되서 위에 map 두고 하니깐 정답
map 관련 참고 :  https://blockdmask.tistory.com/531
-> map(function, iterable), 이 구조가 기본이니깐, function 만들고 list 나 tuple 형태로 iterable 자리에 넣어주면 됨.
# practice/function_map.py
strip 관련 참고 : https://codechacha.com/ko/python-string-strip/
-> 데이터를 받아와서 내가 원하는대로 나누고 거기에서 공백 제거해서 이동할 때 쓰면 될 듯 

1. 우선 input 이 있어서 밑에다가 적어보니, 5,3 으로 했는데 "ValueError: invalid literal for int() with base 10: " 오류 나옴
2. 형 변환이 문제라고 했고, 보니깐, 5,3이 아니라 5 3 으로 해야겠다고 생각들었음 이유는 split(' ')이 되어 있어서 해보니 됨  
3. map 함수원리 알았더라면 굳이 for문 없이 아래 처럼 '\n'으로 했으면됨.
4. 이 문제에선 function 자리에 int로 되어 있으니, 그냥 print 할 생각 했으도 됬을 듯.

다른사람 답 :
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)
=================
a, b = map(int, input().strip().split(' '))
print(('*'*a+"\n")*b)

'''
