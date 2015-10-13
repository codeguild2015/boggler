"""
Boggle solver finds words on a boggle board. 
Authors:  #FIXME
Credits: #FIXME 
Usage:  python3 boggler.py  "board" dict.txt
    where "board" is 16 characters of board, in left-to-right reading order
    and dict.txt can be any file containing a list of words in alphabetical order
    
"""

from boggle_board import BoggleBoard   
import argparse   # Command line processing
import game_dict  # Dictionary of legal game words
from collections import OrderedDict

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


    board = BoggleBoard(board_text)
    prefix = "" 
    #prefix = board.get_char(0, 0)
    results = [ ] 
    #game_dict = game_dict.read( dict_file ) #KS: added this to initialize
    game_dict.read( dict_file )

    for i in range(4):
        for j in range(4):
            print("calling find_words from main with row, col - ", i, j)
            # board.unmark_all()
            find_words(board, i, j, prefix, results)
    print("results at end of main:  ", results)
    uniq_res = rem_dups(results)
    print("Unique results at end of main are:  ", uniq_res)
    score(uniq_res)


    # FIXME: 
    #    Search for words starting from each position on the board. 
    #    Remove duplicates from results, and sort them alphabetically.
    #        (Write a separate function for dedu
    #    Print each word and its score
    #    Print total score

def rem_dups(results):
    return list(OrderedDict.fromkeys(results))


def score(results):
    """
    Compute the Boggle score for a word, based on the scoring table
    at http://en.wikipedia.org/wiki/Boggle. 
    #FIXME: finish writing this docstring
     """
    print("In score function")
    score_dct = {3 : 1, 4: 1, 5 : 2, 6 : 3, 7 : 5,}
    final_score = []
    for word in results:
        print("Word in score is {}.  Length of word is {} .".format(word, len(word)))
        if len(word) >= 8:
            final_score.append(11)
        else:
            final_score.append(score_dct[len(word)])
    for i in range(len(final_score)):
        print (results[i], final_score[i])
            
    final_score = sum(final_score)
    print("final score is: ", final_score)
    
    # return(final_score)
                          
#    assert score(["alp", "alpha", "gal", "gamma", "hap", "lag", "lam", 
#        "mag", "max"]) = 11 



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
    if len(text) != 16 :
        print("Board text must be exactly 16 alphabetic characters")
        exit(1)
    return dictfile, text


def find_words(board, row, col, prefix, results):
    """Find all words starting with prefix that
    can be completed from row,col of board.
    Args:
        row:  row of position to continue from (need not be on board)
        col:  col of position to continue from (need not be on board)
        prefix: A string.  looking for words that start with this prefix
        results: list of words found so far
    Returns: nothing
        (side effect is filling results list)
    Effects:
        inserts found words (not necessarily unique) into results
    """

    """Extracting content
    for item in BoggleBoard.content:
        row = BoggleBoard.content[item]
        for column in row: 
            col = row[column]
    """

    board.mark_taken(row, col)

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if board.available(i, j) is True:
                print('get_char looking for location: ', row + i, col + j)
                prefix += board.get_char(i, j)
                is_word = game_dict.search(prefix)
                if is_word == 1:  # prefix is a word
                    results.append(prefix)
                    find_words(board, i, j, prefix, results)
                elif is_word == 2:  # prefix is a prefix but not also a word
                    find_words(board, i, j, prefix, results)  # need to fix args
                if board.get_char(i, j) == 'qu':
                    prefix = prefix[:-2]
                else:
                    prefix = prefix[:-1]
    board.unmark_taken(row, col)
    print("Reults at end of nested for: ", results)
    return results


def find_words_1(board, row, col, prefix, results):
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

    """Extracting content
    for item in BoggleBoard.content:
        row = BoggleBoard.content[item]
        for column in row: 
            col = row[column]
    """
    print("At start of find_words, row col are: ", row, col)
    try:
        is_word
    except NameError:
        is_word = ""

    cur_tile = ""
    is_word = game_dict.search(row, col)
    if board.available(row, col) is False or is_word == 0:
        print("entered find_words with row_col marked taken and/or is_word is 0 so returning to main", board.available(row, col), is_word)
        return None
    else:
        cur_tile = board.get_char(row, col)
        board.mark_taken(row, col)
        #results.append(cur_tile)
        if len(prefix) == 0:  # Only want to add current char to string if the prefix is empty.
            prefix = cur_tile

    for i in range(-1, 2):
        for j in range(-1, 2):
            if board.available(row + i, col + j) is True:
                print('get_char looking for location: ', row + i, col + j)
                cur_tile = board.get_char(row + i, col + j)
                prefix += cur_tile
                board.mark_taken(row + i , col + j)
                is_word = game_dict.search(prefix)
                print("value of is_word is *{}*.  prefix is *{}* and curr_char are: *{}*".format(is_word, prefix, cur_tile))
                if is_word == 2:  # prefix is a prefix but not also a word
                    board.unmark_taken(row + i , col + j) 
                    find_words(board, row + i, col + j, prefix, results) # need to fix args
                elif is_word == 1:  # prefix is a word
                    results.append(prefix)
                    board.unmark_taken(row + i , col + j)
                    find_words(board, row + i, col + j, prefix, results)
                else:  # prefix isn't in dict (is_word is 0)
                    print("prefix isn't a word so returning to ?")
                    break 
            else:
                continue
            break
    print("Out of nexted for.  is_word is: ", is_word)
    board.unmark_taken(row, col)
    print("Reults at end of nested for: ", results)
    return results

    

####
# Run if invoked from command line
####

if __name__ == "__main__":
    main()
    input("Press enter to end")