# 시뮬레이션과 창의적 해결법

answer = list(map(int, input()))
user_input = list(map(int, input()))

# fail 해서 우선 answer에 있는 숫자로 변경하는 함수
def fail():
    print('fail')
    for i in range(4):
        # 상태가 fail인 자리만 작업을 수행
        if result[i] != 2:
            continue
        while True:
            # 문제에서 요구한 것을 구현 1 증가 , 10 나누기
            # 값을 바로 대입하지 않고, 현재 입력의 다른 자리에 해당 값이 존재하는지를 먼저 판단
            temp = (user_input[i] + 1) % 10
            out = temp not in user_input
            user_input[i] = temp
            if out:
                print('@',user_input)
                break

def ball():
    print('ball')
    # ball 인 경우가 없으면 return
    if 1 not in result:
        return
    pos = []
    value = []
    for i in range(4):
        if result[i] != 0:
            pos.append(i)
            value.append(user_input[i])
    print('####',pos, value)
    for i in range(len(pos)):
        # pos[i] 위치에 들어오는 값은 pos[i-1] 위치에 있던 값이기 때문에 i가 0인 것에 대해서는 마지막순서로 보내기
        if i == 0:
            user_input[pos[i]] = value[-1]
        else:
            user_input[pos[i]] = value[i - 1]

# strike : 0 , ball : 1, fail :2
make_input_count = 0
while True: 
    make_input_count += 1
    result = [2, 2, 2, 2]
    # user_input 과 answer이 같은 경우는 게임이 종료되는 조건
    if user_input == answer:
        print(make_input_count)
        break
    # 입력의 첫째 자리부터 순서대로 보면서 상태 확인
    for i in range(4):
        # 현재 값이 answer에 없는 경우는 fail에 해당
        # 앞서 상태의 기본값을 fail로 설정했기 때문
        if user_input[i] in answer:
            # strike 인 경우
            if user_input[i] == answer[i]:
                result[i] = 0
            # ball인 경우
            else:
                result[i] = 1
            
    fail()
    ball()

print(answer,user_input)

"""
정리 

1. 첫 틀을 잘 잡아야함. strike기준으로 fail, ball은 함수화 시키기
2. fail 에서는 지속적으로 그 안에 있는 값을 만들기 (ball 로 만들기)
3. ball에서는 0(strike)이 아닌 pos를 변경하면서 맞추는 것이 관건
"""