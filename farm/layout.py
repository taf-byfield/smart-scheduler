import random
from robots.robots import robot2

cols = 15
rows = 15
num_fruits = 35
barriers = 10

def make_grid(rows ,cols):
    grid = [[None for col in range(cols)] for row in range(rows)] #printing empty grid
    return grid

#defining robot pos***********************************************************************
def robots_pos(grid, robot_positions):
        for i,(r,c) in enumerate(robot_positions):  #pos of robots
            grid[r][c] = f"R{i+1}"  #robot 1 & robot 2
        return grid

def occupied_pos(pos,robot2):
    return pos == robot2['position']

#fruit placement***************************************************************************
def fruit_pos(grid,num_fruits):
    rows = len(grid)
    cols = len(grid[0])
    placed_apples = 0
    placed_oranges = 0

    #placed apples
    while(placed_apples <= num_fruits):
        r = random.randint(0, rows - 1)     #keep placing until no more fruit
        c = random.randint(0, cols - 1)

        if grid[r][c] is None:
            grid[r][c] = "A"
            placed_apples += 1

    while (placed_oranges <= num_fruits):
        r = random.randint(0, rows - 1)  # keep placing until no more fruit
        c = random.randint(0, cols - 1)

        if grid[r][c] is None:
            grid[r][c] = "O"
            placed_oranges += 1
    return grid

#**********************************************************************8
#added obstacles through the grid
def obstacles(grid,barriers):
    count = 0
    while count < barriers:
        x = random.randint(0, len(grid) - 1)
        y = random.randint(0, len(grid[0])-1)
        if grid[x][y] is None:
            grid[x][y] = '#'
            count +=1


#display grid with fruit and robot pos******************************************************
def display_grid(grid):
    for row in grid:
        print(" ".join(cell if cell else "." for cell in row))

def setup():
    grid = make_grid(rows, cols)
    robot_positions = [(7, 6), (7, 8)]
    grid = robots_pos(grid, robot_positions)
    grid = fruit_pos(grid, num_fruits)
    obstacles(grid, barriers)
    return grid, robot_positions

def main():
    grid, robot_positions = setup()
    display_grid(grid)

if __name__ == "__main__":
    main()

