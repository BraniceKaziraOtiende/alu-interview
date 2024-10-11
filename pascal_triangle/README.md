Pascal's Triangle
Description
This project implements a function that generates Pascal's Triangle up to a specified number of rows, n. Pascal's Triangle is a triangular array of integers, where each number is the sum of the two directly above it in the previous row.

Features:
Handles edge cases: Returns an empty list if n <= 0.
Dynamic creation: Builds the triangle row by row based on mathematical rules.
Efficient: Uses list operations to generate the triangle in an optimized manner.
Function Prototype
python
Copy code
def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        List of lists: Pascal's Triangle represented as a list of lists.
    """
Parameters:
n (int): The number of rows of Pascal's Triangle to generate. If n <= 0, the function returns an empty list.
Return:
A list of lists, where each inner list represents a row of Pascal's Triangle.
Example
For n = 5, the output will be:

python
Copy code
[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
Edge Case
If n = 0 or any negative number, the function returns an empty list [].

File Structure
bash
Copy code
pascal_triangle/
├── 0-pascal_triangle.py  # Contains the pascal_triangle function
└── README.md             # Project documentation
Author
Branice Kazira

