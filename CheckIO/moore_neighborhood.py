def count_neighbours(grid, row, col):
    """
    Input: Three arguments. A grid as a tuple of tuples with integers (1/0),
           a row number and column number for a cell as integers.
    Output: How many neighbouring cells have chips as an integer. 
    """

    # using the hint: form a list of neighbor rules
    NEIGHBORS = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))

    # create a list of all cell positions in the provided grid
    boundary = [(r,c) for r in range(len(grid)) for c in range(len(grid))]

    # build a list of cells to count
    moore_neighbors = [(r+row, c+col) for r,c in NEIGHBORS]

    # count the cells that are within the bounds of the grid
    return sum([grid[r][c] for (r,c) in moore_neighbors if (r,c) in boundary])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
