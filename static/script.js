const widthSlider = document.getElementById('width-slider');
const widthValue = document.getElementById('width-value');
const heightSlider = document.getElementById('height-slider');
const heightValue = document.getElementById('height-value');
const mazeContainer = document.getElementById('maze-container');
const generateButton = document.getElementById('generate-button');
const solveButton = document.getElementById('solve-button');

mazeArray = undefined;

widthSlider.addEventListener('input', () => {
    widthValue.textContent = widthSlider.value;
});

heightSlider.addEventListener('input', () => {
    heightValue.textContent = heightSlider.value;
});

document.getElementById('generate-button').addEventListener('click', function(event) {
    // Get width and height values from slider
    event.preventDefault();

    const width = parseInt(document.getElementById('width-slider').value);
    const height = parseInt(document.getElementById('height-slider').value);

    // Clear any existing maze
    mazeArray = undefined;

    // Generate and display Maze
    generateMaze(width, height);

    return false;
});

function generateMaze(width, height) {

    // Get JSON return from python /generate
    fetch('/generate-maze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ width, height }),
    })
        .then(response => response.json())
        .then(data => {
            mazeArray = data.maze;
            renderMaze(mazeArray)
        })
        .catch(error => console.error('Error:', error));
}

function renderMaze(mazeArray) {

    // Clear any existing content in the container
    mazeContainer.innerHTML = '';

    // Define CSS styles for walls and pathways and solution
    const wallStyle = 'wall';
    const pathStyle = 'path';
    const solutionStyle = 'solution';

    // Create a table element to represent the maze
    const table = document.createElement('table');
    table.classList.add('maze-table'); // You can apply CSS styles to this class

    // Iterate through the mazeArray and create rows and cells accordingly
    for (let row of mazeArray) {
        const rowElement = document.createElement('tr');
        for (let cell of row) {
            const cellElement = document.createElement('td');

            // 1 for wall
            if (cell === 1) {
                cellElement.classList.add(wallStyle);
            }
            // 0 for pathway
            else if (cell === 0) {
                cellElement.classList.add(pathStyle);
            }
            // 2 for solution pathway
            else if (cell === 2) {
                cellElement.classList.add(solutionStyle);
            }

            rowElement.appendChild(cellElement);
        }
        table.appendChild(rowElement);
    }

    mazeContainer.appendChild(table);
}

document.getElementById('solve-button').addEventListener('click', function() {
    // Prevents page refresh
    event.preventDefault();

    // Solve Maze
    solveMaze();

    return false;
});

// Similar to generateMaze
function solveMaze() {
    if (mazeArray === undefined) {
        alert('No maze generated yet');
        return;
    }
    // Get JSON return from python /generate
    fetch('/solve-maze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ maze: mazeArray }), // Pass the generated maze
    })
        .then(response => response.json())
        .then(data => {
            mazeArray = data.maze;
            renderMaze(mazeArray);
        })
        .catch(error => console.error('Error:', error));
}