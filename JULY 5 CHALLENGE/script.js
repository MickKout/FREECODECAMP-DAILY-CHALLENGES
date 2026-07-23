// Bucket Fill
//   Given a 2D grid, a starting position ([row, col]), and a new value, replace the value at the starting position and all connected cells of the same value with the new value.

// Cells are connected if they are adjacent horizontally or vertically (not diagonally).
// Return the updated grid.

function bucketFill(grid, [row, col], newValue) {

  const visited = new Set();
  const queue = [[row, col]];
  const startValue = grid[row][col];

  while (queue.length) {
    const [row, col] = queue.shift();
    if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length || grid[row][col] !== startValue || visited.has(`${row},${col}`)) {
      continue;
    }
    visited.add(`${row},${col}`);
    grid[row][col] = newValue;
    queue.push([row - 1, col]);
    queue.push([row + 1, col]);
    queue.push([row, col - 1]);
    queue.push([row, col + 1]);
  }
  return grid;

}

console.log(bucketFill([["R", "G"], ["R", "G"]], [0, 1], "B"));
console.log(bucketFill([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B"));
console.log(bucketFill([["O", "O", "P"], ["P", "O", "O"], ["P", "P", "O"]], [2, 0], "R"));
console.log(bucketFill([["T", "T", "R", "T"], ["R", "T", "R", "T"], ["R", "T", "R", "T"], ["T", "T", "T", "T"]], [0, 3], "Y"));
console.log(bucketFill([["G", "B", "G", "B"], ["R", "B", "B", "G"], ["B", "G", "B", "R"], ["B", "G", "G", "B"]], [2, 2], "G"));