# I found this very difficult and took a lot of help from chatGPT and YouTube but made sure to give it a good crack first!

grid = [
    "----#",
    "--##-",
    "-##--",
    "-----",
    "--#--"
]

# Define the function count_adjacent_mines that takes the grid as input.
# This function will return a new grid with each dash replaced by a digit indicating the number of adjacent mines.
def count_adjacent_mines(grid):

# Determine the number of rows and columns in the grid using len(grid) and len(grid[0]) respectively.
# This is necessary to iterate over each element in the grid.
# As grids are typically represented as 2D lists, it is assumed that all rows in the grid have the same length. 
# len(grid[0]) determines the number of columns in the grid, assuming the grid is rectangular with at least one row.
    rows = len(grid)
    cols = len(grid[0])

# Define the directions variable (a list of tuples) representing the eight possible directions to check for adjacent cells (up, down, left, right, and diagonals).
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
# The is_valid function is defined to check if a given row and column coordinate is within the bounds of the grid.
# It returns True if the coordinate is valid, and False otherwise.
    def is_valid(row, col):
        return 0 <= row < rows and 0 <= col < cols
    
    """The is_valid function is a helper function that checks whether a given row and column coordinate is valid within the grid. It is not strictly necessary.
    It takes the row and col parameters as inputs, representing the row and column indices of a cell.
    The function compares these indices with the number of rows and columns in the grid to determine if they fall within the valid range.
    The rows and cols variables are obtained from the dimensions of the grid using the len() function.
    The condition 0 <= row < rows checks if the row index is greater than or equal to 0 and less than the total number of rows in the grid. This ensures that the row index is within the valid range.
    Similarly, the condition 0 <= col < cols checks if the col index is greater than or equal to 0 and less than the total number of columns in the grid. This ensures that the column index is within the valid range.
    If both conditions (row and col indices being within valid ranges) are true, the function returns True, indicating that the given coordinate is valid.
    If any of the conditions is not met, the function returns False, indicating that the given coordinate is not valid."""

# The count_mines function takes a row and column coordinate as input and counts the number of adjacent mines.
# It iterates over each direction in the directions list, calculates the new row and column coordinates by adding the direction values to the current row and column, and checks if the new coordinates are valid and if the cell contains a mine ("#").
# If a mine is found, the count is updated.
    def count_mines(row, col):
        count = 0
        for dx, dy in directions:
            new_row = row + dx
            new_col = col + dy
            if is_valid(new_row, new_col) and grid[new_row][new_col] == "#":
                count += 1
        return count
    
# Create a new grid (new_grid) as a copy of the original grid by iterating over each row and converting it to a list.
    new_grid = [list(row) for row in grid]  # Create a copy of the grid
    
# Loop over each cell in the grid using two nested for loops. For each cell, if it contains a dash ("-"), we call the count_mines function to determine the number of adjacent mines. The result is then converted to a string and assigned to the corresponding cell in the new grid.
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "-":
                mines_count = count_mines(row, col)
                new_grid[row][col] = str(mines_count)

    """for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == "-":
                mines_count = count_mines(row_idx, col_idx)
                new_grid[row_idx][col_idx] = str(mines_count)
                
        In this updated version, the enumerate function is used in the nested for loop to iterate over the rows and columns of the grid while also obtaining the indices (row_idx and col_idx) and the values (row and cell) simultaneously.
        This allows for a more concise and readable code.
        The enumerate function is a built-in function in Python that allows you to iterate over a sequence (in this case, the grid) while also obtaining the index and value of each element in the sequence.
        In this code, we use enumerate to iterate over each row in the grid by using for row_idx, row in enumerate(grid).
        Here, row_idx represents the index of the row, and row represents the actual row content.
        By using enumerate in the outer loop, we can easily access the index of each row (row_idx) along with the row itself (row).
        This is useful because it allows us to know the row number and use it as an input to the count_mines function.
        Similarly, within the inner loop, we use enumerate to iterate over each cell in the row by using for col_idx, cell in enumerate(row).
        Here, col_idx represents the index of the column, and cell represents the value of the current cell.
        By using enumerate in the inner loop, we can easily access the index of each cell (col_idx) along with the cell value (cell).
        This is helpful because it allows us to know the column number and use it as an input to the count_mines function.
        With the help of enumerate, we can efficiently iterate over the rows and columns of the grid while simultaneously obtaining the row and column indices and the corresponding cell values.
        This simplifies the code and allows us to perform the necessary calculations, such as counting the adjacent mines for each cell."""
    
# Return the new grid with the digits indicating the number of adjacent mines.
    return new_grid

# Call the count_adjacent_mines function, passing the grid as an argument, and assign the result to the result variable.
result = count_adjacent_mines(grid)

# Iterate over each row in the result grid and print it.
# The "".join(row) joins the characters in each row into a single string for better readability.
for row in result:
    print("".join(row))
