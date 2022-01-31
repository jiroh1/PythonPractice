'''
# 리스트에 값을 하나씩 더해서 새로운 리스트를 만드는 작업
myList = [1, 2, 3, 4, 5]
#myList = [(1,3),(2,4), (3, 4),(5,3)]
# for 반복문 이용 result1 = [] for val in myList: result1.append(val + 1) print(f'result1 : {result1}')
# map 함수 이용
def add_one(n):
    print(n+1)
    return n + 1 #return 받아서 하나씩 리스트로 넣어주고 있음. # 2, 3, 4, 5, 6
    print('@@') # return 하니깐 없어지는 공간
result2 = list(map(add_one, myList))
print('@@@')
# map반환을 list 로 변환
print(f'result2 : {result2}')
'''

# 위에 것에서 응용해본 문제근
# 리스트안에 리스트에 각각 function을 다르게 주어서 연산하기
# 1/28 python vector 연산 x ,https://blog.naver.com/kunyoung90/222072887939 참고해서 해결
myList = [[1, 2], [3, 4], [5, 6], [7, 8]]
# for 반복문 이용 result1 = [] for val in myList: result1.append(val + 1) print(f'result1 : {result1}')
# map 함수 이용
def plusone(n):
    return n + 1
def plustwo(n):
    return n + 2
answer = []
for j in myList:
    #    print(j) #[1,2]myList = [[1, 2], [3, 4], [5, 6], [7, 8]]
    # # for 반복문 이용 result1 = [] for val in myList: result1.append(val + 1) print(f'result1 : {result1}')
    # # map 함수 이용
    # def plusone(n):
    #     return n + 1
    # def plustwo(n):
    #     return n + 2
    # answer = []
    # for j in myList:
    #     #    print(j) #[1,2]
    #     for i in range(len(myList)):
    #         #        print(i) # 0, 1, 2, 3 , myList = 4
    # #        if myList[i][0]:
    # #            print(myList[i], '@@')
    # #            print(myList[i][0], '@')
    #         result = list(map(plusone, j))
    #         print(result, '@', i)
    #     answer.append(result)
    # #            print(result, 'result')
    # #        elif myList[i][1]:
    # #            result = list(map(plustwo, j))
    # #            print(result, 'result2')
    # #            rofr= list(map(int,result))
    # #print(f'r_of_r:{rofr}')
    # print(answer)
    # # goal!! : result = [[2,4],[4,6],[6,8],[8,10]]
    # # subgoal : result = [[2,3],[4,5],[6,7],[8,9]]
    for i in range(len(myList)):
        #        print(i) # 0, 1, 2, 3 , myList = 4
#        if myList[i][0]:
#            print(myList[i], '@@')
#            print(myList[i][0], '@')
        result = list(map(plusone, j))
        print(result, '@', i)
    answer.append(result)
#            print(result, 'result')
#        elif myList[i][1]:
#            result = list(map(plustwo, j))
#            print(result, 'result2')
#            rofr= list(map(int,result))
#print(f'r_of_r:{rofr}')
print(answer)
'''
# 해결 
def add_one(n):
    my_list = list()
    for i in range(len(n)):
        my_list.append(n[i] + (i+1))
    return my_list

res = list(map(add_one, myList))
print(res)

# goal!! : result = [[2,4],[4,6],[6,8],[8,10]]
# subgoal : result = [[2,3],[4,5],[6,7],[8,9]]
'''


# def add_one(n, k):
#    return n + 1, k +2
# result2 = list(map(add_one, myList))
# # map반환을 list 로 변환
# print(f'result2 : {result2}')


'''
## code1
# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
	return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
============================
##code 2
# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))
============================
##code 3
# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))
==============================
##code 4
# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

'''
