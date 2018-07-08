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
cost = [1, 1, 1] # the cost field has 3 values: right turn, no turn, left turn

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
				
				#print "x=", x, " y=", y
				for orient in range(len(forward)):
				
					#print "orient", orient
					if goal[0] == x and goal[1] == y:
						if value[orient][x][y] > 0:
							value[orient][x][y] = 0
							change = True
							
					elif grid[x][y] == 0:
						for a in range(len(forward)):
								
							#print "a=", a
							if a!=(orient+2)%4:
								x2 = x + forward[a][0]
								y2 = y + forward[a][1]
								orient2 = (orient + a) % 4
								
								if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
									
									if a==(orient+0)%4:
										cost_step=cost[1]
									elif a==(orient+1)%4:
										cost_step=cost[2]
									else:
										cost_step=cost[0]
										
									v2 = value[orient2][x2][y2] + cost_step
									#print v2
									
									if v2 < value[orient][x][y]:
										
										change = True
										value[orient][x][y] = v2
										
	
	print value
	
	policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
	
	x = init[0]
	y = init[1]
	orient = init[2]
	
	while (x!=goal[0])or(y!=goal[1]):
		flag = False
		vmin = 999
		for i in range(len(forward)):
			#if (x==2)and(y==1):
				#print "i=", i, "orient=", orient
			if i!=(orient+2)%4:
				x2 = x + forward[i][0]
				y2 = y + forward[i][1]
				orient2 = (orient + i) % 4
				#if (x==2)and(y==1):
					#print "i=", i
					#print "x2=", x2, " y2=", y2
					#print "Orient2=", orient2
				
				if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]) and grid[x2][y2] == 0:
					if value[orient2][x2][y2]<vmin:
						vmin = value[orient2][x2][y2]
						imin = i
						#if (x==2)and(y==1):
							#print imin
						orientmin=orient2
						xmin=x2
						ymin=y2
						flag = True
						#if (x==2)and(y==1):
							#print "vmin=", vmin, " imin=", imin
							#print "orientmin=", orientmin, " xmin=", xmin, " ymin=", ymin
						
	
		if flag and grid[x][y]==0:
			if imin==orient:
				move = action_name[1]
			elif imin==orient+1:
				move = action_name[2]
			else:
				move = action_name[0]
			
			#print 
			#print "vmin=", vmin, " imin=", imin
			#print 
			policy2D[x][y] = move
			
			x = xmin
			y = ymin
			orient = orientmin

	policy2D[goal[0]][goal[1]]='*'
	
	return policy2D # Make sure your function returns the expected grid.

print optimum_policy2D()


