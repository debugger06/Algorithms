# TASK 2.3 - Min Max for CONNECT 4 #
########################
# Arash Nasirtafreshi  #
# Hasan Mahmud         #
# Mana Azamat          #
# Mohammad Saifullah   # 
# Mudra Shah           #
# Tanya Agarwal        #
# Urmimala Majumdar    #
########################
import numpy as np
from connect4 import *


def get_next_move(S,p,mvcntr,depth):
    player = p 
    
    # assign evaluated values to the allowed moves of the gameState
    movesAllowed = {}
    rows, cols = np.where(S==0) # allowed values for column stored in ys
    ys = list(set(cols)) # unique values 
    for j in xrange(len(ys)):
	temp = np.copy(S)
        temp[row_index_at_column(S,ys[j]),ys[j]] = p
	
	# change player for minmax calculations
	player *= -1 
        movesAllowed[j] = -treeSearch(depth, temp, player)
    #print "Moves Allowed: ",movesAllowed, "\n\n"
    
    bestNodeValue = -99999999
    nextMove = None
    
    moves = movesAllowed.items()
    for move, value in moves:
            if value >= bestNodeValue:
                bestNodeValue = value
                nextMove = move

    # Set the gameState
    S[row_index_at_column(S,nextMove),nextMove] = p
    return S

def treeSearch(depth, S, p):
        
    # declaring for all successors from this state
    successor = []
    rows, cols = np.where(S==0) # allowed values for column stored in ys
    ys = list(set(cols)) # unique values 
    for j in xrange(len(ys)):
	temp = np.copy(S)
	temp[row_index_at_column(temp,ys[j]),ys[j]] = p
        successor.append(temp)
        
    if depth == 0 or len(successor) == 0 or not move_still_possible(S):
        # return the evaluated value for the node
        return evalConnectFour(S,p)
    player = p * -1 
        
    value = -np.inf
    for child in successor:
        if child == None:
            print("child == None (search)")
        value = max(value, -treeSearch(depth-1, child, player))
    return value

def evalConnectFour(S,p):
    four = checkForFeature(S, p, 4)
    if four > 0 :
       return 100000	

    three = checkForFeature(S, p, 3) * 1000
    two = checkForFeature(S, p, 2) * 10

    opponentFour = checkForFeature(S, p*-1, 4) 
    opponentThree = checkForFeature(S, p*-1, 3) * 1000
    opponentTwo = checkForFeature(S, p*-1, 2) * 10
   
    if opponentFour > 0 :
       return -100000
    else:
       return three + two - opponentThree - opponentTwo

def checkForFeature(S, p, F): 
    # check for every position in the gameState for requested feature.
    count = 0
    for i in xrange(6):
       for j in xrange(7):
          if S[i][j] == p:
             count += verticalF(i, j, S, F)
             count += horizontalF(i, j, S, F)
             count += diagonalCheck(i, j, S, F)
    return count
            
def verticalF(  row, col, S, F):
    b2bCount = 0 # back to back count
    for i in xrange(row, 6):
       if S[i][col]  == S[row][col]:
          b2bCount += 1
       else:
          break

    if b2bCount >= F:
       return 1
    else:
       return 0

def horizontalF(  row, col, S, F):
    b2bCount = 0
    for j in xrange(col, 7):
       if S[row][j]  == S[row][col] :
          b2bCount += 1
       else:
          break

    if b2bCount >= F:
       return 1
    else:
       return 0

def diagonalCheck(  row, col, S, F):
    total = 0
    # checking on diagonal of gameState
    b2bCount = 0
    j = col
    for i in xrange(row, 6):
       if j > 6:
          break
       elif S[i][j]  == S[row][col] :
          b2bCount += 1
       else:
          break
       j += 1 
    
    if b2bCount >= F:
       total += 1

    # check on anti-diagonal of gameState
    b2bCount = 0
    j = col
    for i in xrange(row, -1, -1):
       if j > 6:
          break
       elif S[i][j] == S[row][col] :
          b2bCount += 1
       else:
          break
       j += 1 

    if b2bCount >= F:
       total += 1

    return total


if __name__ == '__main__':
    print '#############'
    print '# Connect 4 #'	
    print '#############\n'
    playCount = 100
    depthRestriction = 2
    print 'Playing and calculating tournament results...'
    # initializing resultMatrix to collect statistics for a tournament of 1000 games
    resultMatrix = np.zeros((6,7), dtype=int)

    # initializing counters 
    winR =0 
    winY=0
    gameCounter = 0
    drawCounter = 0
    
    while (gameCounter < playCount):
        gameCounter += 1

        # initialize 6x7 connect 4 board
        gameState = np.zeros((6,7), dtype=int)
        
        # initialize player number, move counter
        player = 1
        mvcntr = 1

	# initialize flag that indicates win
	noWinnerYet = True
	depth = depthRestriction

        while move_still_possible(gameState) and noWinnerYet:
            # get player symbol
            name = symbols[player]
            #print '%s moves ' % name
	    
	    # Heuristic player
	    if player == 1:
	        gameState = get_next_move(gameState,player,mvcntr,depth)
		
	    else:# Random player
		gameState = move_at_random(gameState,player)

            # print current game state
            #print_game_state(gameState)

            # evaluate game state
            if check_for_win(gameState, player):
                print 'Game #',gameCounter,' Player %s wins after %d moves' % (name, mvcntr)
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
            
    print 'winR: ', winR
    print 'winY: ', winY
    print 'drawCounter: ', drawCounter
    print '\n'
