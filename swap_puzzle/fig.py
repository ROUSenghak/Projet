
from grid import Grid
import matplotlib.pyplot as plt

def visualize_grid(grid):
    """
    Visualize the grid using matplotlib.

    Parameters:
    -----------
    grid: Grid
        The grid object to be visualized.
    """
    # Create a new figure
    plt.figure(figsize=(grid.n, grid.m))
    
    # Plot each cell with its corresponding number
    for i in range(grid.m):
        for j in range(grid.n):
            plt.text(j, grid.m - i - 1, grid.state[i][j], ha='center', va='center')
    
    # Set axis labels and title
    plt.xticks(range(grid.n))
    plt.yticks(range(grid.m), range(grid.m - 1, -1, -1))
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.title('Grid Visualization')
    
    # Display grid lines
    plt.grid(True)
    
    # Show plot
    plt.show()

# Example usage
grid = Grid(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
visualize_grid(grid)

