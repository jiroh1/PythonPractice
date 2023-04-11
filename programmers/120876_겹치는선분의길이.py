"""
겹치는 선분의 길이
https://school.programmers.co.kr/learn/courses/30/lessons/120876
"""

# 제출답안 
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

# lines=[[0, 1], [2, 5], [3, 9]]
# lines=[[-1, 1], [1, 3], [3, 9]]
lines=	[[0, 5], [3, 9], [1, 10]]
# lines=[[0, 8], [0, 2], [6, 8]]

print(solution(lines))


"""
제출답안
#case 1) 1,9 실패임
def solution(lines):
    # 선분은 세개 각각 범위 만들어서 set 해서 원소 갯수 설정하는게 좋을듯
    # 선분 만들기 
    line1 = [i for i in range(lines[0][0], lines[0][1]+1)]
    line2 = [i for i in range(lines[1][0], lines[1][1]+1)]
    line3 = [i for i in range(lines[2][0], lines[2][1]+1)]
    # 교집합해서 겹치는 부분 
    d1=list(set(line1)&set(line2))
    d2=list(set(line2)&set(line3))
    d3=list(set(line3)&set(line1))    
    
    temp=[]
    if len(d1)>1:
        temp.append(d1)
    if len(d2)>1:
        temp.append(d2)
    if len(d3)>1:
        temp.append(d3)
    print(temp)    
    if len(temp) == 0:
        return 0
    elif len(temp) == 1:
        return len(range(min(set(temp[0])),max(set(temp[0]))))
    elif len(temp) == 2:   
        return len(range(min(set(temp[0]+temp[1])),max(set(temp[0]+temp[1]))))
    elif len(temp) == 3:   
        return len(range(min(set(temp[0]+temp[1]+temp[2])),max(set(temp[0]+temp[1]+temp[2]))))
"""
"""
다른풀이
# case 1
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

# case 2
def solution(lines):
    result=0
    # 2 개의 구간이 겹치는 부분
    for idx in range(3): # 0, 1, 2
        l1, l2 = lines[idx-1], lines[idx]
        l1s,l1e = l1[0],l1[1]
        l2s,l2e = l2[0],l2[1]
        start_max = max(l1s,l2s)
        end_min = min(l1e,l2e)
        if start_max < end_min:
            result += end_min - start_max
    # 3개 구간이 겹치는 부분
    l1, l2, l3 = lines[0], lines[1], lines[2]
    l1s,l1e = l1[0],l1[1]
    l2s,l2e = l2[0],l2[1]
    l3s,l3e = l3[0],l3[1]
    start_max = max(l1s,l2s,l3s)
    end_min = min(l1e,l2e,l3e)
    if start_max < end_min:
        result -= (end_min - start_max) * 2
    return result

# case 3
def solution(lines):
    table = [set([]) for _ in range(200)]
    for index, line in enumerate(lines):
        a, b = line
        for i in range(a, b):
            table[i + 100].add(index)

    count = 0
    for line in table:
        if len(line) > 1:
            count += 1

    return count

"""
"""
정리
1. 선분은 세개 각각 범위 만들어서 set 해서 원소 갯수 (범위)  길이 확인하는게 좋을 것 같다.
2. 교집합을 잘이용하였으나, 합집합을 이용하지 못하여 range에 대해서 잘 구분을 못했다.
"""
"""
참고
https://velog.io/@damin1025/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B2%B9%EC%B9%98%EB%8A%94-%EC%84%A0%EB%B6%84%EC%9D%98-%EA%B8%B8%EC%9D%B4
https://www.youtube.com/watch?v=nHA057fwZ54
https://ryong9rrr.github.io/pgm-Lv0-%EA%B2%B9%EC%B9%98%EB%8A%94-%EC%84%A0%EB%B6%84%EC%9D%98-%EA%B8%B8%EC%9D%B4/
"""