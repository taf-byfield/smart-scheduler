from farm.layout import setup, display_grid
from robots.movement import movement
from robots.robots import robot1, robot2, holding_fruit, fruits_left
import time

def run_simulation(steps=25, delay=3):
    grid, robot_positions = setup()
    display_grid(grid)

    for step in range(steps):
        print(f"\n--- Step {step+1} ---")

        #checking directions for fruit
        for robot in [robot1, robot2]:
            holding_fruit(robot, grid)

        #movement..
        grid, robot_positions = movement(grid, robot_positions)
        display_grid(grid)

        if not fruits_left(grid) and not robot1['holding_fruit'] and not robot2['holding_fruit']:
            print("All fruit collected.")
            break

        time.sleep(delay)

if __name__ == "__main__":
    run_simulation()