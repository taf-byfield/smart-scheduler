
#defining status of each robot
robot1 = {
    'id': 1,
    'position':(0,14),
    'starting_point':(0,14),
    'holding_fruit': False
}
robot2 = {
    'id': 2,
    'position':(14,0),
    'starting_point':(14,0),
    'holding_fruit': False
}
#*******************************************************************************************

#fruit sensing... if any direction contains fruit, clear and change status
def holding_fruit(robot, grid):
    x,y = robot['position']
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for Nx,Ny in directions:
        new_x, new_y = x + Nx, y + Ny

        if (0 <= new_x < len(grid)) and (0 <= new_y < len(grid[0])):
            if grid[new_x][new_y] == 'A':
                grid[new_x][new_y] = '.'    #if fruit, then clear
                robot['holding_fruit'] = True
                print(f"Robot{robot['id']} picked up an apple at {new_x},{new_y}")

                return True
    return False
#************************************************************************************

#number of fruits left
def fruits_left(grid):
    for row in grid:
        if 'A' in row:
            return True
    return False
#**********************************************************************************

#checking position
def in_bounds(new_x,new_y,grid):
    if (0 <= new_x < len(grid)) and (0 <= new_y < len(grid[0])):
        if grid[new_x][new_y] != '#':
            return True
    return False
#*****************************************************************************

def moving(robot,fruit,grid):
    x,y = robot['position']
    fx,fy = fruit

    dx = fx - x
    dy = fy - y
    #try to go left or right
    if dx != 0:
        go_x = x + (1 if (dx > 0)else -1)
        if in_bounds(go_x,y,grid):
            robot['position'] = (go_x, y)
            return True

    if dy != 0:
        go_y = y + (1 if (dy > 0)else -1)
        if in_bounds(x,go_y,grid):
            robot['position'] = (x, go_y)
            return True


