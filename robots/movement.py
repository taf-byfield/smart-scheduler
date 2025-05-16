from farm import layout
import random

from farm.layout import display_grid


#define directions, up down left, right
def find_valid_moves(grid,r,c):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    moves =[]

    for Nr,Nc in directions:
        new_row = r + Nr
        new_col = c + Nc
        if (0 <= new_row < rows) and (0 <= new_col < cols) and (grid[new_row][new_col] is None):
            moves.append((new_row,new_col)) #if cell is empty and less than total length of the grid
                                            # , move to new spot

    return moves
#*************************************************************************************************

#movement
def movement(grid,robot_positions):
    for i,(r,c) in enumerate(robot_positions):  #fill spots if empty
        valid_moves = find_valid_moves(grid,r,c)

        if valid_moves:
            new_row,new_col = random.choice(valid_moves)    #random movement

            grid[r][c] = None #make old pos avaliable
            #update pos of robots
            robot_positions[i] = (new_row,new_col)
            grid[new_row][new_col] = f"R{i+1}"

    return grid,robot_positions
#*************************************************************************************************
