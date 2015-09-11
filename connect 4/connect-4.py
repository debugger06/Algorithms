# TASK 1.3 - CONNECT 4 #
########################
# Arash Nasirtafreshi  #
# Mana Azamat          #
# Mohammad Saifullah   # 
# Mudra Shah           #
# Tanya Agarwal        #
# Urmimala Majumdar    #
# Hasan Mahmud	       #
########################

import numpy as np
import matplotlib.pyplot as plt
import pylab
from numpy.core.numeric import dtype
from numpy.ma.core import flatten_structured_array

# function to draw histogram
def draw_histogram(freq):
    alphab = np.arange (0,42)
    frequencies = freq
    pos = np.arange(len(alphab))
    width = 1.0     # gives histogram aspect to the bar diagram

    ax = plt.axes()
    ax.set_xticks(pos + (width/2))
    ax.set_xticklabels(alphab)
    plt.tick_params(axis='both', which='major', labelsize=7)
    plt.title('Connect-4')
    plt.xlabel('Fields')
    plt.ylabel('Probabilities')
    plt.bar(pos, frequencies, width, color='r',align='center') 
    plt.savefig("histogram-connect-4")

# logic of move_still_possible remains the same in connect 4 as in tic-tac-toe game
def move_still_possible(S):
    return not (S[S==0].size == 0)

# returns matrix of probability for each field that contributes to win
def create_probability_matrix(resultMatrix):
    z = np.empty((6,7),float)
    z[:] = np.sum(resultMatrix)
    d = np.divide(resultMatrix , z)
    return d.flatten()

# we choose the column in which the coin is dropped, however the row is decided by the function
def move_at_random(S, p):
    xs, ys = np.where(S==0) #checking for empty places 

    i = np.random.permutation(np.arange(ys.size))[0] #choosing a empty column at random
    
    S[row_index_at_column(S,ys[i]),ys[i]] = p #setting the value for the row available for column chosen for player p

    return S

# function that returns the appropriate row index for the column chosen at random
def row_index_at_column(S,k):
    i = S.shape[0] - 1
    while(i > -1):
         if(S[i][k] == 0):
           return i
         i -= 1
    return -1 # confusion -- is it required?

# function to extract 4x4 matrices and move across the board to check for winning condition
def check_for_win(S,p, resultMatrix):
    xN = S.shape[0]
    yN = 0
    # loop used with set extent of the sliding window 
    for i in range(xN,xN-3,-1): 
        for j in range(yN, yN+4):
	   hasWon,winAt,value = move_was_winning_move(S[i-4:i,j:j+4],p)
	   if hasWon :
                #Check if the player won when he got 4 in a column
		if winAt =='column':
			row = i
			column = value + j #column index changed to deal with result from small 4x4 matrices
			#row here signifies the last row auspicious index in the matrix
			for i in range(row-1,row-5,-1):
				resultMatrix[i][column] += 1
		#Check if the player won when he got 4 in a row
		elif winAt =='row':	
			row = value + i - 4 #row index changed to deal with result from small 4x4 matrices
			column =  j
			#column here signifies the first auspicous column index in the matrix		
			for i in range(column,column+4):
				resultMatrix[row][i] += 1 
		#Check if the player won when he got 4 in a diagonal
		elif winAt  =='nDiag':
			row = i-4
			column = j
			#row and column signify the first indices of the diagonal in the matrix
			for i in range(0,4):
				resultMatrix[row+i][column+i] += 1
		#Check if the player won when he got 4 in an anti-diagonal
		elif winAt  =='rDiag':
			row = i-1
			column = j
			#row and column signify the first indices of the anti-diagonal in the matrix
			for i in range(0,4):
				resultMatrix[row-i][column+i] += 1
		return True

    return False

# function that accepts a part of the game state and checks for winner
def move_was_winning_move(S, p):
    if np.max((np.sum(S, axis=0)) * p) == 4:
	value = np.argmax((np.sum(S, axis=0)) * p)
        return True,'column',value

    if np.max((np.sum(S, axis=1)) * p) == 4:
	value = np.argmax((np.sum(S, axis=1)) * p)
        return True,'row', value

    if (np.sum(np.diag(S)) * p) == 4:
        return True,'nDiag',0

    if (np.sum(np.diag(np.rot90(S))) * p) == 4:
        return True,'rDiag',0

    return False,'',-1


# relate numbers (1, -1, 0) to symbols ('R', 'Y', ' ') 
# R corresponds to Red & Y corresponds to Yellow
symbols = {1:'R', -1:'Y', 0:' '}

# print game state matrix using symbols
def print_game_state(S):
    B = np.copy(S).astype(object)
    for n in [-1, 0, 1]:
        B[B==n] = symbols[n]
    print B



if __name__ == '__main__':
    print 'Playing and calculating tournament results...'
    # initializing resultMatrix to collect statistics for a tournament of 1000 games
    resultMatrix = np.zeros((6,7), dtype=int)

    # initializing counters 
    winR =0 
    winY=0
    gameCounter = 0
    drawCounter = 0

    
    while (gameCounter < 1000):
	gameCounter += 1
	# initialize 6x7 connect 4 board
    	gameState = np.zeros((6,7), dtype=int)

    	# initialize player number, move counter
    	player = 1
    	mvcntr = 1

    	# initialize flag that indicates win
    	noWinnerYet = True

    	while move_still_possible(gameState) and noWinnerYet:
		# get player symbol
		name = symbols[player]
		#print '%s moves ' % name

		# let player move at random
		gameState = move_at_random(gameState, player)

		# print current game state
		# print_game_state(gameState)

		# evaluate game state
		if check_for_win(gameState, player, resultMatrix):
		    #print 'player %s wins after %d moves' % (name, mvcntr)
		    noWinnerYet = False
		    if (name == 'R'):
                    	winR += 1
	            else:
        	        winY += 1

		# switch player and increase move counter
		player *= -1
		mvcntr +=  1
	

	if noWinnerYet:
        	#print 'game ended in a draw'
		drawCounter += 1 
	
    #print_game_state(gameState)
    probabilityMatrix = create_probability_matrix(resultMatrix)
    print 'winR: ', winR
    print 'winY: ', winY
    print 'drawCounter: ', drawCounter
    print '\n'
    print resultMatrix
    print '\n'
    print probabilityMatrix
    frequency = np.ravel(np.array(probabilityMatrix))
    draw_histogram(frequency)
