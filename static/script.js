const widthSlider = document.getElementById('width-slider');
const widthValue = document.getElementById('width-value');
const heightSlider = document.getElementById('height-slider');
const heightValue = document.getElementById('height-value');

const mazeContainer = document.getElementById('maze-container');

const generateButton = document.getElementById('generate-button');

const solveButton = document.getElementById('solve-button');

const clearButton = document.getElementById('clear-button');

const solutionLength = document.getElementById('solution-length');
const solutionLengthValue = document.getElementById('solution-length-value');
const cellsVisited = document.getElementById('cells-visited');
const cellsVisitedValue = document.getElementById('cells-visited-value');
const executionTime = document.getElementById('execution-time');
const executionTimeValue = document.getElementById('execution-time-value');


mazeArray = undefined;

let timeoutIds = [];

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
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to generate maze. Please try again.');
        });
}

function renderMaze(mazeArray) {

    // Clear any existing content in the container
    mazeContainer.innerHTML = '';

    // Define CSS styles for walls and pathways and solution
    const wallStyle = 'wall';
    const pathStyle = 'path';
    // const solutionStyle = 'solution';
    // const visitedStyle = 'visited';

    // Create a table element to represent the maze
    const table = document.createElement('table');
    table.classList.add('maze-table');

    // Clear any tasks
    timeoutIds.forEach(id => clearTimeout(id));
    timeoutIds = [];

    solutionLengthValue.textContent = 0;
    cellsVisitedValue.textContent = 0;
    executionTimeValue.textContent = `0ms`;

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
            /*else if (cell === 2) {
                cellElement.classList.add(solutionStyle);
            }*/
            // 3 for visited pathway
            /* else if (cell === 3) {
                cellElement.classList.add(visitedStyle);
            }*/

            rowElement.appendChild(cellElement);
        }
        table.appendChild(rowElement);
    }

    mazeContainer.appendChild(table);
}

function renderMazeSolution(visitedArray, pathArray) {
    const solutionStyle = 'solution';
    const pathStyle = 'path';
    const mazeTable = document.querySelector('.maze-table');

    const startTime = performance.now();

    // clear any delayed processes
    timeoutIds.forEach(id => clearTimeout(id));
    timeoutIds = [];

    if (mazeTable) {
        const rows = mazeTable.getElementsByTagName('tr');

        for (let i = 0; i < pathArray.length; i++) {
            const [row, col] = pathArray[i];

            if (rows[row]) {
                const cells = rows[row].getElementsByTagName('td');

                // render solution path
                if (cells[col]) {
                    cells[col].classList.remove(pathStyle);
                    cells[col].classList.add(solutionStyle);
                }
            }
        }
    }

    solutionLengthValue.textContent = pathArray.length;
    cellsVisitedValue.textContent = visitedArray.length;
    const endTime = performance.now();
    const executionTime = (endTime - startTime); // Convert to seconds
    executionTimeValue.textContent = `${executionTime.toFixed(2)}ms`;
}

function wipeMaze() {
    const visitedStyle = 'visited';
    const pathStyle = 'path';
    const solutionStyle = 'solution';
    const mazeTable = document.querySelector('.maze-table');

    // clear any delayed processes 
    timeoutIds.forEach(id => clearTimeout(id));
    timeoutIds = [];

    solutionLengthValue.textContent = 0;
    cellsVisitedValue.textContent = 0;
    executionTimeValue.textContent = `0ms`;

    if (mazeTable) {
        const rows = mazeTable.getElementsByTagName('tr');

        for (let i = 0; i < rows.length; i++) {
            const cells = rows[i].getElementsByTagName('td');

            for (let j = 0; j < cells.length; j++) {
                const cell = cells[j];

                // Reset cell styles based on the classes
                if (cell.classList.contains(visitedStyle)) {
                    // Reset cell to path style if it was marked as visited
                    cell.classList.remove(visitedStyle);
                    cell.classList.add(pathStyle);
                } else if (cell.classList.contains(solutionStyle)) {
                    // Reset cell to path style if it was marked as a solution
                    cell.classList.remove(solutionStyle);
                    cell.classList.add(pathStyle);
                }

            }
        }
    }
    else {
        alert('No maze generated yet');
        return;
    }
}

// render the steps that are used to find the maze solution
function renderMazeSolutionWithSteps(visitedArray, pathArray) {
    const visitedStyle = 'visited';
    const pathStyle = 'path';
    const solutionStyle = 'solution';
    const mazeTable = document.querySelector('.maze-table');

    var solutionCounter = 0;
    var visitedCounter = 0;

    // clear any delayed processes 
    timeoutIds.forEach(id => clearTimeout(id));
    timeoutIds = [];

    const startTime = performance.now();

    if (mazeTable) {
        const rows = mazeTable.getElementsByTagName('tr');

        for (let i = 0; i < visitedArray.length; i++) {
            let timeoutId;
            const [row, col] = visitedArray[i];

            // set a delayed process for every 100ms
            timeoutId = setTimeout(() => {
                if (rows[row]) {
                    const cells = rows[row].getElementsByTagName('td');

                    if (cells[col]) {

                        // check if visited cell is part of the solution path
                        if (pathArray.some(([pathRow, pathCol]) => pathRow === row && pathCol === col)) {
                            cells[col].classList.remove(pathStyle);
                            cells[col].classList.add(solutionStyle);
                            solutionCounter = solutionCounter + 1;
                            visitedCounter = visitedCounter + 1
                        } else {
                            cells[col].classList.remove(pathStyle);
                            cells[col].classList.add(visitedStyle);
                            visitedCounter = visitedCounter + 1
                        }
                    }
                    solutionLengthValue.textContent = solutionCounter;
                    cellsVisitedValue.textContent = visitedCounter;
                }
                const endTime = performance.now();
                const executionTime = (endTime - startTime) / 1000; // Convert to seconds
                executionTimeValue.textContent = `${executionTime.toFixed(2)}s`;
            }, i * 50);

            timeoutIds.push(timeoutId);
        }
    }
}

document.getElementById('solve-button').addEventListener('click', function(event) {
    // Prevents page refresh
    event.preventDefault();

    // Solve Maze
    solveMaze();

    return false;
});

document.getElementById('clear-button').addEventListener('click', function(event) {
    // Prevents page refresh
    event.preventDefault();

    // Clear Maze
    wipeMaze();

    return false;
});

// Similar to generateMaze
function solveMaze() {

    const showStepsCheckbox = document.getElementById('showStepsCheckbox');
    const algorithmSelect = document.getElementById('algorithmSelect');

    const showSteps = showStepsCheckbox.checked;
    const selectedAlgorithm = algorithmSelect.value;

    if (mazeArray === undefined) {
        alert('No maze generated yet');
        return;
    }

    const formData = new FormData();
    formData.append('maze', JSON.stringify(mazeArray));
    formData.append('algorithm', selectedAlgorithm);

    // Get JSON return from python /generate
    fetch('/solve-maze', {
        method: 'POST',
        body: formData, // Pass the generated maze and algorithm drop down value
    })
        .then(response => response.json())
        .then(data => {

            visitedArray = data.visited;
            pathArray = data.path;

            //renderMazeSolutionWithSteps(visitedArray, mazeArray)
            //renderMazeSolution(mazeArray)

            if (showSteps) {
                wipeMaze();
                renderMazeSolutionWithSteps(visitedArray, pathArray);
            } else {
                wipeMaze();
                renderMazeSolution(visitedArray, pathArray);
            }
        })
        .catch(error => console.error('Error:', error));
}