import random

def generate_maze_dfs(width, height):
    # Create a grid of cells
    # Set all cells to walls (1)
    grid = [[1] * width for _ in range(height)]
    
    def is_valid(x, y):
        # Checks if x position is valid
        # Checks if y position is valid
        # if both are valid return true else false  
        return 0 <= x < width and 0 <= y < height

    def get_unvisited_neighbors(x, y):
        # List of all neighboring cells
        neighbors = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]

        # List of all unvisited neighbors
        unvisited = []

        for nx, ny in neighbors:
            if is_valid(nx, ny) and grid[ny][nx] == 1:
                # if neighbor is valid and a wall cell add to unvisited list
                unvisited.append((nx, ny))

        return unvisited
    
    def add_border(maze):

        # Create new maze with width + 2 and height + 2
        width = len(maze[0])
        height = len(maze)
        # Set new maze to all walls
        new_maze = [[1] * (width + 2) for _ in range(height + 2)]

        # Create enterence and exit
        new_maze[1][0] = 0
        new_maze[height][width + 1] = 0

        #copy over old maze to new maze array
        for i in range(height):
            for j in range(width):
                new_maze[i + 1][j + 1] = maze[i][j]
        return new_maze

    def remove_wall_between(cx, cy, nx, ny):
        # Set the wall between (cx,cy) and (nx,ny) to path (0)
        grid[ny][nx] = 0
        grid[cy + (ny - cy) // 2][cx + (nx - cx) // 2] = 0

    # Choose a random starting cell
    # Set step to two to only generate even numbers
    # start_x = random.randrange(0, width, 2)
    # start_y = random.randrange(0, height, 2)

    # Start at (0,0)
    start_x = 0
    start_y = 0

    # Initialize stack with starting x and y 
    stack = [(start_x, start_y)]

    while stack:
        # Current x and y = stack.top()
        current_x, current_y = stack[-1]
        unvisited_neighbors = get_unvisited_neighbors(current_x, current_y)

        # If there are unvisited neighbors
        if unvisited_neighbors:
            # Choose a random unvisited neighbor to visit
            next_x, next_y = random.choice(unvisited_neighbors)
            remove_wall_between(current_x, current_y, next_x, next_y)
            stack.append((next_x, next_y))

        # If all adjacent cells have been visited pop the current cell
        # This leaves the top cell as the last unvisited 
        else:
            stack.pop()

    grid = add_border(grid)
    return grid



# Used for testing
def print_maze(maze):
    for row in maze:
        print("".join(["# " if cell == 1 else "  " if cell == 0 else "- " if cell == 2 else "= " for cell in row]))
        #print("".join(["## " if cell == 1 else "   " if cell == 0 else str(cell) + " " for cell in row]))

"""
width, height = 15, 15  # Adjust the size as needed
maze = generate_maze_dfs(width, height)

start = (1, 0)
end = (height, width + 1)

path, visited = solve_maze_bfs(maze, start, end)

print(path)
print(visited)
"""


