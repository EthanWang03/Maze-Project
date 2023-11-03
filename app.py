from flask import Flask, render_template, request, jsonify
from maze import generate_maze_dfs, add_border
import json

app = Flask(__name__, static_url_path='', static_folder='static')


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
    maze = add_border(maze)

    # Return maze to JSON
    return jsonify({'maze': maze})

if __name__ == '__main__':
    app.run()