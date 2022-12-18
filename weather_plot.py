import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

# Create a 100x100 grid with random values
grid = {}
for i in range(100):
    for j in range(100):
        grid[(i, j)] = random.randint(1, 40)

# Unpack the keys and values of the grid dictionary
xs, ys = zip(*grid.keys())
values = grid.values()

# Create a scatter plot of the grid
fig, ax = plt.subplots()
scatter = ax.scatter(xs, ys, c=list(values))
cbar = fig.colorbar(scatter)

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

                    # Modify the value of the current cell based on the value of the surrounding cell
                    if surrounding_value > current_value:
                        grid[(x, y)] += 1
                    elif surrounding_value < current_value:
                        grid[(x, y)] -= 1

    # Update the data of the scatter plot
    scatter.set_array(list(grid.values()))
    scatter.set_clim(vmin=min(grid.values()), vmax=max(grid.values()))
    # Stop the animation after 100 frames
    if num == 20000:
        ani.event_source.stop()

# Create an animation using the update function
ani = animation.FuncAnimation(fig, update, interval=200)
ani.save('animation.gif', writer='imagemagick')
# Show the animation
plt.show()
