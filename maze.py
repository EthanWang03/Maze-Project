import random

def generate_maze_dfs(width, height):
    # Create a grid of cells
    grid = [[1] * width for _ in range(height)]
    
    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height

    def get_unvisited_neighbors(x, y):
        neighbors = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
        unvisited = []

        for nx, ny in neighbors:
            if is_valid(nx, ny) and grid[ny][nx] == 1:
                unvisited.append((nx, ny))

        return unvisited

    def remove_wall_between(cx, cy, nx, ny):
        grid[ny][nx] = 0
        grid[cy + (ny - cy) // 2][cx + (nx - cx) // 2] = 0

    # Choose a random starting cell
    start_x = random.randrange(0, width, 2)
    start_y = random.randrange(0, height, 2)
    stack = [(start_x, start_y)]

    while stack:
        current_x, current_y = stack[-1]
        unvisited_neighbors = get_unvisited_neighbors(current_x, current_y)

        if unvisited_neighbors:
            next_x, next_y = random.choice(unvisited_neighbors)
            remove_wall_between(current_x, current_y, next_x, next_y)
            stack.append((next_x, next_y))
        else:
            stack.pop()

    return grid

def print_maze(maze):
    print("# " * (width + 2))
    for row in maze:
        print("# " + "".join(["# " if cell == 1 else "  " for cell in row]) + "#")
    print("# " * (width + 2))

width, height = 21, 21  # Adjust the size as needed
maze = generate_maze_dfs(width, height)

print_maze(maze)
