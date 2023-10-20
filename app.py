from flask import Flask, render_template
from maze import generate_maze_dfs, add_border

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def display_maze():
    width, height = 75, 25
    maze = generate_maze_dfs(width, height)
    maze = add_border(maze)
    return render_template('maze.html', maze=maze)

if __name__ == '__main__':
    app.run()