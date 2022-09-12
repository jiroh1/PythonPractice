"""
로또의 최고 순위와 최저 순위
https://school.programmers.co.kr/learn/courses/30/lessons/77484?language=python3

문제 설명
로또 6/45(이하 '로또'로 표기)는 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권입니다. 아래는 로또의 순위를 정하는 방식입니다. 1

순위	당첨 내용
1	6개 번호가 모두 일치
2	5개 번호가 일치
3	4개 번호가 일치
4	3개 번호가 일치
5	2개 번호가 일치
6(낙첨)	그 외
로또를 구매한 민우는 당첨 번호 발표일을 학수고대하고 있었습니다. 하지만, 민우의 동생이 로또에 낙서를 하여, 일부 번호를 알아볼 수 없게 되었습니다. 당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.
알아볼 수 없는 번호를 0으로 표기하기로 하고, 민우가 구매한 로또 번호 6개가 44, 1, 0, 0, 31 25라고 가정해보겠습니다. 당첨 번호 6개가 31, 10, 45, 1, 6, 19라면, 당첨 가능한 최고 순위와 최저 순위의 한 예는 아래와 같습니다.

당첨 번호	31	10	45	1	6	19	결과
최고 순위 번호	31	0→10	44	1	0→6	25	4개 번호 일치, 3등
최저 순위 번호	31	0→11	44	1	0→7	25	2개 번호 일치, 5등
순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정됩니다.
알아볼 수 없는 두 개의 번호를 각각 10, 6이라고 가정하면 3등에 당첨될 수 있습니다.
3등을 만드는 다른 방법들도 존재합니다. 하지만, 2등 이상으로 만드는 것은 불가능합니다.
알아볼 수 없는 두 개의 번호를 각각 11, 7이라고 가정하면 5등에 당첨될 수 있습니다.
5등을 만드는 다른 방법들도 존재합니다. 하지만, 6등(낙첨)으로 만드는 것은 불가능합니다.
민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다. 이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

제한사항
lottos는 길이 6인 정수 배열입니다.
lottos의 모든 원소는 0 이상 45 이하인 정수입니다.
0은 알아볼 수 없는 숫자를 의미합니다.
0을 제외한 다른 숫자들은 lottos에 2개 이상 담겨있지 않습니다.
lottos의 원소들은 정렬되어 있지 않을 수도 있습니다.
win_nums은 길이 6인 정수 배열입니다.
win_nums의 모든 원소는 1 이상 45 이하인 정수입니다.
win_nums에는 같은 숫자가 2개 이상 담겨있지 않습니다.
win_nums의 원소들은 정렬되어 있지 않을 수도 있습니다.
입출력 예
lottos	win_nums	result
[44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
[0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
[45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]
입출력 예 설명
입출력 예 #1
문제 예시와 같습니다.

입출력 예 #2
알아볼 수 없는 번호들이 아래와 같았다면, 1등과 6등에 당첨될 수 있습니다.

당첨 번호	38	19	20	40	15	25	결과
최고 순위 번호	0→38	0→19	0→20	0→40	0→15	0→25	6개 번호 일치, 1등
최저 순위 번호	0→21	0→22	0→23	0→24	0→26	0→27	0개 번호 일치, 6등
입출력 예 #3
민우가 구매한 로또의 번호와 당첨 번호가 모두 일치하므로, 최고 순위와 최저 순위는 모두 1등입니다.

실제로 사용되는 로또 순위의 결정 방식과는 약간 다르지만, 이 문제에서는 지문에 명시된 대로 로또 순위를 결정하도록 합니다.

"""



# 내가 제출한 정답
def lotto_check(lottos, win_nums):
    answer = []
    count = 0
    zero = 0

    for lotto in lottos:
        if lotto in win_nums:
            count += 1
    if 0 in lottos:
        zero = lottos.count(0)

    print('zero', zero)
    print(count)
    if count + zero == 6:
        win_count = 1
    elif count + zero == 5:
        win_count = 2
    elif count + zero == 4:
        win_count = 3
    elif count + zero == 3:
        win_count = 4
    elif count + zero == 2:
        win_count = 5
    else:
        win_count = 6

    if count == 6:
        realcount = 1
    elif count == 5:
        realcount = 2
    elif count == 4:
        realcount = 3
    elif count == 3:
        realcount = 4
    elif count == 2:
        realcount = 5
    else:
        realcount = 6

    answer = [win_count,realcount]
    return answer

if __name__ =='__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    result = [3, 5]

    # lottos = [0, 0, 0, 0, 0, 0]
    # win_nums = [38, 19, 20, 40, 15, 25]
    # result = [1, 6]

    # lottos = [45, 4, 35, 20, 3, 9]
    # win_nums = [20, 9, 3, 45, 4, 35]
    # result = [1, 1]

    print(lotto_check(lottos,win_nums))


# 강사님 답
def solution(lottos, win_nums):
    answer = []

    # lottos : 민우가 선택한 번호들
    # win_nums : 당첨번호

    # 내가 생각한 알고리즘 ???
    # 로또 번호를 하나 하나씩 당첨 번호와 비교한다.
    # 비교할 때 , 로또 번호가 0이면, 별도로 처리한다.
    # 몇개 맞췄는지 알고 있어야 한다.(변수로 저장한다.)
    win_count = 0
    # 로또번호가 지워진 경우도 몇 개인지 알고 있어야 한다.(변수로 저장한다.)
    sub_count = 0

    for lotto in lottos:
        if lotto == 0:
            sub_count += 1
        else:
            if lotto in win_nums:
                win_count += 1
            # for win_num in win_nums:
            #     if lotto == win_num:
            #         win_count += 1
            #        lotto in win_nums

    # 맞춘 갯수와 지워진 갯수를 가지고 최대,최소 몇 개 맞출 수 있는지 확인한다.
    best_count = win_count + sub_count
    worst_count = win_count
    # 최대 맞춘 갯수와, 최소로 맞춘 갯수로 순위를 확인한다.
    best_rank = min(7 - best_count, 6)
    #     if best_count == 6:
    #         best_rank = 1
    #     elif best_count == 5:
    #         best_rank = 2
    #     elif best_count == 4:
    #         best_rank = 3
    #     elif best_count == 3:
    #         best_rank = 4
    #     elif best_count == 2:
    #         best_rank = 5
    #     else:
    #         best_rank = 6
    worst_rank = min(7 - worst_count, 6)
    #     if worst_count == 6:
    #         worst_rank = 1
    #     elif worst_count == 5:
    #         worst_rank = 2
    #     elif worst_count == 4:
    #         worst_rank = 3
    #     elif worst_count == 3:
    #         worst_rank = 4
    #     elif worst_count == 2:
    #         worst_rank = 5
    #     else:
    #         worst_rank = 6

    # answer = [최고 순위, 최저 순위]
    answer = [best_rank, worst_rank]
    return answer
'''
다른 풀이
case#1
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
case#2
def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]] # 리스트 간의 교집합!
'''

'''
주의할 점 :
1. 문제의 길이로 너무 겁먹지 말자.
2. 과정을 한번에 진행하려고 하지 말고 차근차근 한 단계씩 진행한다면 더욱 쉽게 풀릴 것 같다.
3. 강사님 방법처럼 최대한 간결하게 진행 할 수 있는 방법을 생각 해보는 것도 좋을 것 같다.
4. case#1이 내가 처음에 하고 싶었던 방법 이었다. 근데 , dict로만 할 생각을 해서 key값을 숫자가 아닌 다른 값으로 어떻게 줄지 고민만 했다.
5. 4번을 적고, case#2를 봤는데..이게 더 내 생각과 비슷한 듯..
6. dict로 key값 숫자주는 것 되는데, 왜 내가 풀 때는 에러 났엇는지...
'''