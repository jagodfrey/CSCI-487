import numpy as np
import random

#James Godfrey
#2/7/2017
#nQueens
def initialize(numQueens):
    # initialize board with random queens
    board = [[0 for x in range(numQueens)] for y in range(numQueens)]
    state = [0 for x in range(numQueens)]
    print('Empty Board: ')
    print(np.matrix(board))
    for x in range(0, numQueens):
        boardy = random.randint(0, numQueens - 1)
        board[x][boardy] = 1
        state[x] = boardy
    print("")
    return state


def printBoard(numQueens, state):
    board = [[0 for x in range(numQueens)] for y in range(numQueens)]
    for x in range(0, numQueens):
        board[x][int(state[x])] = 1
    print('Full Board: ')
    print(np.matrix(board))
    return board


# working! finds conflicts for a specific queen
def countQueenConf(state, row, col):
    count = 0
    for x in range(0, len(state)):
        if x == row:
            continue
        if state[x] == col or abs(x - row) == abs(state[x] - col):
            count += 1
            # print('State [', row, '][', col, '] conflicts with state [', x, state[x], ']')
    return count


# working! finds total conflicts
def totalConflicts(state):
    countConf = 0
    for x in range(0, len(state)):
        countConf += countQueenConf(state, x, state[x])
    return countConf

# working! solves conflicting nQueens using minimum conflict
def minConflictQueens(state, numQueens):
    counter = 0
    random.seed(8000)
    for iter in range(0, 1000):
        print('--------------------------------------------')
        print('~~~~~Beginning of Iteration~~~~~')
        print('State:', np.matrix(state))
        conflictQueens = []
        # determines if it is a solution or not
        if isFinalState(state):
            print('SOLUTION FOUND')
            print('Number of steps to completion: ', counter)
            return state

        # find the queens that are currently conflicting and store the column they are in
        for x in range(0, numQueens):
            if (countQueenConf(state, x, state[x]) != 0):
                conflictQueens.append(x)
        # receive the location of the queen chosen from the list of Queens in conflict
        randQueen = conflictQueens[random.randint(0, len(conflictQueens) - 1)]
        print('Queen selected: ',randQueen, 'value =', state[randQueen])
        colConf = []
        # find the conflict status of each row for that column and store in colConf.
        for y in range(0, len(state)):
            colConf.append(countQueenConf(state, randQueen, y))
        #add every element that is equal to the minimum value of conflicts to an array
        minConfRand = []
        for y in range(0, len(colConf)):
            if (colConf[y] == min(colConf)):
                minConfRand.append(y)
        #pick a random element from the list of equal conflict elements to swap with.
        newPlace = random.choice(minConfRand)
        print('Swap the value of element',randQueen,'that is currently=',state[randQueen],'with',newPlace)

        state[randQueen] = newPlace
        print('Post-Swap State: ', np.matrix(state))
        printBoard(numQueens, state)
        counter += 1
        print('~~~~~End of Iteration~~~~~')
    print('Did not complete, final matrix :')
    print('Incomplete State:', np.matrix(state))

#working! returns True if there are a total of 0 conflicts between any given queens.
def isFinalState(state):
    if (totalConflicts(state) == 0):
        return True
    elif (totalConflicts(state) != 0):
        return False


initialChoice = input("Enter 1 to choose random implementation and 2 for State entry S = [I, I2, I3, I4,...., In]")
#Random Board
if (int(initialChoice) == 1):
    numQueens = int(input('Enter the number of queens to be placed on the board: '))
    state = initialize(int(numQueens))
#User Entered State
elif (int(initialChoice) == 2):
    numQueens = int(input('Enter the number of queens to be placed on the board: '))
    state = [None] * numQueens
    print('Enter the State Elements one at a time please.')
    for x in range(numQueens):
        print('Enter the state for ', x, '; (0-', numQueens - 1, ')')
        state[x] = int(input())
    print('Initial State: ', np.matrix(state))
    print('Total Conflicts:', totalConflicts(state))
else:
    print("You entered an incorrect input")
#print board
printBoard(numQueens, state)
finalSolution = minConflictQueens(state, numQueens)
print('Final Solution: ',np.matrix(finalSolution))
printBoard(numQueens,state)

