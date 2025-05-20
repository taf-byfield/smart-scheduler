
#defining status of each robot
robot1 = {
    'id': 1,
    'position':(7,6),
    'starting_point':(7,6),
    'holding_fruit': False,
    'fruit_type': None,
    'task_complete': False,
    'past_steps': [],
    'fruits_collected': 0,
    'steps': 0
}
robot2 = {
    'id': 2,
    'position':(7,8),
    'starting_point':(7,8),
    'holding_fruit': False,
    'fruit_type': None,
    'task_complete': False,
    'past_steps': [],
    'fruits_collected': 0,
    'steps': 0
}
#*******************************************************************************************

#fruit sensing... if any direction contains fruit, clear and change status
def holding_fruit(robot, grid):
    if robot['holding_fruit']:
        return False

    x,y = robot['position']
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for Nx,Ny in directions:
        new_x, new_y = x + Nx, y + Ny

        #checks to make sure robots are within the grid
        if (0 <= new_x < len(grid)) and (0 <= new_y < len(grid[0])):
            if (grid[new_x][new_y] == 'A') or (grid[new_x][new_y] == 'O'):
                if grid[new_x][new_y] == 'A':
                    fruit = 'apple'
                else:
                    fruit = 'orange'
                print(f"Robot{robot['id']} picked up an {fruit} at {new_x},{new_y}")
                grid[new_x][new_y] = '.'    #if fruit, then clear
                robot['fruits_collected'] += 1
                robot['holding_fruit'] = True
                robot['fruit_type'] = fruit

                return True
    return False
#************************************************************************************

#number of fruits left
def fruits_left(grid):
    for row in grid:
        if 'A' or 'O' in row:
            return True
    return False
#**********************************************************************************

#checking position
def in_bounds(new_x,new_y,grid):
    if (0 <= new_x < len(grid)) and (0 <= new_y < len(grid[0])):
        return grid[new_x][new_y] not in ['#','R1','R2']

    return False
#*****************************************************************************
from scheduler.core_scheduler import report_hazards
def moving(robot,fruit,grid):
    x,y = robot['position']
    fx,fy = fruit

    dx = fx - x
    dy = fy - y
    #try to go left or right
    if dx != 0:
        go_x = x + (1 if (dx > 0)else -1)
        if 0 <= go_x < len(grid):
            if in_bounds(go_x,y,grid) and grid[go_x][y] != '#':
                robot['position'] = (go_x,y)
                robot['steps'] += 1
                return True
    #up or down
    if dy != 0:
        go_y = y + (1 if (dy > 0)else -1)
        if in_bounds(x,go_y,grid) and grid[x][go_y] != '#':
            robot['position'] = (x, go_y)
            robot['steps'] += 1
            return True

    return False
