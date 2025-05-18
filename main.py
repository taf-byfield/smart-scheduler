from farm.layout import setup, display_grid
from robots.movement import movement
from robots.robots import robot1, robot2, holding_fruit, fruits_left,in_bounds
from scheduler.core_scheduler import initialize_task,fruit_counter,task_status,report_hazards,get_tasks

import time

def run_simulation(steps=200, delay=0.2):
    initialize_task()
    grid, robot_positions = setup()
    display_grid(grid)

    print("Taks")
    print("Robot1:",get_tasks(robot1))
    print("Robot2:",get_tasks(robot2))

    for step in range(steps):
        print(f"\n--- Step {step+1} ---")

        #checking directions for fruit
        for robot in [robot1, robot2]:
            holding_fruit(robot, grid)
            #task checking
            x,y = robot['position']
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny = x + dx, y + dy
                if in_bounds(nx, ny, grid):
                    if grid[nx][ny] == 'A':
                        robot['fruit_type'] = 'apple'
                    elif grid[nx][ny] == 'O':
                        robot['fruit_type'] = 'orange'

        #movement..
        grid, robot_positions = movement(grid, robot_positions)
        display_grid(grid)

        #updating task and counter.
        for robot in [robot1, robot2]:
            if robot['holding_fruit'] and robot['position'] == robot['starting_point']:
                fruit_counter(robot,robot['fruit_type'])
                print(f"Robot{robot['id']} delivered a {robot['fruit_type']}")
                robot['holding_fruit'] = False
                robot['fruit_type'] = None

                if task_status(robot):
                    print(f"Robot {robot['id']} has completed its task.")
                    robot['task_complete'] = True

        if not fruits_left(grid) and not robot1['holding_fruit'] and not robot2['holding_fruit']:
            print("All fruit collected.")
            break

        time.sleep(delay)

if __name__ == "__main__":
    run_simulation()