'''
x만큼 간격이 있는 n개의 숫자
https://programmers.co.kr/learn/courses/30/lessons/12954#qna
문제 설명
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

제한 조건
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.
입출력 예
x	n	answer
2	5	[2,4,6,8,10]
4	3	[4,8,12]
-4	2	[-4, -8]
'''

x=2
n=5
answer=[]

for i in range(n):
    answer.append(x+(i*x))
print(answer)

'''
정리: 그냥 문제에서 제시해 준 것 기반으로 작성하니 한번에 되어서 당황스러운 문제
    for문을 한줄로 쓰는 연습을 해보는 것과 , def 로 return 해서 출력하는 걸 연습하자.
    
다른 사람 답
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))

'''