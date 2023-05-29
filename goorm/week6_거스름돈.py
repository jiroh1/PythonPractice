#  수정한 답안
changes = int(input())
answer = 0
coins=[40, 20, 10, 5, 1]
for coin in coins:
	answer += changes // coin
	changes %= coin
print(answer)

# 첫 제출 답안
coin = int(input())

changes = 0
while True :
	if coin >= 40:
		coin -= 40
		changes += 1
		continue
	elif coin > 20:
		coin -= 20
		changes += 1
		continue
	elif coin >= 10:
		coin -= 10
		changes += 1
		continue
	elif coin >= 5:
		coin -= 5
		changes += 1
		continue
	elif coin >= 1:
		coin -= 1
		changes += 1
		continue
	elif coin == 0:
		break
print(changes)

"""

"""