def find_words(board, row, col, prefix, results):
 

    print("At start of find_words, row and column are:", row, col) 
    cur_word = []
    # cur_word.append(board[row][col])

    if col == 2 and row < 2:           # got to the end of a row, go to the row, column 0
        row = row + 1
        col = 0
    if row == 2 and col == 2:         # got to end of table.  done.
        print("done with table")
        return "done"
    origin_char = board[row][col]
    print("origin_char at start of func is: ", origin_char)
    # print("At start of find_words, current tile is: ", board[row][col])
    cur_word.append(board[row][col])  # set first letter to tile at the root of the path
    next_row = row
    next_col = col    
    row_offset = [-1, 0, 1]
    column_offset = [-1, 0, 1]
    adj_tile_cnt = 0
    for i in row_offset:
        next_row = row + 1
        for j in column_offset:
            adj_tile_cnt += 1
            if adj_tile_cnt > 8:   # call find_words and repeat on next tile
                # next_row = row + 1
                # next_col = col + 1  
                find_words(board, row + 1, next_col, prefix, results)
            #next_row = row + 1
            next_col = col + 1  
            if (next_row < 0 or next_col < 0) or (next_row > 1 or next_col > 1):
                print("row or column out of range.")
            else:                  # We have a valid adj. tile
                if origin_char == board[next_row][next_col]:     # don't add the origin tile to cur_word
                    print('\n')
                else:
                    cur_word.append(board[next_row][next_col])

                print("next_tile is: ", board[next_row][next_col])
                print("cur_word is: ", cur_word)


def main():
    table = [['c', 'a'],['s', 't']]
    result = find_words(table, 0, 0, 3, 4)
    print(result)

main()

#prefix = table[0]

#results = find_words(table, 0, 0, prefix)

#print(results)