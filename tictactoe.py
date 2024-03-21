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

		

