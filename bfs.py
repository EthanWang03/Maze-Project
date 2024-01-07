from collections import deque

def solve_maze_bfs(maze, start, end):
    # Checks if the move is valid (if there is a path there)
    def is_valid_move(row, col):
        rows, cols = len(maze), len(maze[0])
        return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0

    # Queue for BFS algorithm
    queue = deque([(start[0], start[1])])

    # Set to keep track of visited cells
    allVisited = [(start[0], start[1])]

    # Dictionary to store parent information for reconstructing the path
    parents = {(start[0], start[1]): None}

    while queue:
        # Current position
        row, col = queue.popleft()

        if (row, col) == end:
            # Reconstruct the path from end to start
            path = []
            while (row, col) != start:
                path.append((row, col))
                row, col = parents[(row, col)]
            path.append(start)
            path.reverse()
            return path, allVisited

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(new_row, new_col) and (new_row, new_col) not in allVisited:
                allVisited.append((new_row, new_col))
                queue.append((new_row, new_col))
                parents[(new_row, new_col)] = (row, col)

    # No path found
    return [], allVisited