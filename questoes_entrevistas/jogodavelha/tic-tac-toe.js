const board = document.getElementById('board');
const cells = document.querySelectorAll('[data-cell]');
const status = document.getElementById('status');
const restartButton = document.getElementById('restart');
const themeToggle = document.getElementById('theme-toggle');

let currentPlayer = 'X';
let gameActive = true;
let gameState = ['', '', '', '', '', '', '', '', ''];

const winningCombinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
];

// Theme handling

/**
 * Toggles between light and dark theme
 * Saves the selected theme preference to localStorage
 */
function toggleTheme() {
    const isDark = document.body.getAttribute('data-theme') === 'dark';
    document.body.setAttribute('data-theme', isDark ? 'light' : 'dark');
    localStorage.setItem('theme', isDark ? 'light' : 'dark');
}

// Load saved theme
const savedTheme = localStorage.getItem('theme') || 'light';
document.body.setAttribute('data-theme', savedTheme);

// Handle cell click

/**
 * Handles the click event on a cell
 * Updates the game state, checks for win/draw conditions
 * and switches the current player
 * @param {Event} e - The click event object
 */
function handleClick(e) {
    const cell = e.target;
    const index = Array.from(cells).indexOf(cell);

    if (gameState[index] !== '' || !gameActive) return;

    gameState[index] = currentPlayer;
    cell.textContent = currentPlayer;
    
    if (checkWin()) {
        status.textContent = `Jogador ${currentPlayer} venceu!`;
        gameActive = false;
        return;
    }

    if (checkDraw()) {
        status.textContent = 'Empate!';
        gameActive = false;
        return;
    }

    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    status.textContent = `Vez do Jogador ${currentPlayer}`;
}

/**
 * Checks if the current player has won the game
 * @returns {boolean} True if current player has won, false otherwise
 */
function checkWin() {
    return winningCombinations.some(combination => {
        return combination.every(index => {
            return gameState[index] === currentPlayer;
        });
    });
}

/**
 * Checks if the game has ended in a draw
 * @returns {boolean} True if game is a draw, false otherwise
 */
function checkDraw() {
    return gameState.every(cell => cell !== '');
}

/**
 * Resets the game to its initial state
 * Clears the board, resets player turn and game status
 */
function restartGame() {
    currentPlayer = 'X';
    gameActive = true;
    gameState = ['', '', '', '', '', '', '', '', ''];
    status.textContent = `Vez do Jogador ${currentPlayer}`;
    cells.forEach(cell => cell.textContent = '');
}

// Event listeners
cells.forEach(cell => cell.addEventListener('click', handleClick));
restartButton.addEventListener('click', restartGame);
themeToggle.addEventListener('click', toggleTheme);
