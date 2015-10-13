"""
Boggle solver finds words on a boggle board. 
Authors:  Dana & Patrick 
Credits: Not sure.  Some guy who wrote most of this code.

Usage:  python3 boggler.py  "board" dict.txt
    where "board" is 16 characters of board, in left-to-right reading order
    and dict.txt can be any file containing a list of words in alphabetical order    
"""

from boggle_board import BoggleBoard   
import argparse   # Command line processing
import game_dict  # Dictionary of legal game words
results = set()



def main():
    """Main program: Find all words of length 3 or greater on a boggle 
    board. 
    
    Parameters
    ---------
    Input:
    None
    pulls two arguments from the command line:
        "board" is 16 characters of board, in left-to-right reading order
        dict.txt is a file containing a list of words in alphabetical order
    
    Output:
    None 
        but prints found words in alphabetical order, without duplicates, 
        one word per line)"""

    
    global word_dict
    dict_file, board_text = getargs() # pulls args from command line
    word_dict = game_dict.read(dict_file)
    board = BoggleBoard(board_text)


    # Creates range to hit all possible x values on board.
    for x in range(board.board_height): 
        # Creates range to hit all possible y values on board.
        for y in range(board.board_width): 
            # runs recursive search beginning from each tile on the board.
            results.update(find_words(board, x, y, board.get_char(x,y)))
    final_list = score_list(results)
    total_score = 0
    for x, y in sorted(final_list): # Prints each word with associated score.
        print("{} {}".format(x,y))
        total_score += y
    print("Total score:", total_score)


def getargs():
    """
    Get command line arguments.
    Args:
        none (but expects two arguments on program command line)
    Returns:
        pair (dictfile, text)
            dictfile is a file containing dictionary words 
            text is 16 characters of text that form a board
    Effects:
        also prints meaningful error messages when the command line does 
            not have the right arguments
   """
    parser = argparse.ArgumentParser(description="Find boggle words")
    parser.add_argument('board', type=str, help="A 16 character string\
        to represent 4 rows of 4 letters. Q represents QU.")
    parser.add_argument('dict', type=argparse.FileType('r'),
        help="A text file containing dictionary words, one word per line.")
    args = parser.parse_args()  # Gets args from command line and validates them.
    text = args.board
    dictfile = args.dict
    if int(len(text)**.5) != (len(text)**.5): # Tests if board is square.
        print("Board text must result in a square board.  Please enter 4, 9, 16",
        "25, 36, etc. alphabetic characters,")
        exit(1)
    return dictfile, text

        
def find_words(board, row, col, str1):
    """Find all words starting with string that can be completed from 
        row,col of board. 
    
    Parameters
    ---------
    Input:
    row: row of position to continue from (need not be on board)
    col: col of position to continue from (need not be on board)
    str1: looking for words that start with this string
    
    
    Output:
    results: set
    A set of all unique words found on the boggle board  
    """
    
    # A list of relative positions of any cell in a square grid.
    neighbors = [
        (-1, -1), (-1,  0), (-1,  1), 
        ( 0,  1),           ( 1,  1), 
        ( 1,  0), ( 1, -1), ( 0, -1)
    ]

    board.mark_taken(row, col) # marks the currently occupied square as taken.
    for x, y, in neighbors:
        x += row
        y += col
        if board.available(x, y): 
            str1 += board.get_char(x, y) # builds the string to be searched.
            if game_dict.search(str1, word_dict) == 1:
                results.add(str1) 
                find_words(board, x, y, str1) # a word can also be a prefix.
            elif game_dict.search(str1, word_dict) == 2:
                find_words(board, x, y, str1)
            # subtracting from the string when moving away from a tile.
            # "q" char in boggle is always represented as "qu"
            if board.get_char(x, y) == 'qu': 
                str1 = str1[:-2]
            else:
                str1 = str1[:-1]

    board.unmark_taken(row, col) # unmarks a square before leaving the square.
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
    
    
def score(word):
   """
   Calculates the score of a word using the rules for Boggle.

   Parameters
   ---------
   Input:
   word: String
   A word to be scored.

   Output:
   int:
   The score value of the word.
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
   Scores a list of words according the rules of Boggle.

   This function takes a list of words and caclulates the score for each word.  
   Each word and score combination is stored as a tuple in a new list which is
   returned.

   Parameters
   ---------
   Input:
   score_lst: List
   A list of words and scores stored as tuples.
   

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
