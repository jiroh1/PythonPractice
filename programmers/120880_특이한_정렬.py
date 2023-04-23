"""
특이한 정렬
https://school.programmers.co.kr/learn/courses/30/lessons/120880
"""

# n과 가까운 순으로 answer 넣기
# 뺀 list 를 만들기 
# [-3, -2, -1, 0, 1, 2]

def solution(numlist, n):
    sort_list=[[abs(num-n),-num] for num in numlist]
    sort_list = sorted(sort_list)
    return [-num for _ , num in sort_list]


numlist=[1, 2, 3, 4, 5, 6]
n=4

print(solution(numlist,n))


"""
정리
1. abs를 이용하여 각 수의 거리를 구해서 가까운 수를 찾으면 된다고 생각함.
2. 그 다음이 진행이 안되서, 결국 시간 내에 풀지 못했음.
3. [[3, -1], [2, -2], [1, -3], [0, -4], [1, -5], [2, -6]] 이런식으로 comprehension 되고 sort 하면 [[0, -4], [1, -5], [1, -3], [2, -6], [2, -2], [3, -1]]
4. 그래서 다시 list 를 풀어주면서 값에 '-'만 붙여주면 된다.
5. lambda를 이용해서 풀 수 있도록 익혀야 겠다.
"""
"""
다른풀이
def solution(numlist, n):
    answer = sorted(numlist, key = lambda x : (abs(x-n), n-x))
    return answer
"""
"""
참고
https://www.youtube.com/watch?v=V9MFm70tNhc
https://velog.io/@damin1025/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8A%B9%EC%9D%B4%ED%95%9C-%EC%A0%95%EB%A0%AC
"""