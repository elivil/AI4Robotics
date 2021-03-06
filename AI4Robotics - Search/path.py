# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. NOTE: the 'v' should be 
# lowercase.
#
# Your function should be able to do this for any
# provided grid, not just the sample grid below.
# ----------


# Sample Test case
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# ----------------------------------------
# modify code below
# ----------------------------------------

def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0
    
    cache = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    open = [[g, x, y]]
    
    path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    back = False # flag set if we traced the path back 
    
    x3 = goal[0]
    y3 = goal[1]
    
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            cache[x2][y2] = delta_name[i]
                            closed[x2][y2] = 1
    
    #print found
                            
    while not back and not resign:
        
        if x3 == init[0] and y3 == init[1]:
            back = True
        else:
            #print "y", x3, " ", y3
            #print cache[x3][y3]
            j=delta_name.index(cache[x3][y3])
            x3 = x3 - delta[j][0]
            y3 = y3 - delta[j][1]
            path[x3][y3] = delta_name[j]
    
    
    path[goal[0]][goal[1]] = '*'
    return path # make sure you return the shortest path.

print search()


