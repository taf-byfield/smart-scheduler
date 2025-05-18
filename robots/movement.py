from farm import layout
import random

from farm.layout import occupied_pos
from robots.robots import robot1, robot2, holding_fruit


#define directions, up down left, right
def find_valid_moves(grid,r,c):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    moves =[]

    for Nr,Nc in directions:
        new_row = r + Nr
        new_col = c + Nc
        if (0 <= new_row < rows) and (0 <= new_col < cols):
            cell = grid[new_row][new_col]
            if cell != '#' and cell == '.': #adjusting for barriers
                moves.append((new_row,new_col)) #if cell is empty and less than total length of the grid #
                                                    # , move to new spot
            if not occupied_pos((new_row,new_col),robot2):
                moves.append((new_row,new_col))
    return moves
#*************************************************************************************************



#return to orignal position
def return_to_start(robot, grid):
    if not robot['holding_fruit']:
        return
    x,y = robot['position']
    sx, sy = robot['starting_point']

    # deliver message when back at original position
    if (x, y) == (sx, sy):
        print(f"Fruit delivered to base by Robot {robot['id']}")
        robot['holding_fruit'] = False
        return

    dx = sx - x
    dy = sy - y

    #moving horizontolly first
    if dx != 0:
        step_x = x + (1 if (dx > 0) else - 1)
        if grid[step_x][y] is None:
            grid[x][y] = None
            robot['position'] = (step_x, y)
            grid[step_x][y] = f"R{robot['id']}"
            return
    #vertical movements
    if dy != 0:
        step_y = y + (1 if (dy > 0) else - 1)
        if grid[x][step_y] is None:
            grid[x][y] = None
            robot['position'] = (x, step_y)
            grid[x][step_y] = f"R{robot['id']}"
            return

#************************************************************************

#movement
def movement(grid,robot_positions):
    robots = [robot1,robot2]

    for i,(r,c) in enumerate(robot_positions):  #fill spots if empty
        robot = robots[i]

        if robot['holding_fruit']:
            return_to_start(robot, grid)
            robot_positions[i] = robot['position']
            continue

        step_counter = 4
        valid_moves = find_valid_moves(grid,r,c)

        #preventing back tracing
        valid_moves = [i for i in valid_moves if i not in robot['past_steps']]

        #failsafe if trapped by memory or barrier
        if not valid_moves:
            print(f"Robot {robot['id']} has no valid moves, resetting at {r},{c}")
            robot['past_steps'].clear()
            valid_moves = find_valid_moves(grid, r, c)
            continue

        #***********************************************************
        # RANDOM MOVEMENT LOGIC BLOCK #
        if valid_moves:
            new_row, new_col = random.choice(valid_moves) #random movement 'with memory'
            grid[r][c] = None #make old pos avaliable
            #update pos of robots
            robot['past_steps'].append((r,c))
            if len(robot['past_steps']) == step_counter:
                robot['past_steps'].clear()
            robot_positions[i] = (new_row,new_col)
            robot['position'] = (new_row,new_col)
            grid[new_row][new_col] = f"R{i+1}"

            robot['position'] = (new_row, new_col) #reset
        #***********************************************************

    return grid,robot_positions
#*************************************************************************************************
