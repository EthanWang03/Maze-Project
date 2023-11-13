from flask import Flask, render_template, request, jsonify
from maze import generate_maze_dfs, solve_maze_dfs
import sys

app = Flask(__name__, static_url_path='', static_folder='static')
print(sys.getrecursionlimit())

@app.route('/')

def display_maze():
    return render_template('maze.html')

@app.route('/generate-maze', methods=['POST'])
def generate_maze():

    # Get height and width values from slider
    width = int(request.json.get('width'))
    height = int(request.json.get('height'))

    # Generate Maze
    maze = generate_maze_dfs(width, height)

    # Return maze to JSON
    return jsonify({'maze': maze})

@app.route('/solve-maze', methods=['POST'])
def solve_maze():
    maze = request.json.get('maze')

    # Account for new larger size 
    height = len(maze) - 2
    width = len(maze[0]) - 2
 
    # start will always be the same
    start = (1, 0)
    end = (height, width + 1)

    # Solve the maze
    maze = solve_maze_dfs(maze, start, end)

    return jsonify({'maze': maze})

if __name__ == '__main__':
    app.run()