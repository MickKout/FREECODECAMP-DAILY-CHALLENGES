"""
Bucket Fill
Given a 2D grid, a starting position ([row, col]), and a new value, replace the value at the starting position and all connected cells of the same value with the new value.

Cells are connected if they are adjacent horizontally or vertically (not diagonally).
Return the updated grid.

Tests:
Waiting:1. bucket_fill([["R", "G"], ["R", "G"]], [0, 1], "B") should return [["R", "B"], ["R", "B"]].
Waiting:2. bucket_fill([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B") should return [["B", "G", "G"], ["B", "B", "B"], ["B", "B", "R"]].
Waiting:3. bucket_fill([["O", "O", "P"], ["P", "O", "O"], ["P", "P", "O"]], [2, 0], "R") should return [["O", "O", "P"], ["R", "O", "O"], ["R", "R", "O"]].
Waiting:4. bucket_fill([["T", "T", "R", "T"], ["R", "T", "R", "T"], ["R", "T", "R", "T"], ["T", "T", "T", "T"]], [0, 3], "Y") should return [["Y", "Y", "R", "Y"], ["R", "Y", "R", "Y"], ["R", "Y", "R", "Y"], ["Y", "Y", "Y", "Y"]].
Waiting:5. bucket_fill([["G", "B", "G", "B"], ["R", "B", "B", "G"], ["B", "G", "B", "R"], ["B", "G", "G", "B"]], [2, 2], "G") should return [["G", "G", "G", "B"], ["R", "G", "G", "G"], ["B", "G", "G", "R"], ["B", "G", "G", "B"]].
"""
def bucket_fill(grid, pos, new_value):

    visited = set()
    queue = [pos]
    start_value = grid[pos[0]][pos[1]]

    while queue:
        row, col = queue.pop(0)
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != start_value or f"{row},{col}" in visited:
            continue
        visited.add(f"{row},{col}")
        grid[row][col] = new_value
        
        queue.append((row - 1, col))
        queue.append((row + 1, col))
        queue.append((row, col - 1))
        queue.append((row, col + 1))

    return grid

print(bucket_fill([["R", "G"], ["R", "G"]], [0, 1], "B"))
print(bucket_fill([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B"))
print(bucket_fill([["O", "O", "P"], ["P", "O", "O"], ["P", "P", "O"]], [2, 0], "R"))
print(bucket_fill([["T", "T", "R", "T"], ["R", "T", "R", "T"], ["R", "T", "R", "T"], ["T", "T", "T", "T"]], [0, 3], "Y"))
print(bucket_fill([["G", "B", "G", "B"], ["R", "B", "B", "G"], ["B", "G", "B", "R"], ["B", "G", "G", "B"]], [2, 2], "G"))