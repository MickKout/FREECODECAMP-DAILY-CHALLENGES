# Connect Three — Code Explained

> Scan a 2D grid of game pieces and detect if any player has three matching pieces in a row — horizontally, vertically, or diagonally.

---

## Table of Contents
1. [The Problem in Plain English](#1-the-problem-in-plain-english)
2. [Understanding the Grid](#2-understanding-the-grid)
3. [The Four Win Directions](#3-the-four-win-directions)
4. [How the Algorithm Works](#4-how-the-algorithm-works)
5. [Step-by-Step Code Breakdown](#5-step-by-step-code-breakdown)
6. [Boundary Checks Explained](#6-boundary-checks-explained)
7. [Worked Examples](#7-worked-examples)
8. [Methods Used](#8-methods-used)
9. [Full Annotated Code](#9-full-annotated-code)

---

## 1. The Problem in Plain English

Imagine a board game grid like Connect Four. Two players take turns placing coloured pieces — `"R"` (Red) and `"Y"` (Yellow) — on the grid. Empty cells are represented by `""`.

The goal is to detect whether any player has placed **three of their pieces in a consecutive line**, in any of the four possible directions. If a winner is found, return who won and the exact grid coordinates of their three winning cells. If nobody has three in a row, return an empty array.

```
Input grid (4 rows × 4 columns):

     col0  col1  col2  col3
row0 [ "",   "",   "",   "" ]
row1 [ "",   "",   "",   "" ]
row2 [ "",  "Y",   "",   "" ]
row3 ["Y",  "R",  "R",  "R" ]   ← R has three in a row!

Output: ["R", [3,1], [3,2], [3,3]]
```

---

## 2. Understanding the Grid

The grid is a **matrix** — an array of arrays. Each inner array is one row. Each element inside a row is one cell.

```js
matrix[i][j]
//      ↑  ↑
//      │  └── column index (left → right)
//      └───── row index    (top → bottom)
```

So `matrix[3][1]` means: row 3, column 1.

```
         j=0   j=1   j=2   j=3
i=0  [  "",   "",   "",   ""  ]
i=1  [  "",   "",   "",   ""  ]
i=2  [  "",  "Y",   "",   ""  ]
i=3  [ "Y",  "R",  "R",  "R" ]
              ↑
         matrix[3][1] = "R"
```

---

## 3. The Four Win Directions

From any starting cell `[i, j]`, three-in-a-row can go in exactly four directions. The algorithm checks each one:

```
Direction             Pattern                 Cell offsets from [i,j]
─────────────────────────────────────────────────────────────────────
↓  Vertical           [i,j] [i+1,j] [i+2,j]      rows increase, col fixed
→  Horizontal         [i,j] [i,j+1] [i,j+2]      row fixed, cols increase
↘  Diagonal down-right [i,j] [i+1,j+1] [i+2,j+2] both increase
↙  Diagonal down-left  [i,j] [i+1,j-1] [i+2,j-2] row increases, col decreases
```

Visualised on the grid:

```
  ↓ Vertical      → Horizontal    ↘ Down-right    ↙ Down-left
  X . . .         X X X .         X . . .         . . . X
  X . . .         . . . .         . X . .         . . X .
  X . . .         . . . .         . . X .         . X . .
```

> **Why only these four?** The loop already moves left-to-right and top-to-bottom, so directions like ← (left) or ↑ (up) would just be duplicates of directions already checked at the starting cell of that line.

---

## 4. How the Algorithm Works

The strategy is called a **sliding window scan**:

1. Visit every cell in the grid from top-left to bottom-right
2. Skip empty cells (they can never be the start of a win)
3. For each non-empty cell, try all four directions
4. For each direction, check if the next two cells match the current one
5. If they do, a winner is found — return immediately
6. If the entire grid is scanned with no winner, return `[]`

The key insight is that we only need to check **forward** directions (down, right, down-right, down-left) because:
- The loop processes cells left-to-right, top-to-bottom
- Any three-in-a-row will always have a topmost/leftmost starting cell
- That starting cell will be visited before the other two cells in the line

---

## 5. Step-by-Step Code Breakdown

### Step 1 — Measure the grid

```js
const rows = matrix.length;       // number of rows (vertical size)
const cols = matrix[0].length;    // number of columns (horizontal size)
```

`matrix.length` counts the outer array's elements — each one is a row.  
`matrix[0].length` counts the elements of the first row — each one is a column.

For a 4×4 grid: `rows = 4`, `cols = 4`.

---

### Step 2 — Scan every cell with nested loops

```js
for (let i = 0; i < rows; i++) {       // i = row index (top → bottom)
  for (let j = 0; j < cols; j++) {     // j = column index (left → right)
```

The outer loop moves through rows (top to bottom).  
The inner loop moves through columns within each row (left to right).  
Together they visit every cell exactly once, in this order:

```
[0,0] [0,1] [0,2] [0,3]
[1,0] [1,1] [1,2] [1,3]
[2,0] [2,1] [2,2] [2,3]
[3,0] [3,1] [3,2] [3,3]
```

---

### Step 3 — Skip empty cells

```js
if (matrix[i][j] !== "") {
  // ... all direction checks go here
}
```

An empty cell `""` can never be the start of a three-in-a-row. Skipping them avoids false matches where three empty cells could theoretically "match" each other. All four direction checks live inside this guard.

---

### Step 4 — Check vertical (↓)

```js
if (i + 2 < rows &&
    matrix[i][j] === matrix[i + 1][j] &&
    matrix[i][j] === matrix[i + 2][j]) {
  return [matrix[i][j], [i, j], [i + 1, j], [i + 2, j]];
}
```

Checks three cells stacked vertically: current cell, one below, two below.
- `i + 2 < rows` — boundary check: ensures `i+2` doesn't go past the last row
- `matrix[i+1][j]` — same column, one row down
- `matrix[i+2][j]` — same column, two rows down

```
[i,  j]   ← current
[i+1,j]   ← one down
[i+2,j]   ← two down
```

---

### Step 5 — Check horizontal (→)

```js
if (j + 2 < cols &&
    matrix[i][j] === matrix[i][j + 1] &&
    matrix[i][j] === matrix[i][j + 2]) {
  return [matrix[i][j], [i, j], [i, j + 1], [i, j + 2]];
}
```

Checks three cells in the same row moving rightward.
- `j + 2 < cols` — boundary check: ensures `j+2` doesn't go past the last column
- `matrix[i][j+1]` — same row, one column right
- `matrix[i][j+2]` — same row, two columns right

```
[i,j]  [i,j+1]  [i,j+2]   ← same row, moving right
```

---

### Step 6 — Check diagonal down-right (↘)

```js
if (i + 2 < rows && j + 2 < cols &&
    matrix[i][j] === matrix[i + 1][j + 1] &&
    matrix[i][j] === matrix[i + 2][j + 2]) {
  return [matrix[i][j], [i, j], [i + 1, j + 1], [i + 2, j + 2]];
}
```

Checks cells going diagonally toward the bottom-right corner.
- Needs **two** boundary checks: row must have 2 more rows below, column must have 2 more columns to the right
- Each step increases both `i` and `j` by 1

```
[i,  j  ]
  [i+1,j+1]
      [i+2,j+2]
```

---

### Step 7 — Check diagonal down-left (↙)

```js
if (i + 2 < rows && j - 2 >= 0 &&
    matrix[i][j] === matrix[i + 1][j - 1] &&
    matrix[i][j] === matrix[i + 2][j - 2]) {
  return [matrix[i][j], [i, j], [i + 1, j - 1], [i + 2, j - 2]];
}
```

Checks cells going diagonally toward the bottom-left corner.
- Row increases by 1 each step (moving down)
- Column **decreases** by 1 each step (moving left)
- Boundary check is `j - 2 >= 0` — can't go left of column 0

```
      [i,  j  ]
   [i+1,j-1]
[i+2,j-2]
```

---

### Step 8 — Return no winner

```js
return [];
```

If the nested loops complete without finding three in a row anywhere, no player has won yet and an empty array is returned.

---

## 6. Boundary Checks Explained

Before checking cells at offsets `+1` and `+2`, the code must verify those cells actually exist. Going out of bounds would give `undefined`, which would wrongly fail the comparison.

```js
// Vertical: need 2 more rows below current row
i + 2 < rows       // e.g. if rows=4 and i=2: 2+2=4, 4 < 4 is FALSE ✅ (won't go out of bounds)

// Horizontal: need 2 more cols to the right
j + 2 < cols       // same logic for columns

// Down-right diagonal: need both
i + 2 < rows && j + 2 < cols

// Down-left diagonal: need 2 more rows AND 2 cols to the LEFT
i + 2 < rows && j - 2 >= 0   // j-2 must not go below 0
```

A concrete example — if you're at `[i=3, j=0]` in a 4-row grid:
- `i + 2 < rows` → `3 + 2 = 5 < 4` → **false** → vertical check skipped ✅

Without this guard, `matrix[5]` would be `undefined` and `matrix[5][0]` would throw a TypeError.

---

## 7. Worked Examples

### Example 1 — Horizontal win

```
Grid:
row0 [ "",  "",  "",  "" ]
row1 [ "",  "",  "",  "" ]
row2 [ "",  "Y", "",  "" ]
row3 [ "Y", "R", "R", "R" ]

Scan reaches [3,1] = "R"
→ Vertical check:   i+2=5, 5 < 4 is false → skip
→ Horizontal check: j+2=3, 3 < 4 is true
  matrix[3][1]==="R", matrix[3][2]==="R", matrix[3][3]==="R" → ALL MATCH ✅
→ return ["R", [3,1], [3,2], [3,3]]
```

---

### Example 2 — Vertical win

```
Grid:
row0 [ "",  "",  "",  "" ]
row1 [ "",  "Y", "Y", "" ]
row2 [ "",  "Y", "R", "R"]
row3 [ "",  "Y", "R", "R"]

Scan reaches [1,1] = "Y"
→ Vertical check: i+2=3, 3 < 4 is true
  matrix[1][1]==="Y", matrix[2][1]==="Y", matrix[3][1]==="Y" → ALL MATCH ✅
→ return ["Y", [1,1], [2,1], [3,1]]
```

---

### Example 3 — Diagonal down-left win (↙)

```
Grid:
row0 [ "",  "",  "Y", "R" ]
row1 [ "",  "Y", "R", "Y" ]
row2 [ "",  "R", "Y", "R" ]
row3 [ "",  "R", "Y", "R" ]

Scan reaches [0,3] = "R"
→ Vertical:    i+2=2 < 4 ✅, but matrix[1][3]="Y" ≠ "R" → no match
→ Horizontal:  j+2=5, 5 < 4 is false → skip
→ Down-right:  j+2=5, 5 < 4 is false → skip
→ Down-left:   i+2=2 < 4 ✅, j-2=1 >= 0 ✅
  matrix[0][3]="R", matrix[1][2]="R", matrix[2][1]="R" → ALL MATCH ✅
→ return ["R", [0,3], [1,2], [2,1]]

Visualised:
         col0  col1  col2  col3
  row0  [  "",  "",  "Y",  "R" ]  ← start [0,3]
  row1  [  "",  "Y", "R",  "Y" ]  ← middle [1,2]
  row2  [  "",  "R", "Y",  "R" ]  ← end [2,1]
  row3  [  "",  "R", "Y",  "R" ]
```

---

### Example 4 — No winner

```
Grid:
[ "Y","R","R","Y" ]
[ "R","Y","Y","R" ]
[ "Y","R","R","Y" ]
[ "R","Y","Y","R" ]

Every row/column/diagonal alternates between R and Y.
No three consecutive cells ever match.
→ return []
```

---

## 8. Methods Used

| Method / Syntax | Where Used | What It Does |
|---|---|---|
| `matrix.length` | Measuring rows | Returns the number of elements in the outer array (= number of rows) |
| `matrix[0].length` | Measuring columns | Returns the number of elements in the first row (= number of columns) |
| `matrix[i][j]` | Accessing a cell | Double bracket notation accesses a specific row then column |
| `!== ""` | Skipping empty cells | Strict inequality — only proceeds if the cell contains a piece |
| `===` | Comparing pieces | Strict equality — checks that two cells contain the same player symbol |
| `i + 2 < rows` | Boundary check (rows) | Prevents accessing a row index that doesn't exist |
| `j - 2 >= 0` | Boundary check (cols left) | Prevents accessing a negative column index |
| `return [...]` | Early return | Exits the function immediately when a winner is found |
| `return []` | No winner | Returns an empty array after all cells are scanned with no match |

---

## 9. Full Annotated Code

```js
function connectThree(matrix) {

  const rows = matrix.length;       // total number of rows
  const cols = matrix[0].length;    // total number of columns

  for (let i = 0; i < rows; i++) {        // scan top → bottom
    for (let j = 0; j < cols; j++) {      // scan left → right

      if (matrix[i][j] !== "") {          // skip empty cells

        // ── Check VERTICAL ↓ ──────────────────────────────────────
        // Need 2 more rows below: i+2 must be a valid row index
        if (i + 2 < rows &&
            matrix[i][j] === matrix[i + 1][j] &&
            matrix[i][j] === matrix[i + 2][j]) {
          return [matrix[i][j], [i, j], [i + 1, j], [i + 2, j]];
        }

        // ── Check HORIZONTAL → ────────────────────────────────────
        // Need 2 more cols to the right: j+2 must be a valid col index
        if (j + 2 < cols &&
            matrix[i][j] === matrix[i][j + 1] &&
            matrix[i][j] === matrix[i][j + 2]) {
          return [matrix[i][j], [i, j], [i, j + 1], [i, j + 2]];
        }

        // ── Check DIAGONAL DOWN-RIGHT ↘ ───────────────────────────
        // Need 2 more rows AND 2 more cols to the right
        if (i + 2 < rows && j + 2 < cols &&
            matrix[i][j] === matrix[i + 1][j + 1] &&
            matrix[i][j] === matrix[i + 2][j + 2]) {
          return [matrix[i][j], [i, j], [i + 1, j + 1], [i + 2, j + 2]];
        }

        // ── Check DIAGONAL DOWN-LEFT ↙ ────────────────────────────
        // Need 2 more rows below AND 2 cols to the LEFT (j-2 >= 0)
        if (i + 2 < rows && j - 2 >= 0 &&
            matrix[i][j] === matrix[i + 1][j - 1] &&
            matrix[i][j] === matrix[i + 2][j - 2]) {
          return [matrix[i][j], [i, j], [i + 1, j - 1], [i + 2, j - 2]];
        }

      }
    }
  }

  return []; // no winner found after scanning entire grid
}
```
