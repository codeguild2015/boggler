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
    # FIXME: 
    #    Search for words starting from each position on the board. 
    #    Remove duplicates from results, and sort the alphabetically.
    #        (Write a separate function for dedu
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

    board.mark_taken(row, col)
        for x in range(row-1, row+2):
            for y in range(col-1, col+2):
                if board.available(x, y):
                    


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
    Compute the Boggle score for a word, based on the scoring table
    at http://en.wikipedia.org/wiki/Boggle. 
    #FIXME: finish writing this docstring
     """
	#FIXME  score the word correctly
    return 0



####
# Run if invoked from command line
####

if __name__ == "__main__":
    main()
    input("Press enter to end")

