#Authored by Kevin S  and Ransom V 
# Created on 10/13/15
#
# A program that sets up a 4 x 4 boggle board from a string of 16 characters
# and finds all legitimate boggle words on board as defined in a dictionary file
# which is also supplied as a command line argument.


__author__ = "Kevin and Ransom, Michal Young, PDX Code Guild 2015 Class"

"""
Boggle solver finds words on a boggle board.
Credits: Michal Young, Thunder Shiviah, Cole and Patrick
Usage:  python3 boggler.py  "board" dict.txt
    where "board" is 16 characters of board, in left-to-right reading order
    and dict.txt can be any file containing a list of words in alphabetical order
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
        none (but expect two command line arguments - a string of 16 alph characters
        and a dictionary file)

    Returns:
        Nothing, but prints found words in alphabetical
        order, without duplicates, one word per line.  Each word is scored and the sum of all words is printed
    """

    dict_file, board_text = getargs()
    game_dict.read(dict_file)
    board = BoggleBoard(board_text)

    rows = 4
    cols = 4
    results = []
    for row in range(rows):
        for col in range(cols):
            find_words(board, row, col, board.get_char(row, col), results)

    set_ = set(results)
    fin_list = list(set_)
    fin_list.sort()
    final = score(fin_list)
    print("Total score:", final)


def getargs():
    """
    Get command line arguments.
    Args:
       none (but expects two arguments on program command line)

    Returns:
       pair (dictfile, text)
         where dictfile is a file containing dictionary words (the words boggler will look for)
         and text is 16 characters of text that form a board
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


def find_words(board, row, col, prefix, results):
    """Find all words starting with prefix that
    can be completed from row,col of board.

    Args:
        row:  int - row of position to continue from (need not be on board)
        col:  int - col of position to continue from (need not be on board)
        prefix: string - looking for words that start with this prefix
        results: list of strings containing words found on board

    Returns: nothing
        (side effect is filling results list)

    Effects:
        inserts found words (not necessarily unique) into results
    """

    if prefix is None:
        return "You must start with a prefix!"

    if board.available(row, col) is False:
        return "Tile not available!"

    else:
        board.mark_taken(row, col)

        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if board.available(i, j) is True:
                    prefix += board.get_char(i, j)
                    is_word = game_dict.search(prefix)
                    if is_word == 1:  # 1  - prefix is a word
                        results.append(prefix)
                        find_words(board, i, j, prefix, results)
                    elif is_word == 2:  # 2 - prefix is a prefix but not also a word
                        find_words(board, i, j, prefix, results)  
                    if board.get_char(i, j) == 'qu':  #  If tile is qu, back up 2 spaces
                        prefix = prefix[:-2]
                    else:
                        prefix = prefix[:-1]
        board.unmark_taken(row, col)


def score(word):
    """
    Compute the Boggle score for a word, based on the scoring table
    at http://en.wikipedia.org/wiki/Boggle.
    Words < 3 letters are not awarded any points.
    Words 3-4 letters long are awarded 1 point.
    Words 5 letters long are awarded 2 points.
    Words 6 letters long are awarded 3 points.
    Words 7 letters long are awarded 5 points.
    Words greater than 8 letters long are worth 11 points.

    Args - word - a set (sorted) of found words 

    Returns - An int containing sum of all found words

    Effects - Prints the found words and the score of each word
     """
    score_dct = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5}
    final_score = []
    for item in word:
        if len(item) >= 8:
            final_score.append(11)
        else:
            final_score.append(score_dct[len(item)])
    for i in range(len(final_score)):
        print (word[i], final_score[i])

    final_score = sum(final_score)
    return(final_score)

    """Assert Tests"""
    assert score(["alp", "alpha", "gal", "gamma", "hap", "lag", "lam",
        "mag", "max"]) == 11
    assert score(["redundant" == 11])

####
# Run if invoked from command line
####

if __name__ == "__main__":
    main()
    input("Press enter to end")
