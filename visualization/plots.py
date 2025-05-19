import matplotlib.pyplot as plt

def robot_stats(stats):
    robots = list(stats.keys())

    fruits = [stats[robot]['Fruits Collected'] for robot in robots]
    steps_total = [stats[robot]['Steps'] for robot in robots]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 5))
    ax1.bar(robots, fruits, color='green')
    ax1.set_title('Fruits Collected')
    ax1.set_ylabel('Fruits')

    ax2.bar(robots, steps_total, color='blue')
    ax2.set_title('Total Steps Taken')
    ax2.set_ylabel('Steps')

    plt.tight_layout()
    plt.show()
