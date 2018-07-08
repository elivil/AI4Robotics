# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]

#grid = [[0,1,0],[0,0,0]]
      
goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5                      
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100                    
cost_step = 1        
                     

############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.

def stochastic_value():
	value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
	policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
	
	change = True
	while change:
		
		change = False
		for x in range(len(grid)):
			for y in range(len(grid[0])):
				if goal[0]==x and goal[1]==y:
					if value[x][y]>0:
						value[x][y]=0
						change = True

				elif grid[x][y]==0:
					for a in range(len(delta)):
						x_success = x + delta[a][0]
						y_success = y + delta[a][1]
						x_left_fail = x + delta[(a+1)%4][0]
						y_left_fail = y + delta[(a+1)%4][1]
						x_right_fail = x + delta[(a-1)%4][0]
						y_right_fail = y + delta[(a-1)%4][1]
						
						if x_success >= 0 and x_success < len(grid) and y_success >= 0 and y_success < len(grid[0]) and grid[x_success][y_success] == 0:
							value_success = value[x_success][y_success]*success_prob
						else:
							value_success = collision_cost*success_prob
						
						if x_left_fail >= 0 and x_left_fail < len(grid) and y_left_fail >= 0 and y_left_fail < len(grid[0]) and grid[x_left_fail][y_left_fail] == 0:
							value_left_fail = failure_prob*value[x_left_fail][y_left_fail]
						else:
							value_left_fail = failure_prob*collision_cost
						
						if x_right_fail >= 0 and x_right_fail < len(grid) and y_right_fail >= 0 and y_right_fail < len(grid[0]) and grid[x_right_fail][y_right_fail] == 0:
							value_right_fail = failure_prob*value[x_right_fail][y_right_fail]
						else:
							value_right_fail = failure_prob*collision_cost
						
						v2 = value_success + value_left_fail + value_right_fail + cost_step
						
						if v2 < value[x][y]:
							change = True
							value[x][y] = v2
							
	return value


print stochastic_value()



