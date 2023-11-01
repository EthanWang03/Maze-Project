const widthSlider = document.getElementById('width-slider');
const widthValue = document.getElementById('width-value');
const heightSlider = document.getElementById('height-slider');
const heightValue = document.getElementById('height-value');
const mazeContainer = document.getElementById('maze-container');
const generateButton = document.getElementById('generate-button');

widthSlider.addEventListener('input', () => {
    widthValue.textContent = widthSlider.value;
});

heightSlider.addEventListener('input', () => {
    heightValue.textContent = heightSlider.value;
});

$(document).ready(function(){
    $("#generate-button").click(function() {
        $.get('/generate_maze', function(data) {
            var mazeData = data.maze;
            console.log(mazeData);
        });
    });
});

function renderMaze(maze) {
    console.log('Received maze data:', maze);
    mazeContainer.innerHTML = ''; // Clear the maze container

    for (let row of maze) {
        const mazeRow = document.createElement('div');
        mazeRow.classList.add('maze-row');

        for (let cell of row) {
            const mazeCell = document.createElement('div');
            mazeCell.classList.add('maze-cell');
            if (cell === 1) {
                mazeCell.classList.add('wall');
            }
            mazeRow.appendChild(mazeCell);
        }

        mazeContainer.appendChild(mazeRow);
    }
}