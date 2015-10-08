def find_words(board, row, col, prefix, results):
    """Find all words starting with prefix that
    can be completed from row,col of board.
    Args:
        row:  row of position to continue from (need not be on board)
        col:  col of position to continue from (need not be on board)
        prefix: looking for words that start with this prefix
        results: list of words found so far
    Returns: nothing
        (side effect is filling results list)
    Effects:
        inserts found words (not necessarily unique) into results
    """
    
    cur_word = board[0][0]


    row_offset = [-1, 0, 1]
    column_offset = [-1, 0, 1]

    for i in row_offset:
        for j in column_offset:
            next_row = row + i
            next_col = col + j  
            if (next_row < 0 or next_col < 0) or (next_row > 1 or next_col > 1):
                print("row or column out of range.")
            else:
                print("tile is: ", board[next_row][next_col])

            """ try:
                #print("board is: ", board)
                print("next row and column are: ", next_row, next_col)
                print("next tile is: ", board[next_row][next_column])
            except:
                print("out of range", i, j)
            """

def main():
    table = [['c', 'a'],['s', 't']]
    find_words(table, 0, 0, 3, 4)

main()

#prefix = table[0]

#results = find_words(table, 0, 0, prefix)

#print(results)