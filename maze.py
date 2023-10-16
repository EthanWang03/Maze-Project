import random


def create_grid(width, height):
    maze = []
    for i in range (0,height):
        line = []
        for j in range (0, width):
            line.append('@')
        maze.append(line)
    return maze

def print_grid(grid):
    for i in range (0,len(grid)):
        for j in range(0, len(grid[0])):
            print(grid[i][j], end='   ')
        print('\n')

def starting_cell(grid):
    width = len(grid[0])
    height = len(grid)
    
    starting_x = int(random.random()*width)
    starting_y = int(random.random()*height)

    if starting_y == 0:
        starting_y += 1
    if starting_y == height-1:
        starting_y -= 1
    if starting_x == 0:
        starting_x += 1
    if starting_x == width-1:
        starting_x -= 1
    return (starting_x, starting_y)

def get_unvisited_neighbors(grid, cell):
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    neighbors = []

    width = len(grid[0])
    height = len(grid)

    current_x, current_y = cell
    
    for dx, dy in directions:
        new_x, new_y = current_x + dx, current_y + dy


        if 0 <= new_x < width and 0 <= new_y < height:

            if grid[new_y][new_x] == 0:
                neighbors.append((new_x, new_y))

    return neighbors

def random_choice(neighbors):
    index = random.randint(0, len(neighbors) - 1)
    return neighbors[index]

def generate_maze_DFS(width, height):
    grid = create_grid(width, height)
    start_cell = starting_cell(grid)
    stack = [start_cell]
    while stack:
        current_cell = stack[-1]
        neighbors = get_unvisited_neighbors(grid, current_cell)
        if neighbors:
            neighbor = random_choice(neighbors)
            
    return grid

grid = generate_maze_DFS(10,10)
print_grid(grid)  
