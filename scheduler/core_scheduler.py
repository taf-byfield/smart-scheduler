import random


tasks = {
    'robot1':{
        'apples_goal':0,
        'apples_collected':0,
        'oranges_goal':0,
        'oranges_collected':0,
        'hazards_reported':[]
    },
        'robot2':{
            'apples_goal':0,
            'apples_collected':0,
            'oranges_goal':0,
            'oranges_collected':0,
            'hazards_reported':[]
        },
}

##*********************************************************************************
def initialize_task():
    """Task for each robot with random amount of fruits to pick, between 1-10."""
    #robot 1 tasked with apples
    tasks['robot1']['apples_goal'] = random.randint(1,5)
    tasks['robot1']['oranges_goal'] = random.randint(1,5)

    #robot 2 tasked with oranges
    tasks['robot2']['apples_goal'] = random.randint(1,5)
    tasks['robot2']['oranges_goal'] = random.randint(1,5)

    for robot in tasks:
        tasks[robot]['apples_collected'] = 0
        tasks[robot]['oranges_collected'] = 0
        tasks[robot]['hazards_reported'] = []
##*************************************************************************

def fruit_counter(robot,fruit_type,amount=1):
    """Live Counter for num of fruits a robot has collected"""
    robot_id = f"robot{robot['id']}"
    if fruit_type == 'apple':
        tasks[robot_id]['apples_collected'] += amount
    elif fruit_type == 'orange':
        tasks[robot_id]['oranges_collected'] += amount

##*************************************************************************
def task_status(robot):
    """Check if the robot completed its task"""
    robot_id = f"robot{robot['id']}"
    r = tasks[robot_id]
    return (
            r['apples_collected'] >= r['apples_goal'] and
            r['oranges_collected'] >= r['oranges_goal']
    )

def report_hazards(robot,position):
    """Report a barrier/hazard on the farm grid"""
    robot_id = f"robot{robot['id']}"
    tasks[robot_id]['hazards_reported'].append(position)
    print(f"Hazard reported by Robot {robot_id} at {robot['position']}")

def get_tasks(robot):
    """Report progress on each task"""
    robot_id = f"robot{robot['id']}"
    return{
        'Pick Apples': tasks[robot_id]['apples_goal'],
        'Pick Oranges': tasks[robot_id]['oranges_goal'],
    }


