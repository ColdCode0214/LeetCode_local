'''
A black and white image is composed of pixels and is represented as an (n*m) grid of cells.
Each pixel can have a value of 0 or 1, where 0 represents a white pixel and 1 represents a
black pixel.
The greyness of a cell (i,j) is affected by the pixel values in the ith row and the jth column.
More formally, the greyness of the cell (i,j) is the difference between the number of black
pixels in the ith row and the jth column and the number of white pixels in the ith row and the
jth column
Find the maximum greyness among all the cells of the grid
Note: The value of cell (i,j) is counted both in the ith row and in the jth column
'''
from typing import List

grid = ["1101", "0101", "1010"]

def oa1t7(grid: List[str]) -> int:
    ans = 0
    count_row_w, count_row_b, count_col_w, count_col_b = list(), list(), list(), list()
    r, c = len(grid), len(grid[0])
    for i in range(r):
        count_w, count_b = 0, 0
        for j in range(c):
            if grid[i][j] == '0':
                count_w += 1
            else:
                count_b += 1
        count_row_b.append(count_b)
        count_row_w.append(count_w)
    for j in range(c):
        count_w, count_b = 0, 0
        for i in range(r):
            if grid[i][j] == '0': count_w += 1
            else: count_b += 1
        count_col_b.append(count_b)
        count_col_w.append(count_w)
    for i in range(r):
        for j in range(c):
            sum_b = count_row_b[i] + count_col_b[j]
            sum_w = count_row_w[i] + count_col_w[j]
            if grid[i][j] == '1': sum_b -= 1
            else: sum_w -= 1
            grey = sum_b - sum_w
            ans = max(ans, grey)
    return ans

print(oa1t7(grid))

