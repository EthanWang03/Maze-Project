import random

def solve_maze_dfs(maze, start, end):
    
    # Checks if the move is valid (if there is a path there)
    def is_valid_move(row, col):
        rows, cols = len(maze), len(maze[0])
        return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0

    # Stack for DFS algorithm
    stack = [(start[0], start[1])]

    # Set to keep track of visited cells 
    visited = set(stack)

    # Path to exit
    path = []

    allVisitied = []
    
    allVisitied.append((1,0))

    while stack:

        # Current position
        row, col = stack[-1]

        if (row, col) == end:
            # Record the path
            path.extend(stack)
            break

        found = False

        # choose a random direction to travel to
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        random.shuffle(directions)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(new_row, new_col) and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                allVisitied.append((new_row, new_col))
                stack.append((new_row, new_col))
                found = True
                break

        if not found:
            stack.pop()  # Backtrack
    """
    if path:
        for r, c in path:
            # Mark solution path
            maze[r][c] = 2
    else:
        print("No path found.")
    """

    # print(allVisitied)

    return path, allVisitied