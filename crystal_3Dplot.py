import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import matplotlib.cm

# Create a 100x100 grid with random values
grid = {}
for i in range(100):
    for j in range(100):
        grid[(i, j)] = random.randint(1, 40)

# Unpack the keys and values of the grid dictionary
xs, ys = zip(*grid.keys())
values = grid.values()

# Create a 3D scatter plot of the grid
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
cmap = matplotlib.cm.get_cmap('cool')
scatter = ax.scatter(xs, ys, list(values), c=list(values), cmap=cmap)
#scatter = ax.scatter(xs, ys, values)

def update(num):
    # Iterate over each cell in the grid
    for x, y in grid.keys():
        # Get the value of the current cell
        current_value = grid[(x, y)]

        # Iterate over the surrounding cells
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Skip the current cell
                if i == 0 and j == 0:
                    continue

                # Get the coordinates of the surrounding cell
                surrounding_x = x + i
                surrounding_y = y + j

                # Check if the surrounding cell is within the grid
                if (surrounding_x, surrounding_y) in grid:
                    # Get the value of the surrounding cell
                    surrounding_value = grid[(surrounding_x, surrounding_y)]

                    # Modify the value of the current cell based on the value of the surrounding cell <--- setting >= the height in each point converge
                    if surrounding_value >= current_value:
                        grid[(x, y)] += 1
                    elif surrounding_value <= current_value:
                        grid[(x, y)] -= 1


    # Update the data of the scatter plot
    scatter.set_offsets(list(zip(xs, ys)))
    scatter.set_3d_properties(list(grid.values()), zdir='z')
    ax.auto_scale_xyz(xs, ys, list(values))
    # Stop the animation after 100 frames
    if num == 20000:
        ani.event_source.stop()


    # Stop the animation after 100 frames
    if num == 20000:
        ani.event_source.stop()


# Create an animation using the update function
ani = animation.FuncAnimation(fig, update, interval=200)
#ani.save('animation.gif', writer='imagemagick')
# Show the animation
plt.show()
