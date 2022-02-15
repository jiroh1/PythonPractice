# https://info-lab.tistory.com/303
# case1
animal = 'dog'
cat = 'cat'
dog = 'dog'
ret = None

# 1. if 문 #
if animal is dog:
    ret = dog
print("Default: " + ret)

if animal is dog: ret = dog
print("One-Line: " + ret)


# [output]
# Default: dog
# One-Line: dog


# case2
cat = 'cat'
dog = 'dog'
ret = None

# 2. if - eles 문 #
animal = 'cat'
if animal is dog:
    ret = dog
else:
    ret = cat
print("Default: " + ret)

ret = dog if animal is dog else cat
print("One-Line: " + ret)

# animal 변수값 변경 #
animal = 'dog'
if animal is dog:
    ret = dog
else:
    ret = cat
print("Default: " + ret)

ret = dog if animal is dog else cat
print("One-Line: " + ret)

# [output]
# Default: cat
# One-Line: cat
# Default: dog
# One-Line: dog


#case 3
cat = 'cat'
dog = 'dog'
cow = 'cow'
ret = None

# 3. if - elif - eles 문 #
animal = 'cow'
if animal is dog:
    ret = dog
elif animal is cat:
    ret = cat
else:
    ret = cow
print("Default: " + ret)

ret = dog if animal is dog else cat if animal is cat else cow
print("One-Line: " + ret)

# animal 변수값 변경 #
animal = 'cat'
if animal is dog:
    ret = dog
elif animal is cat:
    ret = cat
else:
    ret = cow
print("Default: " + ret)

ret = dog if animal is dog else cat if animal is cat else cow
print("One-Line: " + ret)

# animal 변수값 변경 #
animal = 'dog'
if animal is dog:
    ret = dog
elif animal is cat:
    ret = cat
else:
    ret = cow
print("Default: " + ret)

ret = dog if animal is dog else cat if animal is cat else cow
print("One-Line: " + ret)

# [output]
# Default: cow
# One-Line: cow
# Default: cat
# One-Line: cat
# Default: dog
# One-Line: dog
