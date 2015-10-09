import time
results = []

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
    game_dict.read( dict_file )
    board = BoggleBoard(board_text)
    results = [ ]

    for x in range(4):
        for y in range(4):
            results = find_words(board, x, y, board.get_char(x,y))
    res_set = set(results)
    final_list = score_list(res_set)
    total = 0
    for x, y in sorted(final_list):
        print("{}: {}".format(x,y))
        total += y
    print("Total: ", total)


    
   





    # FIXME: 
    #    Search for words starting from each position on the board. 
    #    Remove duplicates from results, and sort the list alphabetically.
    #        (Write a separate function for deduplication)
    #    Print each word and its score
    #    Print total score


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
    if len(text) != 16 :
        print("Board text must be exactly 16 alphabetic characters")
        exit(1)
    return dictfile, text


        
def find_words(board, row, col, str1):
    global results
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
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
    for x, y, in neighbors:
        x += row
        y += col
        if board.available(x, y):
            str1 += board.get_char(x, y)
            if game_dict.search(str1) == 1:
                results.append(str1)
                find_words(board, x, y, str1)
            elif game_dict.search(str1) == 2:
                find_words(board, x, y, str1)
            if board.get_char(x, y) == 'qu':
                str1 = str1[:-2]
            else:
                str1 = str1[:-1]
    board.unmark_taken(row, col)
    return results
            

	# FIXME: one base case is that position row,col is not
	#    available (could be off the board, could be currently
	#    in use).  board.py can check that
	# FIXME:  For the remaining cases, where the tile at row,col 
	#    is available, we need to consider the new prefix that 
	#    includes the letter on this tile
	# FIXME:  Another base case is that no word can start with 
	#    the current prefix.  No use searching further on that path.
	# FIXME:  If the current position is a complete word, it is NOT 
	#    a base case, because it might also be part of a longer word. 
	#    We save the word we found into the global results list, and
	#    continue with the recursive case. 
	# FIXME: The recursive case is when the current prefix (including
	#    the tile at row,col) is a possible prefix of a word.  We 
	#    must mark it as currently in use, then search in all 8 directions
	#    around it, and finally mark it as no longer in use. See board.py
	#    for how to mark and unmark tiles, and how to get the text
	#    on the current tile.     
    return
    
    
    
def score(word):
   """
   Takes a string of words produced by running res_set.

   Parameters
   ---------
   Input:
   word: String
   Word

   Output:
   int:
   The score value of a word.
   """

   line_word = len(word)
   if line_word == 3 or line_word == 4:
       return 1
   if line_word == 5:
       return 2
   if line_word == 6:
       return 3
   if line_word == 7:
       return 5
   if line_word >= 8:
       return 11

assert score("car") == 1
assert score("this") == 1
assert score("brady") == 2
assert score("dragon") == 3
assert score("fjibhrd") == 5
assert score("hjsihfyd") == 11
assert score("wfiwfjiwjsfjkejfiwjijefijie") == 11

def score_list(lst):
   """
   Takes a list of words produced by running res_set.

   Parameters
   ---------
   Input:
   list: String
   Word

   Output:
   int:
   The score value of a word.
   """
   score_lst = []
   for elem in lst:
       score_lst.append((elem, score(elem)))
   return score_lst

####
# Run if invoked from command line
####

if __name__ == "__main__":
    main()
    input("Press enter to end")

