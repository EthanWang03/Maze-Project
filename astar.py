import heapq

# A* algorithm works by traveling to nodes that are the closest to the goal allowing for fast solutions
def solve_maze_astar(maze, start, end):

    # Estimate the remaining cost from a node to the goal
    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def is_valid_move(row, col):
        rows, cols = len(maze), len(maze[0])
        return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0

    # Priority queue for A* algorithm
    open_set = [(0, start)]
    heapq.heapify(open_set)

    # Dictionary to store the cost to reach each node
    g_scores = {start: 0}

    # Dictionary to store the previous node in the optimal path
    came_from = {}

    # Path to exit
    path = [(start[0], start[1])]

    # Set to keep track of visited cells
    allVisited = [(start[0], start[1])]

    while open_set:
        current_cost, current_node = heapq.heappop(open_set)

        if current_node == end:
            # Reconstruct the path
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            break

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = current_node[0] + dr, current_node[1] + dc
            new_cost = g_scores[current_node] + 1

            if is_valid_move(new_row, new_col):
                if (new_row, new_col) not in g_scores or new_cost < g_scores[(new_row, new_col)]:
                    g_scores[(new_row, new_col)] = new_cost
                    priority = new_cost + heuristic((new_row, new_col), end)
                    heapq.heappush(open_set, (priority, (new_row, new_col)))
                    came_from[(new_row, new_col)] = current_node

                    allVisited.append((new_row, new_col))

    return path, allVisited