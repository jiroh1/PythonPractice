myList = [[1, 2], [3, 4], [5, 6], [7, 8]]

def add_one(n):
    my_list = list()
    for i in range(len(n)):
        my_list.append(n[i] + (i+1))
    return my_list

res = list(map(add_one, myList))
print(res)

'''

# goal!! : result = [[2,4],[4,6],[6,8],[8,10]]
# subgoal : result = [[2,3],[4,5],[6,7],[8,9]]
'''