"""
외계어사전
https://school.programmers.co.kr/learn/courses/30/lessons/120869
"""
# spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1
def solution(spell, dic):
    for word in dic:
        # 한번 씩 사용했으면 길이가 같아야 한다.
        if len(word)==len(spell):
            valid=True
        else:
            valid=False
        # 길이가 같을 경우 실제로 한번씩 사용했는지 확인에 들어간다.
        for alpha in spell:
            if word.count(alpha)==1:
                pass
            else:
                valid=False
        if valid:
            return 1
    return 2
"""
정리
1. 첨에 이전에 모두 제거 할 수 있는 문제랑 헷갈려서 잘 못 풀었음
2. 조합으로 풀어야한다고 생각해서 permmutations 까지 했는데, 거기에서 안에 있는 tuple을 처리하는 것을 못했음.
3. youtube에 참고영상을 보고 해결
4. 다른풀이 로는 set과 sorted를 주로 이용 했음. 
5. case 1 은 sorted(spell)을 for loop 밖에서 지정해 주면 좋을 것 같다.
6. case2 가 set 함수를 이용한 차집합 구하는 것
7. 문제를 자세히 읽었으면 풀 수 있었을 문제. 단, set을 이용하는 것을 잘 생각해야 될듯
"""
"""
다른풀이
# case1
def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2

# case2
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2
"""

"""
참조 
https://www.youtube.com/watch?v=5kPRReabNKU
"""