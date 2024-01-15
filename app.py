from flask import Flask, render_template, request, jsonify, json
from maze import generate_maze_dfs
from bfs import solve_maze_bfs
from dfs import solve_maze_dfs
from astar import solve_maze_astar

app = Flask(__name__)

@app.route('/')

def display_maze():
    return render_template('maze.html')

@app.route('/generate-maze', methods=['POST'])
def generate_maze():

    # Get height and width values from slider
    width = int(request.json.get('width'))
    height = int(request.json.get('height'))

    height = int(request.json.get('height'))

    # Generate Maze
    maze = generate_maze_dfs(width, height)

    # Return maze to JSON
    return jsonify({'maze': maze})

@app.route('/solve-maze', methods=['POST'])
def solve_maze():

    # get maze array 
    maze = json.loads(request.form.get('maze'))

    # Account for new larger size 
    height = len(maze) - 2
    width = len(maze[0]) - 2
 
    # start will always be the same
    start = (1, 0)
    end = (height, width + 1)

    selected_algorithm = request.form.get('algorithm')

    # print(selected_algorithm)

    # Solve the maze
    # Solve the maze
    if selected_algorithm == 'dfs':
        path, allVisited = solve_maze_dfs(maze, start, end)
    elif selected_algorithm == 'bfs':
        path, allVisited = solve_maze_bfs(maze, start, end)
    elif selected_algorithm == 'astar':
        path, allVisited = solve_maze_astar(maze, start, end)
    else:
        return jsonify({'error': 'Invalid algorithm'})

    # print("Visited cells:", allVisited)

    return jsonify({'path': path, 'visited': allVisited})

if __name__ == '__main__':
    app.run()