"""
2016년
https://programmers.co.kr/learn/courses/30/lessons/12901

2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

제한 조건
2016년은 윤년입니다.
2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

입출력 예
a	b	result
5	24	"TUE"
"""


def solution(a, b):
    dow = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    chek = sum(days[:a-1]) + b + 4
    k = chek % 7
    answer = dow[k]

    return answer


# print(solution(5, 24))  # TUE
print(solution(1, 1))  # FRI
print(solution(1, 2),22)
print(solution(1, 3),33)
print(solution(1, 4),44)
print(solution(1, 5),55)
print(solution(1, 6),66)
print(solution(1, 7),77)

# print(solution(9, 13))  #
# print(solution(11, 4))
# print(solution(12, 4))
"""
 
1월 1일 금요일 days[5]
1/2 토 days[6]
1/3 일 days[0]
1/4 월 days[1]
1/5 화 days[2]
1/6 수 days[3]
1/7 목 days[4]

"""
'''
정리 :  어렵지 않았는데, 숫자 몇 개를 정리하면서 오히려 헷갈렸던 듯

# case 01
def getDayName(a,b):
    week=['FRI','SAT','SUN','MON','TUE','WED','THU']
    month=[31,29,31,30,31,30,31,31,30,31,30,31]

    return week[(sum(month[:a-1])+(b-1))%7]
    
# case 02 : 오히려 제출답 보다 느린케이스가 있음
solution = lambda a, b: ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"][(sum([0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:a]) + b) % 7]

#case 03 느린케이스도 있으나 용량적으로 적은 경우도 있음
import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]



'''