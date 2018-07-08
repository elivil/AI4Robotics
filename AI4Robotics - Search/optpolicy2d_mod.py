# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [2, 0] # final position
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
# 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

#orient = 0 a = 0 res =0
			#a=1	  res = 1
			#a =2	res =2
#orient = 1 a =0 res =1
			#a =3 res = 0
			



forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # do right
forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']


# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D():
	value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],[[999 for row in range(len(grid[0]))] for col in range(len(grid))],[[999 for row in range(len(grid[0]))] for col in range(len(grid))],[[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
	
	change = True
	
	while change:
		change = False
		
		for x in range(len(grid)):
			for y in range(len(grid[0])):
			
				for orient in range(len(forward)):
					if goal[0] == x and goal[1] == y:
						if value[orient][x][y] > 0:
							value[orient][x][y] = 0
							change = True
							
						elif grid[x][y] == 0:
							for a in range(len(forward)):
								if a!=orient+2:
									x2 = x + forward[a][0]
									y2 = y + forward[a][1]
									orient2 = (orient + a) % 4
									
									if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
										
										if a==orient:
											cost_step=cost[1]
										elif a==orient+1:
											cost_step=cost[2]
										else:
											cost_step=cost[0]
											
										v2 = value[orient2][x2][y2] + cost_step
										print v2
										
										if v2 < value[orient][x][y]:
											
											change = True
											value[orient][x][y] = v2
											
	
	print value
	policy2D=0
	
	return policy2D # Make sure your function returns the expected grid.

res = optimum_policy2D()


