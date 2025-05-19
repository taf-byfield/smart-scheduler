from farm.layout import setup, display_grid
from robots.movement import movement
from robots.robots import robot1, robot2, holding_fruit, fruits_left,in_bounds
from scheduler.core_scheduler import initialize_task,fruit_counter,task_status,report_hazards,get_tasks
from security.encrypt import send_message,decrypt_message,shift
from visualization.plots import robot_stats
from visualization.ui import start_pg,draw_grid,actions

import pygame as pg
import time


#MAIN FUNCTION TO RUN EVERYTHING
def run_simulation(steps=100, delay=1):
    initialize_task()
    grid, robot_positions = setup()
    display_grid(grid)

    screen = start_pg()
    draw_grid(screen,grid)

    print("Task Required for Each Robot")
    print("Robot 1:",get_tasks(robot1))
    print("Robot 2:",get_tasks(robot2))

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

        #PYGAME INTERFACE
        actions()
        draw_grid(screen,grid)


        #updating task and counter, message encryption, ect
        for robot in [robot1, robot2]:
            robot['steps'] += 1

            if robot['task_complete']:
                continue

            if robot['holding_fruit'] and robot['position'] == robot['starting_point']:
                fruit_counter(robot,robot['fruit_type'])
                robot['fruits_collected'] += 1
                message = f"Robot{robot['id']} delivered a {robot['fruit_type']}"
                encrypted_message = send_message(robot, message, shift)
                decrypt_message(robot, encrypted_message, shift)
                robot['holding_fruit'] = False
                robot['fruit_type'] = None

            #alert when task done
            if task_status(robot):
                print(f"Robot {robot['id']} has completed its task.")
                robot['task_complete'] = True

        #auto matically end if all fruits are collected
        if not fruits_left(grid) and not robot1['holding_fruit'] and not robot2['holding_fruit']:
            print("All fruit collected.")
            break

        #time.sleep(delay)
        pg.time.delay(int(delay*1000))
    #data for the bar graph
    stats = {
        'Robot1': {'Fruits Collected': robot1['fruits_collected'], 'Steps': robot1['steps']},
        'Robot2': {'Fruits Collected': robot2['fruits_collected'], 'Steps': robot2['steps']}
    }
    robot_stats(stats)

