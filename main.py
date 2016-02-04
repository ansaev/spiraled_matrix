

# args:
# matrix: list of list of items [["item_00", "item_01"],["item_10", "item_11"]]
# number of rows in matrix have to be equal of number of cells in each row
# number of rows in matrix + 1 have to be a multiply of
def spiraled_matrix_representative(matrix):
    n_rows = len(matrix)
    n_cells = len(matrix[0])
    assert n_rows > 0
    assert n_rows == n_cells
    assert n_rows % 2 == 1
    indexes_list = []
    cur_row = (n_rows - 1)/2
    cur_cell = cur_row
    line_length = 0
    # add center cell indexes
    indexes_list.append([cur_row, cur_cell])
    for line in xrange(n_rows*2-1):
        # for each line of spiral
        # increase line_length every 2 thimes but no longer than n_rows-1
        if line % 2 == 0 and line_length < n_rows - 1:
            line_length += 1

        # go to necessary direction depended by line number
        if line % 4 == 0:
            # go left
            for iteration in xrange(line_length):
                cur_cell -= 1
                indexes_list.append([cur_row, cur_cell])
        elif line % 4 == 1:
            # go up
            for iteration in xrange(line_length):
                cur_row -= 1
                indexes_list.append([cur_row, cur_cell])
        elif line % 4 == 2:
            # go right
            for iteration in xrange(line_length):
                cur_cell += 1
                indexes_list.append([cur_row, cur_cell])
        elif line % 4 == 3:
            # go down
            for iteration in xrange(line_length):
                cur_row += 1
                indexes_list.append([cur_row, cur_cell])

    return indexes_list
