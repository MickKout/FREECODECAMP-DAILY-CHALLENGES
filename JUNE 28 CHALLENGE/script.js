// Given a matrix of strings representing pieces on a game grid, determine if any player has three in a row.

// Each cell contains "R", "Y", or "" (empty string).
// Three in a row means three consecutive non-empty cells of the same type horizontally, vertically, or diagonally.
// Return:

// A flat array with the winner and the coordinates of their three winning cells in the format: ["R", [0,2], [1,3], [2,4]]. Coordinates are returned top-to-bottom, then left-to-right.
// An empty array if there is no winner.

// Tests:
// Waiting:1. connectThree([["", "", "", ""], ["", "", "", ""], ["", "Y", "", ""], ["Y", "R", "R", "R"]]) should return ["R", [3, 1], [3, 2], [3, 3]].
// Waiting:2. connectThree([["", "", "", ""], ["", "Y", "Y", ""], ["", "Y", "R", "R"], ["", "Y", "R", "R"]]) should return ["Y", [1, 1], [2, 1], [3, 1]].
// Waiting:3. connectThree([["", "", "Y", "R"], ["", "Y", "R", "Y"], ["", "R", "Y", "R"], ["", "R", "Y", "R"]]) should return ["R", [0, 3], [1, 2], [2, 1]].
// Waiting:4. connectThree([["", "Y", "", ""], ["", "Y", "Y", ""], ["", "R", "R", "Y"], ["R", "R", "Y", "R"]]) should return ["Y", [0, 1], [1, 2], [2, 3]].
// Waiting:5. connectThree([["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"], ["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"]]) should return [].

function connectThree(matrix) {

const rows = matrix.length;
const cols = matrix[0].length;

for (let i = 0; i < rows; i++) {
  for (let j = 0; j < cols; j++) {
    if (matrix[i][j] !== "") {
      if (i + 2 < rows && matrix[i][j] === matrix[i + 1][j] && matrix[i][j] === matrix[i + 2][j]) {
        return [matrix[i][j], [i, j], [i + 1, j], [i + 2, j]];
      }
      if (j + 2 < cols && matrix[i][j] === matrix[i][j + 1] && matrix[i][j] === matrix[i][j + 2]) {
        return [matrix[i][j], [i, j], [i, j + 1], [i, j + 2]];
      }
      if (i + 2 < rows && j + 2 < cols && matrix[i][j] === matrix[i + 1][j + 1] && matrix[i][j] === matrix[i + 2][j + 2]) {
        return [matrix[i][j], [i, j], [i + 1, j + 1], [i + 2, j + 2]];
      }
      if (i + 2 < rows && j - 2 >= 0 && matrix[i][j] === matrix[i + 1][j - 1] && matrix[i][j] === matrix[i + 2][j - 2]) {
        return [matrix[i][j], [i, j], [i + 1, j - 1], [i + 2, j - 2]];
      }
    }
  }
}
return [];
}

console.log(connectThree([["", "", "", ""], ["", "", "", ""], ["", "Y", "", ""], ["Y", "R", "R", "R"]])); //should return ["R", [3, 1], [3, 2], [3, 3]].
console.log(connectThree([["", "", "", ""], ["", "Y", "Y", ""], ["", "Y", "R", "R"], ["", "Y", "R", "R"]])); //should return ["Y", [1, 1], [2, 1], [3, 1]].
console.log(connectThree([["", "", "Y", "R"], ["", "Y", "R", "Y"], ["", "R", "Y", "R"], ["", "R", "Y", "R"]])); // should return ["R", [0, 3], [1, 2], [2, 1]].
console.log(connectThree([["", "Y", "", ""], ["", "Y", "Y", ""], ["", "R", "R", "Y"], ["R", "R", "Y", "R"]])); //should return ["Y", [0, 1], [1, 2], [2, 3]].
console.log(connectThree([["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"], ["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"]])); // should return [].
