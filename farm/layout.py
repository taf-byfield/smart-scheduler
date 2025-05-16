import random

cols = 15
rows = 15
num_fruits = 20

def make_grid(rows ,cols):
    grid = [[None for col in range(cols)] for row in range(rows)] #printing empty grid
    return grid

#defining robot pos***********************************************************************
def robots_pos(grid, robot_positions):
        for i,(r,c) in enumerate(robot_positions):  #pos of robots
            grid[r][c] = f"R{i+1}"  #robot 1 & robot 2
        return grid

#fruit placement***************************************************************************
def fruit_pos(grid,num_fruits):
    rows = len(grid)
    cols = len(grid[0])
    placed = 0

    while(placed < num_fruits):
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)

        if grid[r][c] is None:
            grid[r][c] = "F"
            placed += 1
    return grid

#display grid with fruit and robot pos******************************************************
def display_grid(grid):
    for row in grid:
        print(" ".join(cell if cell else "." for cell in row))


def main():
    grid = make_grid(rows , cols)
    robot_positions = [(0,14), (14,0)]
    grid = robots_pos(grid, robot_positions)
    grid = fruit_pos(grid, num_fruits)
    display_grid(grid)

if __name__ == "__main__":
    main()

