"""
예제 : 기본 정렬 구현하기
- 선택 정렬 : 0번째 인덱스부터 현재 위치에 들어갈 값을 찾는 알고리즘
- 삽입 정렬 : 1번째 인덱스부터 현재 위치의 수와 앞의 배열을 확인하여 들어갈 위치를 찾는 알고리즘
- 버블 정렬 : 0번째 인덱스부터 2개씩 비교하여 맨 끝을 정렬해가는 알고리즘

"""

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        print('min_idx_i : ', min_idx)
        # 선택한 인덱스 다음부터 하기 위해서 i+1
        for j in range(i + 1, len(arr)):
            print('R',range(i+1,len(arr)))
            print("j : ", j)
            print('arr[min_idx]',arr[min_idx])
            print('--------' * 20)
            # 각각 남은 인덱스의 값들을 arr[min_idx]로 지정해준다.
            if arr[j] < arr[min_idx]:
                print('*****enter!')
                min_idx = j
                print('min_idx_j : ', min_idx)
                print('@@@@',arr[min_idx], arr[j])
                print('@@@@@@@' *20)
        # 여기에서 변경 된 것을 자리 바꿔주는 것
        # 이전까지 비교는 계속 이루어지지 만 swap은 여기에서만 이루어짐
        print('======'*20)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print('####',arr[i], arr[min_idx])
        print('--------' * 20)
    return arr

c_list=[8,3,2,1,9,5,4]
print(selection_sort(c_list))


def insert(i_list):
    answer = [i_list[0]]
    while True:
        for i in range(len(i_list[1:])):
            # print('i_list',i_list)
            # print('answer',answer)
            if i_list[i] > answer[-1]:
                answer.append(i_list[i])
                i_list.pop(i)


c_list=[8,3,2,1,9,5,4]
# print('insert :',insert(c_list))

def bubble(list,number):

    pass


c_list=[8,3,2,1,9,5,4]
n = 3 # 현재위치
# print(bubble(c_list,n))


