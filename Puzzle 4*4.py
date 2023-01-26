
#---------------------------------------------------------------
#libraries:
import numpy as np
import math
import random
import time

#Finding the puzzle is solvable or not
N=4
def getInvCount(arr):
	arr1=[]
	for y in arr:
		for x in y:
			arr1.append(x)
	arr=arr1
	inv_count = 0
	for i in range(N * N - 1):
		for j in range(i + 1,N * N):
			# count pairs(arr[i], arr[j]) such that
			# i < j and arr[i] > arr[j]
			if (arr[j] and arr[i] and arr[i] > arr[j]):
				inv_count+=1
		
	
	return inv_count


# find Position of blank from bottom
def findXPosition(puzzle):
	# start from bottom-right corner of matrix
	for i in range(N - 1,-1,-1):
		for j in range(N - 1,-1,-1):
			if (puzzle[i][j] == 0):
				return N - i


# This function returns true if given
# instance of N*N - 1 puzzle is solvable
def isSolvable(puzzle):
	# Count inversions in given puzzle
	invCount = getInvCount(puzzle)

	# If grid is odd, return true if inversion
	# count is even.
	if (N & 1):
		return ~(invCount & 1)

	else: # grid is even
		pos = findXPosition(puzzle)
		if (pos & 1):
			return ~(invCount & 1)
		else:
			return invCount & 1
	


# Driver program to test above functions
def solvable_check(puzzle):


         print("The puzzle is Solvable press enter to solve") if  isSolvable(puzzle) else print("Not Solvable")
        

#✅ Number replacing Puzzle 4*4 solving with a* method

#STAR >>>

#function:
#---------------------------------------------------------------
def make_random_puzzle(): #making an random puzzle 4*4
    
    array = []
    for i in range(16):
        array.append(i)
    np.random.shuffle(array)

    puzzle = []
    n = 0
    for i in range(4):
        p = []
        for j in range(4):
            p.append(array[n])
            n = n + 1
        puzzle.append(p)
    puzzle = np.array(puzzle)
    print(puzzle)
    
    return(puzzle)
#---------------------------------------------------------------
def zero_position(puzzle): #finding 0 position 
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == 0:
                point = [i,j]
                return point
                break
#---------------------------------------------------------------
def position_finding(puzzle,f): #finding where can the 0 number move
    
    position = []#up down left right
    a = False
    for i in range(4):
        if a == False:
            for j in range(4):
                if puzzle[i][j]==0:
                    #up
                    if i == 0:
                        position.append(0)
                    else:
                        position.append(1)
                    #down   
                    if i == 3:
                        position.append(0)
                    else:
                        position.append(1)
                    #left   
                    if j == 0:
                        position.append(0)
                    else:
                        position.append(1)
                    #right  
                    if j == 3:
                        position.append(0)
                    else:
                        position.append(1)
                    a = True    
                    break
    if f>=0:
        position[f] = 0
        
    return position

#--------------------------------------------------------------
def criteria_sort():#sort goal
    
    criteria = []
    for i in range(16):
        criteria.append(i)
        
    return criteria
#--------------------------------------------------------------
def goal_puzzle(): #puzzle goal
    array = []
    for i in range(16):
        array.append(i)

    puzzle = []
    n = 0
    for i in range(4):
        p = []
        for j in range(4):
            p.append(array[n])
            n = n + 1
        puzzle.append(p)
    puzzle = np.array(puzzle)
    return puzzle
#---------------------------------------------------------------
def puzzle_sort(puzzle):
    
    result = []    
    for i in range(4):
        for j in range(4):
            result.append(puzzle[i][j])
    return result         
#---------------------------------------------------------------
def gain(puzzle): #cost function

    """ f(X) = g(X) + h(X) """ 
    
    criteria = criteria_sort()
    matrix_goal = goal_puzzle()
    result = puzzle_sort(puzzle)
            
    g = 0
    man = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if puzzle[i][j]!=0 and puzzle[i][j] == matrix_goal[k][l]:
                        x = abs(i-k)
                        y = abs(j-l)
                        man = x+y  #manhatan distance
                        g = g + man
            
    h = 0    
    for i in range(16):
        if result[i]!=0 and criteria[i] != result[i]:
            h = h + 1 # h missed place number
    f = h + g  #f      
    return f    
            
#---------------------------------------------------------------
def moving(puzzle,position,zero): #calculate the gain and find the best position 
    
    a = False
    for i in range(4):
        if a == False:
            for j in range(4):
                if puzzle[i][j]==0:
                    i0 = i
                    j0 = j
                    a == True
                    break
                
    condidate_list = []
    
    if position[0] == 1:
        c = puzzle[i0-1][j0]
        puzzle[i0][j0] = puzzle[i0-1][j0]
        puzzle[i0-1][j0] = 0
        g = gain(puzzle)#finding gain
        if zero[0]==i0-1 and zero[1]== j0:
            g = 100#random.randint(1, 2) #penalty
        puzzle[i0][j0] = 0
        puzzle[i0-1][j0] = c
        condidate_list.append(g)
        
    else:
        condidate_list.append(-1)
                
    if position[1] == 1:
        c =  puzzle[i0+1][j0]
        puzzle[i0][j0] = puzzle[i0+1][j0]
        puzzle[i0+1][j0] = 0
        
        if zero[0]==i0+1 and zero[1]== j0:
            g = 100 #random.randint(1, 2) #penalty
        else:
            g = gain(puzzle)
        condidate_list.append(g)
        puzzle[i0][j0] = 0
        puzzle[i0+1][j0] = c
        
    else:
        condidate_list.append(-1)
        
    if position[2] == 1:
        c = puzzle[i0][j0-1]
        puzzle[i0][j0] = puzzle[i0][j0-1]
        puzzle[i0][j0-1] = 0
        
        if zero[0]==i0 and zero[1]== j0-1:
            g = 100 #random.randint(1, 2) #penalty
        else:
            g = gain(puzzle)
        puzzle[i0][j0] = 0
        puzzle[i0][j0-1] = c
        condidate_list.append(g)
        
    else:
        condidate_list.append(-1)
        
    if position[3] == 1:
        c = puzzle[i0][j0+1]
        puzzle[i0][j0] = puzzle[i0][j0+1]
        puzzle[i0][j0+1] = 0
        
        
        if zero[0]==i0 and zero[1]== j0+1:
            g = 100 #penalty
        else:
            g = gain(puzzle)
        puzzle[i0][j0] = 0
        puzzle[i0][j0+1] = c
        condidate_list.append(g)
        
    else:
        condidate_list.append(-1)
        
    c = []    
    for i in range(len(condidate_list)):
        if condidate_list[i]>=0:
            c.append(condidate_list[i])
            
    condid = min(c) #finding the min f(x)
    for i in range(4):
        if condid == condidate_list[i]:
            number=i
            break
        
    if number == 0:
        puzzle[i0][j0] = puzzle[i0-1][j0]
        puzzle[i0-1][j0] = 0
        f = 1
        
    if number == 1:
        puzzle[i0][j0] = puzzle[i0+1][j0]
        puzzle[i0+1][j0] = 0
        f = 0
        
    if number == 2:
        puzzle[i0][j0] = puzzle[i0][j0-1]
        puzzle[i0][j0-1] = 0
        f = 3
        
    if number == 3:
        puzzle[i0][j0] = puzzle[i0][j0+1]
        puzzle[i0][j0+1] = 0
        f = 2
        
    print(puzzle)
    p =[puzzle,f]
    return p  
#--------------------------------------------------------------
def check(puzzle):
    
    a = True
    sort = criteria_sort()
    result = puzzle_sort(puzzle)
    l = len(sort)
    for i in range(l):
        if sort[i] != result[i]:
            return False
            break
        
    if a == True:
        pritn("\n")
        print("puzzle solved")
        
        return True
#---------------------------------------------------------------    
def percentage_correct(puzzle,save_first):
    
    sort = criteria_sort()
    result = puzzle_sort(puzzle)
    l = len(sort)
    correct = 0
    for i in range(l):
        if sort[i] == result[i]:
            correct = correct + 1
            
    result = round(correct/16,3)        
    if  result>=0.79:
        print("------------------------")
        print("------------------------")
        print(result*100,"% of Puzzle is solved")
        print("\n")
        print("Initial puzzel:\n")
        print(save_first)
        print("       ||")
        print("       ||")
        print("       \/")
        print(puzzle,"\n")
        print("correct number:",correct)
        
        return True
    else:
        return False
        
#---------------------------------------------------------------
#---------------------------------------------------------------       
#main function
def main():
    
    print("shuffled puzzle\n")  
    print("-------------------")
    puzzle = make_random_puzzle()
    save_first = np.copy(puzzle)
    print("\n")
    zero = zero_position(puzzle)
    go = solvable_check(puzzle)
    input()
    a = False
    step = 0
    f = -1
    z = 0
    x = 7
    if go != False:
        start_time = time.time()
        while a == False:
                        
            if z == x :
                zero = zero_position(puzzle)  #each three time the last third position of 0 saved
                z = 0
               
            position = position_finding(puzzle,f)
            puzzle0= moving(puzzle,position,zero)
            puzzle = puzzle0[0]
            f = puzzle0[1]
            step = step+1
            z = z + 1
            a = check(puzzle)
            a = percentage_correct(puzzle,save_first)
            
        print("%s seconds " % round((time.time() - start_time),2))
        print("step times: ",step)
        print("------------------------")
        print("------------------------")
#---------------------------------------------------------------    
if __name__ == "__main__":
    
    main()
    
input()    
#---------------------------------------------------------------    
    
    
#END<<<
