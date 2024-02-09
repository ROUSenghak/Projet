from grid import Grid
from solver import Solver

# Create a Grid object
grid = grid = Grid(2,3,[[6,2,3],[4,5,1]])  # Assuming a 2x3 grid for testing

# Print the initial state of the grid
print("Initial State:")
print(grid)

# Create a Solver object
solver = Solver(grid)

# Solve the grid
solution = solver.get_solution()

# Print the solution
print("\nSolution:")
print(solution)

# Apply the solution to the grid
for swap in solution:
    grid.swap(*swap)

# Print the final state of the grid after applying the solution
print("\nFinal State:")
print(grid)

