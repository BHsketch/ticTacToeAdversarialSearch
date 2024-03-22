from tictactoeLib import *

def minimaxDecision(stateIn):
	#print("in minimax decision")
	state = stateIn
	listOfMinValues = []
	bestVal = float('-inf')
	bestAction = []
	
	for a in actions(state):
		stateTemp = []
		for i in range(0, len(state)):
			stateTemp.append([])
			for j in range(0, len(state)):
				stateTemp[i].append(state[i][j])

		val = minValue(result(stateTemp, a))
		
		if val > bestVal:
			bestVal = val
			bestAction = a
	
	#for row in state:
	#		print("\n")
	#		for elem in row:
	#			print(elem, "\t", end='')

	return bestAction
	

def maxValue(stateIn):
	#print("in maxvalue")
	state = stateIn
	if terminalTest(state):
		return utility(state)
	
	v = float('-inf')
	
	possibleActions = actions(state)

	for a in possibleActions:
		
		stateTemp = []
		for i in range(0, len(state)):
			stateTemp.append([])
			for j in range(0, len(state)):
				stateTemp[i].append(state[i][j])

		v = max(v, minValue(result(stateTemp, a)))

	
	#for row in state:
	#		print("\n")
	#		for elem in row:
	#			print(elem, "\t", end='')

	return v


def minValue(stateIn):
	#print("in minvalue")
	state = stateIn
	if terminalTest(state):
		return utility(state)
		
	v = float('+inf')
	
	possibleActions = actions(state)
	for a in possibleActions:
		
		stateTemp = []
		for i in range(0, len(state)):
			stateTemp.append([])
			for j in range(0, len(state)):
				stateTemp[i].append(state[i][j])

		v = min(v, maxValue(result(stateTemp, a)))


	#for row in state:
	#		print("\n")
	#		for elem in row:
	#			print(elem, "\t", end='')

	return v

def gameBegins():
	print("Welcome fellow earthling. My name is Snot, the AI bot. Wanna play tic tac toe with me?\n")
	
	gameBoard = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

	while(utility(gameBoard) == -2):
		# AI Makes it's move
		copyBoard = [ i for i in gameBoard ]
		#curAction = minimaxDecision(copyBoard)
		#result(gameBoard, curAction)
		gameBoard = result(gameBoard, minimaxDecision(copyBoard))

		for row in gameBoard:
			print("\n")
			for elem in row:
				print(elem, "\t", end='')

		if(utility(gameBoard) != -2):
			#print("hello")
			break

		# Now the Human's turn
		inputCoordinates = input("enter row and column here: ")
		# Splitting the input string by space
		inputCoordinates = inputCoordinates.split()

		# Converting each element to integer using list comprehension
		numbers = [int(num) for num in inputCoordinates]
		
		gameBoard[numbers[0]][numbers[1]] = 0

		
	if utility(gameBoard) == 1:
		print("Game Over: Looks like I won!")
	elif utility(gameBoard) == -1:
		print("Congratulations, You won!")
	else:
		print("Good game, partner. Looks like a draw")


gameBegins()

	
