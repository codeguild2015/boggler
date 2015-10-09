"""
Boggle solver finds words on a boggle board.
Authors:  Connor and Cole
Credits:  Whoever it was that wrote the original framing of this.
          Connor and Cole just filled in the blanks for main and
          find_words (as well as read and search in the game_dict)

Usage:  python3 boggler.py  "board" dict.txt
    where "board" is 16 characters of board, in left-to-right reading order
    and dict.txt can be any file containing a list of words in alphabetical
    order
"""

from boggle_board import BoggleBoard
import argparse   # Command line processing
import game_dict  # Dictionary of legal game words


def main():
    """
    Main program:
    Find all words of length 3 or greater on a boggle
    board.
    Args:
        none (but expect two arguments on command line)
    Returns:
        Nothing (but prints found words in alphabetical
        order, without duplicates, one word per line)
    """
    dict_file, board_text = getargs()
    game_dict.read(dict_file)
    board = BoggleBoard(board_text)
    for x in range(4):
        for y in range(4):
            find_words(board, x, y, board.get_char(x, y))
    results = board.results
    set_results = set(results)
    results = list(set_results)
    results.sort()
    final = [(item, score(item)) for item in results]
    if final:
        for elem in final:
            print(elem[0], elem[1])
        sum_list = [elem[1] for elem in final]
        print('Total score: ', sum(sum_list))
    else:
        print('None')


def getargs():
    """
    Get command line arguments.
    Args:
       none (but expects two arguments on program command line)
    Returns:
       pair (dictfile, text)
         where dictfile is a file containing dictionary words (the words boggler will look for)
         and   text is 16 characters of text that form a board
    Effects:
       also prints meaningful error messages when the command line does not have the right arguments
   """
    parser = argparse.ArgumentParser(description="Find boggle words")
    parser.add_argument('board', type=str, help="A 16 character string to represent 4 rows of 4 letters. Q represents QU.")
    parser.add_argument('dict', type=argparse.FileType('r'),
                        help="A text file containing dictionary words, one word per line.")
    args = parser.parse_args()  # will get arguments from command line and validate them
    text = args.board
    dictfile = args.dict
    if len(text) != 16:
        print("Board text must be exactly 16 alphabetic characters")
        exit(1)
    return dictfile, text


def find_words(board, row, col, prefix):
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

    board.mark_taken(row, col)
    for x in range(row-1, row+2):
        for y in range(col-1, col+2):
            if board.available(x, y):
                prefix += board.get_char(x, y)
                if game_dict.search(prefix) == 1:
                    board.results.append(prefix)
                    find_words(board, x, y, prefix)
                elif game_dict.search(prefix) == 2:
                    find_words(board, x, y, prefix)
                if board.get_char(x, y) == 'qu':
                    prefix = prefix[:-2]
                else:
                    prefix = prefix[:-1]
    board.unmark_taken(row, col)
    return


def score(word):
    """
    Compute the Boggle score for a word, based on the scoring table
    at http://en.wikipedia.org/wiki/Boggle.
    Longer the word, more the points.
    3, 4 long gives 1 point
    5 gives 2
    6 gives 3
    7 gives 5
    8+ gives 11
    """
    length = len(word)
    if length <= 4:
        return 1
    elif length == 5:
        return 2
    elif length == 6:
        return 3
    elif length == 7:
        return 5
    else:
        return 11


####
# Run if invoked from command line
####

if __name__ == "__main__":
    assert score('act') == 1
    assert score('ecclesiastical') == 11
    assert score('please') == 3
    main()
    input("Press enter to end")
