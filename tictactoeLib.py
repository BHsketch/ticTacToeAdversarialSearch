# representing x's by 1's and o's by 0's

board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]


# returns the utility of an end state w.r.t. the player playing 'x' i.e. '1'
def utility(state):

	# checking for row-wise win if any
	for row in state:
		if (row[0] == row[1]) and (row[0] == row[2]) and (row[0] != -1):
			if (row[0] == 1):
				return 1 # WIN
			else:
				return -1 # LOSS
	
	# checking column-wise win if any
	for i in range(0, len(state)):
		if (state[0][i] == state[1][i]) and (state[0][i] == state[2][i]) and (state[0][i] != -1):
			if state[0][i] == 1:
				return 1 # WIN
			else:
				return -1 # LOSS

	# checking diagonals:
	if (((state[0][0] == state[1][1]) and (state[0][0] == state[2][2])) or ((state[2][0] == state[1][1]) and (state[2][0] == state[0][2]))) and (state[1][1] != -1):
		if state[1][1] == 1:
			return 1 # WIN
		else:
			return -1 # LOSS
	
	# if no three-in-a-row, check if all are filled
	unfilledFlag = 0
	for row in state:
		for elem in row:
			if elem == -1:
				unfilledFlag = 1

	if unfilledFlag == 0:
		return 0 # DRAW
	
	# if none of the above, this is not a terminal state
	return -2
	

# CHECK IF END HAS BEEN REACHED 
def terminalTest(state):
	utilityTest = utility(state)
	if utilityTest != -2:
		return True
	else:
		return False

# GETS THE SET OF ACTIONS POSSIBLE FOR THIS STATE
def actions(state):
	zeroCount = 0
	oneCount = 0
	nextPly = -1
	possibleMoves = [];
	for i in range(0, len(state)):
		for j in range(0, len(state)):
			if state[i][j] == 0:
				zeroCount+=1
			elif state[i][j] == 1:
				oneCount+=1
			else:
				possibleMoves.append([i, j])
	
	# assuming 1 always plays first (without loss of generality)
	if(zeroCount == oneCount):
		# one's turn
		nextPly = 1
	else:
		nextPly = 0

	for move in possibleMoves:
		move.append(nextPly)

	return possibleMoves
	
# GETS THE RESULT OF PERFORMING AN ACTION ON A STATE
def result(state, action):
	# action is a list of three things: i, j, player(1 or 0)

	state[action[0]][action[1]] = action[2]

	return state



				
	


