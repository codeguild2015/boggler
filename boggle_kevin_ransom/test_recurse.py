directions = [(0,0), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1),(-1,-1)]
dictionary = ["car", "carrot", "race", "rare", "tea", "tear" ]

table = [['c', 'a', 'r' ], ['e', 'r', 'm'], ['o', 't', 'y']]

def recurse():
    candidates = []  

    for row_generate in range(3): # Update the max range to 4 for final
        x = row_generate
        for col_generate in range(3): # Update the max range to 4 for final
            y = col_generate
            print(x, y)

            strings_ = ""
            for tuple in range(9):
                row, col = directions[tuple]
                row_coord = x + row
                col_coord = y + col
                if row_coord >= 0 and col_coord >= 0 and row_coord <=2 and col_coord <= 2:
                    strings_ = strings_ + table[row_coord][col_coord]
            candidates.append(strings_)

    print(candidates)

recurse()