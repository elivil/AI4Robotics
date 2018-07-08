# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    path = []
    already_visited = []
    calc_next_step = []
    
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            row.append(grid[i][j])
            
        already_visited.append(row)

    for i in range(len(grid)):
        row = []

        for j in range(len(grid[0])):
            row.append(grid[i][j])

        calc_next_step.append(row)

    #print grid
    #print already_visited
    #print calc_next_step[0][0]
        
    opengr = [[0, init[0], init[1]]]
    already_visited[init[0]][init[1]] = 1
    #print calc_next_step[0][0]
    imin = 0
    poss_x = init[0]
    poss_y = init[1]
    gmin = len(grid)*len(grid[0])
    found = 1
    
    while ((poss_x!=goal[0])or(poss_y!=goal[1]))and(found):
        found = 0
        for i in range(len(opengr)):
            #print "y", i
            #print "nxt", calc_next_step[0][0]
            if (opengr[i][0]<=gmin)and(calc_next_step[opengr[i][1]][opengr[i][2]]!=1):
                #print "if"
                gmin = opengr[i][0]
                imin = i
                found = 1

        #print "possx", poss_x
        #print "possy", poss_y
        #print "gmin", gmin
        #print "imin",  imin
        #print "nxtst", calc_next_step[opengr[imin][1]][opengr[imin][2]] 
        
        if (calc_next_step[opengr[imin][1]][opengr[imin][2]]!=1):
            j = 0

            while (not((poss_x==goal[0])and(poss_y==goal[1])))and(j<len(delta)):

                if ((opengr[imin][1]+delta[j][0])>=0)and((opengr[imin][1]+delta[j][0])<len(grid)):
                    
                    if ((opengr[imin][2]+delta[j][1])>=0)and((opengr[imin][2]+delta[j][1])<len(grid[0])):
                        poss_x = opengr[imin][1]+delta[j][0]
                        poss_y = opengr[imin][2]+delta[j][1]
                        #print "possx", poss_x 
                        #print "possy", poss_y
                        if (already_visited[poss_x][poss_y]!=1):
                            opengr.append([gmin+cost, poss_x, poss_y])
                            already_visited[poss_x][poss_y] = 1
                            #print opengr
                j = j+1            

            calc_next_step[opengr[imin][1]][opengr[imin][2]] = 1
            gmin = len(grid)*len(grid[0])

    #print found
    
    if (found):
        path.append(opengr[len(opengr)-1])
    else:
        path.append("fail")
    
    return path[0] # you should RETURN your result

print search()


