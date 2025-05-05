import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # важно для 3D-графиков

def plot_trajectory(solution, title="Lorenz Attractor", color="blue", label=None):
    """
    Відображення траєкторії розв'язання в 3D просторі.
    """
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    x, y, z = solution.y
    ax.plot(x, y, z, color=color, label=label if label else "Trajectory")

    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title(title)

    if label:
        ax.legend()

    plt.tight_layout()
    plt.show()

def compare_trajectories(sol1, sol2, labels=("Trajectory 1", "Trajectory 2")):
    """
    Порівняння двох траєкторій на окремих підграфіках.
    """
    fig = plt.figure(figsize=(14, 6))

    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122, projection='3d')

    x1, y1, z1 = sol1.y
    x2, y2, z2 = sol2.y

    ax1.plot(x1, y1, z1, color='blue')
    ax1.set_title(labels[0])
    ax1.set_xlabel("X Axis")
    ax1.set_ylabel("Y Axis")
    ax1.set_zlabel("Z Axis")

    ax2.plot(x2, y2, z2, color='red')
    ax2.set_title(labels[1])
    ax2.set_xlabel("X Axis")
    ax2.set_ylabel("Y Axis")
    ax2.set_zlabel("Z Axis")

    plt.tight_layout()
    plt.show()
