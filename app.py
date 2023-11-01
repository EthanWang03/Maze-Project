from flask import Flask, render_template, request, jsonify
from maze import generate_maze_dfs, add_border
import json

app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.route('/')

def display_maze():
    return render_template('maze.html')

@app.route('/generate_maze', methods=['GET'])
def generate_maze():

    width = int(request.args.get('width', 25))
    height = int(request.args.get('height', 25))
    
    print('1')

    maze = generate_maze_dfs(width, height)
    maze = add_border(maze)

    return jsonify({'maze': maze})

if __name__ == '__main__':
    app.run(debug=True)