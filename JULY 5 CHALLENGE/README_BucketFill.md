# Bucket Fill — Code Explained

> Given a 2D grid, a starting cell, and a new value — replace the starting cell and all connected cells of the same value with the new value. Like the paint bucket tool in image editors.

---

## Table of Contents
1. [The Problem in Plain English](#1-the-problem-in-plain-english)
2. [The Real-World Analogy](#2-the-real-world-analogy)
3. [Key Concepts Before the Code](#3-key-concepts-before-the-code)
4. [Step-by-Step Code Breakdown](#4-step-by-step-code-breakdown)
5. [How the Queue Spreads the Fill](#5-how-the-queue-spreads-the-fill)
6. [Why Each Guard Condition Is Needed](#6-why-each-guard-condition-is-needed)
7. [Worked Examples](#7-worked-examples)
8. [Methods Used](#8-methods-used)
9. [Full Annotated Code](#9-full-annotated-code)

---

## 1. The Problem in Plain English

You have a 2D grid of coloured cells. Given:
- A **starting position** `[row, col]`
- A **new value** (colour) to fill with

Replace the cell at the starting position and every cell connected to it (horizontally or vertically) that shares the same original value.

```
Grid:            Start: [0,1] = "G"    After filling "G" → "B":

R  G             R  B
R  G             R  B
```

Both `G` cells are connected vertically, so both get filled. The `R` cells are a different value — they are left alone.

---

## 2. The Real-World Analogy

This is exactly the **paint bucket tool** in any image editor (MS Paint, Photoshop, etc.). When you click on a region with the bucket tool:

1. It reads the colour you clicked
2. It fills that cell with your chosen colour
3. It spreads to every neighbouring cell of the same original colour
4. It stops at boundaries where the colour changes

The algorithm is called **Breadth-First Search (BFS)** — it explores the grid outward from the starting point one layer at a time, like ripples spreading from a stone dropped in water.

---

## 3. Key Concepts Before the Code

### The Grid

```
grid[row][col]
      ↑    ↑
      │    └── column: left → right (index 0, 1, 2...)
      └──────── row:    top → bottom (index 0, 1, 2...)
```

```
         col 0   col 1   col 2
row 0  [  "Y",   "G",    "G"  ]
row 1  [  "Y",   "Y",    "Y"  ]
row 2  [  "B",   "Y",    "R"  ]
```

So `grid[1][2]` is the cell at row 1, column 2 → `"Y"`.

### The Queue

A queue is a list where items are added at the back and removed from the front — **First In, First Out (FIFO)**, like a queue of people. It is used here to keep track of which cells still need to be visited. Each item in the queue is a `[row, col]` coordinate pair.

### The Visited Set

A `Set` is used to remember which cells have already been filled. Without it, the algorithm could visit the same cell multiple times and loop forever.

### The Four Neighbours

From any cell `[row, col]`, the four adjacent cells are:

```
         [row-1, col]    ← above
[row, col-1]  ●  [row, col+1]
         [row+1, col]    ← below
```

Diagonals are **not** connected.

---

## 4. Step-by-Step Code Breakdown

### Step 1 — Capture the starting value

```js
const startValue = grid[row][col];
```

Read and store the value at the starting cell **before** anything is changed. Every cell that gets filled must match this original value. If you tried to read it mid-fill, it would already have been replaced with `newValue`.

---

### Step 2 — Initialise the queue and visited set

```js
const visited = new Set();
const queue = [[row, col]];
```

The queue begins with just the starting cell. The visited set starts empty. As the algorithm runs, cells are pulled from the front of the queue, processed, marked visited, and their neighbours added to the back of the queue.

---

### Step 3 — The main BFS loop

```js
while (queue.length) {
  const [row, col] = queue.shift();
  ...
}
```

`queue.length` is truthy (non-zero) as long as there are cells left to process. The loop continues until the queue is completely empty — meaning every reachable connected cell has been visited.

`queue.shift()` removes and returns the **first** item from the queue (FIFO order). The `[row, col]` destructuring unpacks the coordinate pair directly.

---

### Step 4 — Guard conditions: skip invalid cells

```js
if (
  row < 0 ||
  row >= grid.length ||
  col < 0 ||
  col >= grid[0].length ||
  grid[row][col] !== startValue ||
  visited.has(`${row},${col}`)
) {
  continue;
}
```

Six conditions are checked. If **any** is true, skip this cell and move to the next item in the queue:

| Condition | Meaning |
|---|---|
| `row < 0` | Cell is above the top edge |
| `row >= grid.length` | Cell is below the bottom edge |
| `col < 0` | Cell is left of the left edge |
| `col >= grid[0].length` | Cell is right of the right edge |
| `grid[row][col] !== startValue` | Cell is a different colour — don't fill it |
| `visited.has(...)` | Cell was already filled — don't process again |

These guards are what give the fill its boundaries.

---

### Step 5 — Fill the cell and mark it visited

```js
visited.add(`${row},${col}`);
grid[row][col] = newValue;
```

The cell passed all six guards — it is within bounds, has the right value, and hasn't been visited yet. Mark it visited and replace its value with `newValue`.

The visited key is the string `"row,col"` (e.g. `"1,2"`). A `Set` of strings is used instead of a 2D boolean array for simplicity.

---

### Step 6 — Add the four neighbours to the queue

```js
queue.push([row - 1, col]); // above
queue.push([row + 1, col]); // below
queue.push([row, col - 1]); // left
queue.push([row, col + 1]); // right
```

All four adjacent cells are added to the **back** of the queue to be processed later. Some will be out of bounds or the wrong colour — the guard conditions in Step 4 will handle that when they are dequeued.

---

### Step 7 — Return the modified grid

```js
return grid;
```

The original grid is modified in place. Once the queue is empty (all connected cells filled), return it.

---

## 5. How the Queue Spreads the Fill

Here is the queue state at every step for `bucketFill([["R","G"],["R","G"]], [0,1], "B")`:

```
Grid:
  R  G   ← starting at [0,1] = "G"
  R  G

Start value: "G" → "B"
Queue start: [ [0,1] ]

Step 1: dequeue [0,1]  → value="G" ✅ FILL → grid[0][1]="B"
        add neighbours: [-1,1] [1,1] [0,0] [0,2]
        Queue: [ [-1,1], [1,1], [0,0], [0,2] ]

Step 2: dequeue [-1,1] → OUT OF BOUNDS → skip
        Queue: [ [1,1], [0,0], [0,2] ]

Step 3: dequeue [1,1]  → value="G" ✅ FILL → grid[1][1]="B"
        add neighbours: [0,1] [2,1] [1,0] [1,2]
        Queue: [ [0,0], [0,2], [0,1], [2,1], [1,0], [1,2] ]

Step 4: dequeue [0,0]  → value="R" ≠ "G" → skip
Step 5: dequeue [0,2]  → OUT OF BOUNDS → skip
Step 6: dequeue [0,1]  → value="B" ≠ "G" (already filled) → skip
Step 7: dequeue [2,1]  → OUT OF BOUNDS → skip
Step 8: dequeue [1,0]  → value="R" ≠ "G" → skip
Step 9: dequeue [1,2]  → OUT OF BOUNDS → skip

Queue empty → done!

Final grid:
  R  B
  R  B
```

The queue works like a spreading wave. Each filled cell adds its neighbours, and the wave stops naturally when it hits boundaries or different-coloured cells.

---

## 6. Why Each Guard Condition Is Needed

### Without the bounds checks:
`queue.push([row - 1, col])` at row `0` would push `[-1, col]`. Then `grid[-1]` would be `undefined`, and `grid[-1][col]` would throw a `TypeError`.

### Without the value check:
The fill would spread to cells of any colour, replacing the entire grid.

### Without the visited check:
When `[0,1]` fills and pushes its neighbours, one of those neighbours might later push `[0,1]` again. Without the visited check, `[0,1]` would be processed a second time — and since it's now `newValue` (not `startValue`), it would be skipped by the value check. But in a grid where `newValue === startValue`, the algorithm would loop infinitely, revisiting and re-adding the same cells forever.

---

## 7. Worked Examples

### Example 1 — Simple 2×2 grid

```
Input:  [["R","G"],["R","G"]]  start: [0,1]="G"  fill: "B"

R  G        R  B
R  G   →    R  B

Both G cells are vertically connected → both filled.
R cells are a different value → untouched.
```

---

### Example 2 — L-shaped region

```
Input:  [["Y","G","G"],["Y","Y","Y"],["B","Y","R"]]  start: [1,2]="Y"  fill: "B"

Y  G  G        B  G  G
Y  Y  Y   →    B  B  B
B  Y  R        B  B  R

The Y region is connected in an L-shape.
The fill spreads from [1,2] → left to [1,1] → [1,0] → up to [0,0]
                                                      → down to [2,1]
G and R cells are different values → untouched.
The existing B at [2,0] happens to become B too, but was already B.
```

---

### Example 3 — Disconnected regions

```
Input:  [["O","O","P"],["P","O","O"],["P","P","O"]]  start: [2,0]="P"  fill: "R"

O  O  P        O  O  P
P  O  O   →    R  O  O
P  P  O        R  R  O

Only the P cells connected to [2,0] are filled.
The P at [0,2] is isolated — surrounded by O cells — so it is NOT filled.
```

---

### Example 4 — Winding path

```
Input:  [["T","T","R","T"],["R","T","R","T"],["R","T","R","T"],["T","T","T","T"]]
Start:  [0,3]="T"  fill: "Y"

T  T  R  T        Y  Y  R  Y
R  T  R  T   →    R  Y  R  Y
R  T  R  T        R  Y  R  Y
T  T  T  T        Y  Y  Y  Y

All T cells are connected through a winding path (R cells act as walls).
The fill snakes through the grid following every adjacent T.
```

---

## 8. Methods Used

| Method / Syntax | Where Used | What It Does |
|---|---|---|
| `new Set()` | Tracking visited cells | A collection of unique values; `has()` checks membership, `add()` inserts |
| `.has(key)` | Visited check | Returns `true` if the key exists in the Set |
| `.add(key)` | Marking visited | Adds the key to the Set (no-op if already present) |
| `queue.shift()` | Dequeuing | Removes and returns the **first** item from the array (FIFO) |
| `queue.push(item)` | Enqueuing | Adds an item to the **end** of the array |
| `[row, col]` destructuring | Unpacking coordinates | Extracts the two values from a `[row, col]` array in one line |
| Template literal `` `${row},${col}` `` | Visited key | Builds a unique string key for each cell position |
| `continue` | Skipping invalid cells | Jumps immediately to the next loop iteration |
| `while (queue.length)` | BFS loop | Runs as long as the queue is non-empty (length > 0 is truthy) |

---

## 9. Full Annotated Code

```js
function bucketFill(grid, [row, col], newValue) {

  const visited = new Set();         // tracks which cells have been filled
  const queue = [[row, col]];        // BFS queue, starts with the clicked cell
  const startValue = grid[row][col]; // remember the original colour to match against

  while (queue.length) {             // keep going until no cells left to process
    const [row, col] = queue.shift(); // take the next cell from the front

    // Skip this cell if any of these are true:
    if (
      row < 0 ||                          // above the grid
      row >= grid.length ||               // below the grid
      col < 0 ||                          // left of the grid
      col >= grid[0].length ||            // right of the grid
      grid[row][col] !== startValue ||    // different colour — boundary
      visited.has(`${row},${col}`)        // already processed
    ) {
      continue;
    }

    visited.add(`${row},${col}`);   // mark as visited
    grid[row][col] = newValue;      // fill the cell

    // Add all four neighbours to the queue for processing
    queue.push([row - 1, col]); // above
    queue.push([row + 1, col]); // below
    queue.push([row, col - 1]); // left
    queue.push([row, col + 1]); // right
  }

  return grid;
}
```
