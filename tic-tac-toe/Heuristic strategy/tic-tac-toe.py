# TASK 1.2.1 -           #
# PROBABILISTIC STRATEGY #
##########################
# Arash Nasirtafreshi    #
# Mana Azamat            #
# Mohammad Saifullah     #
# Mudra Shah             #
# Tanya Agarwal          #
# Urmimala Majumdar      #
# Hasan Mahmud	         #
##########################

import numpy as np
import matplotlib.pyplot as plt
import pylab
from numpy.core.numeric import dtype
from numpy.ma.core import flatten_structured_array


def Draw_histogram(freq):
    alphab = ['0,0', '0,1', '0,2', '1,0', '1,1', '1,2' , '2,0' , '2,1' , '2,2']
    frequencies = freq
    pos = np.arange(len(alphab))
    width = 1.0     # gives histogram aspect to the bar diagram
    
    ax = plt.axes()
    ax.set_xticks(pos + (width / 2))
    ax.set_xticklabels(alphab)
    plt.title('Tic-Tac-Toe Win')
    plt.xlabel('Fields')
    plt.ylabel('Probabilities')
    plt.bar(pos, frequencies, width, color='r')
    plt.savefig("histogram-Random")


# returns Matrix of probability for each field that contributes to win
def Create_probability_matrix(res):
    z = np.empty((3,3),float)
    z[:] = np.sum(resultmatrix)
    d = np.divide(resultmatrix , z)
    return d.flatten()


# The function to add two matrices (pair-wise)

def add_two_matrices(res, a):
    # iterate through rows
    for i in range(len(res)):
            # iterate through columns
            for j in range(len(res[0])):
                res[i][j] = res[i][j] + a[i][j]
    return res


def print_Matrix(res):
    print 'res now is:  '
    print res


def move_still_possible(S):
    return not (S[S==0].size == 0)


def move_at_random(S, p):
    xs, ys = np.where(S==0)

    i = np.random.permutation(np.arange(xs.size))[0]
    
    S[xs[i],ys[i]] = p

    return S


def move_was_winning_move(S, p , res):
    # check the columns
    if np.max((np.sum(S, axis=0)) * p) == 3:
        
        # Get the index of the Column
        col = np.argmax(np.sum(S, axis=0)*p)
        # increment the fields in resultmatrix  
        res[:, col] += 1
        return True

    # check the rows
    if np.max((np.sum(S, axis=1)) * p) == 3:
        
        # Get the index of the Row
        row = np.argmax(np.sum(S, axis=1)*p)
        # increment the fields in resultmatrix 
        res[row, :] += 1
        return True

    if (np.sum(np.diag(S)) * p) == 3:
        
        #print np.diag(res)+1
        # Create a matrix with diagonal 1 (identity matrix)
        # Good to know:
        #a= [1,1,1]
        #res = np.add(res , np.diag(a))
       
        a = np.identity(3)
        res = add_two_matrices(res, a)
        return True

    if (np.sum(np.diag(np.rot90(S))) * p) == 3:
        # Add 90 rotated Identity matrix to resultmatrix
        
        a = np.identity(3)
        a = np.rot90(a)
        res = add_two_matrices(res, a)
        return True

    return False



# relate numbers (1, -1, 0) to symbols ('x', 'o', ' ')
symbols = {1:'x', -1:'o', 0:' '}

# print game state matrix using symbols
def print_game_state(S):
    B = np.copy(S).astype(object)
    for n in [-1, 0, 1]:
        B[B==n] = symbols[n]
    print B





if __name__ == '__main__':
    # initialize 3x3 tic tac toe board
    
    fo = open('RandomGames.txt','wb')   
    
    winFor_X =0 
    winFor_Y=0
    
    gameCounter = 0
    drawCounter = 0
    resultmatrix = np.zeros((3,3), dtype=int)
    while (gameCounter<1000):
        gameCounter +=1
        
        #print '**************************** Starting the Game:', gameCounter
        gameState = np.zeros((3,3), dtype=int)
    
        # initialize player number, move counter
        player = 1
        mvcntr = 1
    
        # initialize flag that indicates win
        noWinnerYet = True
        
    
        while move_still_possible(gameState) and noWinnerYet:
            # get player symbol
            name = symbols[player]
            #print '%s moves' % name
    
            # let player move at random
            gameState = move_at_random(gameState, player)
    
            # print current game state
            #print_game_state(gameState)
            
            # evaluate game state
            if move_was_winning_move(gameState, player , resultmatrix):
                #print 'player %s wins after %d moves' % (name, mvcntr)
                if (name == 'x'):
                    winFor_X += 1
                else:
                    winFor_Y += 1
                noWinnerYet = False
    
            # switch player and increase move counter
            player *= -1
            mvcntr +=  1
    
    
    
        if noWinnerYet:
            drawCounter+=1
            #print 'game ended in a draw' 

    # piechart for wins and draws
    ax = pylab.axes([0.1, 0.1, 0.6, 0.6])
    labels = 'x-wins', 'o-wins', 'draws'  
    fracs = [winFor_X,winFor_Y,drawCounter]

    explode=(0.07,0.05,0.025)
    ax.pie(fracs, labels=labels, explode = explode,         
                             autopct='%1.1f%%', shadow =True)
    pylab.savefig("pieChart-Random")
            
    # Show the result
    print '*************************************** Final Result ****************************************'
    print resultmatrix
    
    # sort by index
    h = np.argsort(resultmatrix.flatten())
    # reverse the sort
    fo.write(str(h[::-1]))
    
    #Write probability Matrix
    pm = Create_probability_matrix(resultmatrix)
    fo.write('\n')
    fo.write(str(pm))
    
    #print draws
    print '\nDraws:',drawCounter
    fo.write('\ndraws: \n')
    fo.write(str(drawCounter))
    
    #print X won
    print 'X won: ',winFor_X
    fo.write('\nX won: \n')
    fo.write(str(winFor_X))
    
    #print Y won
    print 'Y won: ',winFor_Y
    fo.write('\nY won: \n')
    fo.write(str(winFor_Y))
    
    #print Number of Games
    fo.write('\nNumber of Games \n')
    fo.write(str(gameCounter))
    
    #close file
    fo.close()
  
    print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Now reading file and drawing Histogram <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
    fi = open('RandomGames.txt','rb')
    #Read lines from 1 to 3 because these lines contain what we need
    fi.readline()
    L1 = fi.readline()
    L2 = fi.readline()
    L3 = ''
    if (L2.find(']')==-1):
        L3 = fi.readline()
    c = L1 + L2 + L3
    #Cleaning the c
    c = c.replace('\n','')
    c = c.replace('[ ','')
    c = c.replace('[','')
    c = c.replace(' ]','')
    c = c.replace(']','')
    while (c.find('  ')!=-1):
        c = c.replace('  ',' ')
        
    # creating the a list
    c = c.split(' ')
    
    # Converting strings to floats
    freq = np.asfarray(c, str)
    Draw_histogram(freq)
    print 'Histogram saved as png!' 

