"""
Boggle solver finds words on a boggle board. 
Authors:  Mercy_and_Jaydn
​
Credits: Stackoverflow, Cole/Connor- credit for large portion of code. Trying to parse their code into ours created more problems that it fixed, and it ended up now being largely their code. The issue now being that, seeing how it works, 
I'm not sure how to rewrite it and make a new working code that is distinctly different. 
​
Usage:  python3 boggler.py  "board" dict.txt
    where "board" is 16 characters of board, in left-to-right reading order
    and dict.txt can be any file containing a list of words in alphabetical order
    
"""
​
from boggle_board import BoggleBoard   
import argparse   # Command line processing
import game_dict  # Dictionary of legal game words
import time
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
​
    for x in range(4): #recursion loop to run through all 16 tiles on the board. 
        for y in range(4):
            find_words(board,x,y,board.get_char(x,y,))
    results = board.results
    set_results = set(results)
    results =  list(set_results)
    results.sort()
    final = [(item, score(item)) for item in results] #Honestly not entirely sure how the following code works. 
    if final:
        for elem in final:
            print(elem[0], elem[1])
        sum_list = [elem[1] for elem in final]
        print('Total score: ', sum(sum_list))
    else:
        print("None")
    find_words(board,0,0,board.get_char(0,0))
    
​
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
​
​
        
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
    board.mark_taken(row,col)
    for x in range(row - 1, row + 2): #this and following line set search range to each tile around current tile, discounts tiles out of play 
        for y in range(col - 1, col + 2):
            if board.available(x,y):
                prefix += board.get_char(x,y)
                if game_dict.search(prefix) == 1:
                    board.results.append(prefix)
                    find_words(board,x,y,prefix)
                elif game_dict.search(prefix) == 2:
                    find_words(board,x,y,prefix)
                if board.get_char(x,y) == "qu": #makes sure that if program runs aross "qu" it backs up 2 letters but only 1 tiles in search function
                    prefix = prefix[:-2]
                else:
                    prefix = prefix[:-1]
    board.unmark_taken(row,col)
    return
​
​
​
​
​
​
def score(word):
    """
    Compute the Boggle score for a word, based on the scoring table
    at http://en.wikipedia.org/wiki/Boggle.
    Words are given a point value based on the length. The longer the word the more points.
    """
    score = {3: 1,
        4: 1,
        5: 2,
        6: 3,
        7: 5,
        8: 11,
        9: 11,
        10: 11,
        11: 11,
        12: 11,
        13: 11,
        14: 11,
        15: 11,
        16: 11}
    return score[len(word)]
​
​
​
####
# Run if invoked from command line
####
​
if __name__ == "__main__":
    main()
    input("Press enter to end")