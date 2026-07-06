"""""
Connect 3
Given a matrix of strings representing pieces on a game grid, determine if any player has three in a row.

Each cell contains "R", "Y", or "" (empty string).
Three in a row means three consecutive non-empty cells of the same type horizontally, vertically, or diagonally.
Return:

A flat array with the winner and the coordinates of their three winning cells in the format: ["R", [0,2], [1,3], [2,4]]. Coordinates are returned top-to-bottom, then left-to-right.
An empty array if there is no winner.
Tests:
Waiting:1. connect_three([["", "", "", ""], ["", "", "", ""], ["", "Y", "", ""], ["Y", "R", "R", "R"]]) should return ["R", [3, 1], [3, 2], [3, 3]].
Waiting:2. connect_three([["", "", "", ""], ["", "Y", "Y", ""], ["", "Y", "R", "R"], ["", "Y", "R", "R"]]) should return ["Y", [1, 1], [2, 1], [3, 1]].
Waiting:3. connect_three([["", "", "Y", "R"], ["", "Y", "R", "Y"], ["", "R", "Y", "R"], ["", "R", "Y", "R"]]) should return ["R", [0, 3], [1, 2], [2, 1]].
Waiting:4. connect_three([["", "Y", "", ""], ["", "Y", "Y", ""], ["", "R", "R", "Y"], ["R", "R", "Y", "R"]]) should return ["Y", [0, 1], [1, 2], [2, 3]].
Waiting:5. connect_three([["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"], ["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"]]) should return [].
"""""

def connect_three(matrix):

   rows=len(matrix)
   cols=len(matrix[0])

   for i in range(rows):
      for j in range(cols):
         if matrix[i][j]!="":
            if i+2<rows and matrix[i][j]==matrix[i+1][j] and matrix[i][j]==matrix[i+2][j]:
               return [matrix[i][j],[i,j],[i+1,j],[i+2,j]]
            if j+2<cols and matrix[i][j]==matrix[i][j+1] and matrix[i][j]==matrix[i][j+2]:
               return [matrix[i][j],[i,j],[i,j+1],[i,j+2]]
            if i+2<rows and j+2<cols and matrix[i][j]==matrix[i+1][j+1] and matrix[i][j]==matrix[i+2][j+2]:
               return [matrix[i][j],[i,j],[i+1,j+1],[i+2,j+2]]
            if i+2<rows and j-2>=0 and matrix[i][j]==matrix[i+1][j-1] and matrix[i][j]==matrix[i+2][j-2]:
               return [matrix[i][j],[i,j],[i+1,j-1],[i+2,j-2]]
   return []

print(connect_three([["", "", "", ""], ["", "", "", ""], ["", "Y", "", ""], ["Y", "R", "R", "R"]]))
print(connect_three([["", "", "", ""], ["", "Y", "Y", ""], ["", "Y", "R", "R"], ["", "Y", "R", "R"]]))
print(connect_three([["", "", "Y", "R"], ["", "Y", "R", "Y"], ["", "R", "Y", "R"], ["", "R", "Y", "R"]]))
print(connect_three([["", "Y", "", ""], ["", "Y", "Y", ""], ["", "R", "R", "Y"], ["R", "R", "Y", "R"]]))
print(connect_three([["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"], ["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"]]))
