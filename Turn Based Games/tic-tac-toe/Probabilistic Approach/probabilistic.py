# TASK 1.2.1 -           #
# PROBABILISTIC STRATEGY #
##########################
# Arash Nasirtafreshi    #
# Mana Azamat            #
# Mohammad Saifullah     #
# Mudra Shah             #
# Tanya Agarwal          #
# Urmimala Majumdar      #
# Hasan Mahmud           #
##########################

import numpy as np
import matplotlib.pyplot as plt
import pylab

def Draw_histogram(freq):
    alphab = ['0,0', '0,1', '0,2', '1,0', '1,1', '1,2' , '2,0' , '2,1' , '2,2']
    #frequencies = [23, 44, 12, 11, 2, 10, 1, 2, 3 ]
    print freq
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
    plt.savefig("histogram-Probabilistic")


# returns Matrix of probability for each field that contributes to win
def Create_probability_matrix(res):
    z = np.empty((3,3),float)
    z[:] = np.sum(resultmatrix)
    d = np.divide(resultmatrix , z)
    return d.flatten()

# Function to remove used priorities from priority list
def delete_from_priority(v):
    v = np.delete(v, [0])
    return v

def move_x(S, p, priority):
    while (S[priority[0][0],priority[0][1]]!=0):
        priority = np.delete(priority, [0,1])
        priority = priority.reshape((priority.size/2 , 2))
        
    S[priority[0][0],priority[0][1]] = p
    return S

def move_x1(S, p):
    # Global because we want to use the updated priority list each time
    global priority
    while (S.flatten()[int(priority[0])]!=0):
        # The field is full so  move to the next priority and remove the the current one
        priority = delete_from_priority(priority)
        
    # Changing the value of S
    temp = S.flatten()
    temp[int(priority[0])] = p
    # The priority used so move the to next priority and remove the the current one
    priority = delete_from_priority(priority)
    # reshape the temp to have 3x3 matrix just like S
    S = temp.reshape((3,3))
    return S
    

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
        col = np.argmax(np.sum(S, axis=0)* p)
        # increment the fields in resultmatrix  
        res[:,col]+=1
        return True

    # check the rows
    if np.max((np.sum(S, axis=1)) * p) == 3:
        
        # Get the index of the Row
        row = np.argmax(np.sum(S, axis=1)* p)
        # increment the fields in resultmatrix 
        res[row,:]+=1
        return True

    if (np.sum(np.diag(S)) * p) == 3:
        
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
    
    '''
    sys.stdout = open('log.txt', 'w')
    print 'Write this to file.'
    '''
    fi = open('RandomGames.txt','r')
    fo = open('ProbabilisticGames.txt','wb')
    temp = fi.readline()
    #clean the line for converting it to array
    temp = temp.replace('\n','')
    temp = temp.replace('[','')
    temp = temp.replace(']','')
    
    
    winFor_X =0 
    winFor_Y=0
    gameCounter = 0
    drawCounter = 0
    #The Matrix that shows the contribution of each field in winning scenario
    resultmatrix = np.zeros((3,3), dtype=int)
    while (gameCounter<1000):
        gameCounter +=1
        #print '**************************** Starting the Game:', gameCounter
        gameState = np.zeros((3,3), dtype=int)
        #priority = np.array([[1,1], [2,2], [0,0], [0,2], [2,0], [0,1], [1,2], [2,1], [1,0]])
        global priority
        #Reset the Global Priority list for the new game
        priority = temp.split(' ')
        # initialize player number, move counter
        player = 1
        mvcntr = 1
    
        # initialize flag that indicates win
        noWinnerYet = True
        
    
        while move_still_possible(gameState) and noWinnerYet:
            # get player symbol
            name = symbols[player]
            #print '%s moves' % name
            
            #condition for selecting an appropriate function
            if (name =='x'):
                gameState = move_x1(gameState, player)
                
            else:
                # let player move at random
                gameState = move_at_random(gameState, player)
    
            # print current game state
            #print_game_state(gameState)
            
            # evaluate game state
            if move_was_winning_move(gameState, player, resultmatrix):
                #print 'player %s wins after %d moves' % (name, mvcntr)
                if (name == 'x'):
                    winFor_X += 1
                else:
                    winFor_Y += 1
                noWinnerYet = False
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
    pylab.savefig("pieChart-Probabilistic")   

         
    # Show the result
    print '*************************************** Final Result ****************************************'
    print 'Result matrix is:'
    print resultmatrix
    
    #Write probability Matrix
    pm = Create_probability_matrix(resultmatrix)
    fo.write('\n')
    fo.write(str(pm))
    
    #print draws
    print 'Draws:',drawCounter
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
    #Close file
    fo.close()
   

    print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Now reading file and drawing Histogram <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
    fi = open('ProbabilisticGames.txt','rb')
    #Read lines from 1 to 3 because these lines contain what we need
    L1 = fi.readline()
    L2 = fi.readline()
    L3 = ''
    if (L2.find(']')==-1):
        L3 = fi.readline()
    c = L1 + L2 + L3
    c = c.replace('\n','')
    c = c.replace('[ ','')
    c = c.replace('[','')
    c = c.replace(' ]','')
    c = c.replace(']','')
    while (c.find('  ')!=-1):
        c = c.replace('  ',' ')
        
    c = c.split(' ')
    print 'split c is: ',c
    for k in c:
        k = float(k)
        
    freq = np.asfarray(c, str)
    Draw_histogram(freq)
    
    print 'Histogram saved as png!' 

    
