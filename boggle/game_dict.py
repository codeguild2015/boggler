"""
game_dict: Game dictionary.

Authors:  Patrick and Dana
Consulted in design: Cole, Connor, Thunder, Andrew McNally and the internet

Differs from a spelling dictionary in that looking up a string
has three possible outcomes:  The string matches a word exactly,
or it does not match exactly but is a prefix of a word, or there is
no word starting with that string.
"""

# Codes for result of search
WORD = 1
PREFIX = 2
NO_MATCH = 0
 

def read(file1, min_length=3 ):
    """Builds the game dictionary from a sorted list of words.

    Itterates through a provided list of words.  All words of an appropriate 
        length (default 3 letters or longer) and playable in Boggle are added 
        to the final list which is returned.
    Args:
        file: dictionary file (list of words, in alphabetical order), already open
        min_length: integer, minimum length of words to include in 
            dictionary. Useful for games in which short words don't count.  
            For example, in Boggle the limit is usually 3, but in some 
            variations of Boggle only words of 4 or more letters count.
    Returns:  
        words: a list of words conforming to boggle rules in aphabetical order.
    """

    words = [ ]
    for line in file1:
        # words need to be pre-stripped to eliminate whitepace issues counting len
        if len(line.strip()) >= min_length\
        and "-" not in line\
        and "'" not in line:
            words.append(line.strip().lower())
    words = sorted(words)  # Being sorted is essential for binary search
    return words        


def search(str1, lst):
    """Recursive binary search function.

    Compares a string to a list of words.  Returns either
    that the string is a word, a prefix of at least 1 word or not in the list.

    Search is done by divinding the list in half and checking the search string 
    against the middle point of the split.  If the string is equal to the mid point
    then it stops and returns WORD.

    If the search string is not equal to the mid point then search will continue
    by persuing the half in which the string could be.  That half will be split 
    in half and so on.  

    When the list is 3 items or less the binary search stops and a linear approach
    is adopted.  This is to prevent infinite recursion on a list of 2 items.
   
    Parameters
    ---------
    Args:
        str1: A string to be compared against a game dictionary[list of words].
        words: A list of words to be searched.

    Returns:
        WORD: A variable denoting that the string input is a word in the list
        PREFIX: A variable denoting that the string input is a prefix 
            of at least 1 word in the list.
        NO_MATCH: A variable denoting that the string input is a word in the list
    """

    max = len(lst)
    min = 0
    # List of 3 is the base case as a list of 2 causes infinte recursion.
    if lst[max//2] == str1 or max <= 3:
        if str1 == lst[max//2]\
        or str1 == lst[min]\
        or str1 == lst[max-1]: # -1 corrects diff between len(list) and last index.
            return WORD
        elif lst[max//2].startswith(str1)\
        or lst[min].startswith(str1)\
        or lst[max-1].startswith(str1):      
            return PREFIX
        else:
            return NO_MATCH
    else:
        if str1 < lst[max//2]:
            return search(str1, lst[:max//2 + 1]) # +1 to inc. middle item of odd list
        else:
            return search(str1, lst[max//2:])


def search_linear(str1, words): 
    """This function is redundant and not called.  It is left in for 
    historical reasons.

    Search function.  Searches dict.txt for prefix of words and returns prefix
    also searches dict.txt for words that can be used on boggle board.
   
    Parameters
    ---------
    Input:
    str1: Parameter assigned to fing prefix's in the dict.txt
    words: Parameter assigned to find possible words that can be used on the boggle board.

    Output:
    WORD: Words to be used on boggle board based on the dict.txt.
    PREFIX: Identifies prefix in dict.
    NO_MATCH: Returns no math.
    """

    if str1 in words:
        return WORD
    else:
        for word in words:
            if word.startswith(str1):
                return PREFIX
        return NO_MATCH

    # FIXME: I suggest using a linear search first, checking for exact matches
    # with == and then for partial matches with the "startswith" function, e.g.,
    # words[i].startswith(prefix). 
    # Once you get the whole program working, you can make it much, much faster
    # using a binary search (which we will discuss in class). 
    
    
######################################################
#  Test driver
#    for testing game_dict.py by itself,
#    separate from boggler.py
#   Note we will need shortdict.txt and dict.txt for
#    testing.  Using the module does not require those files,
#    but this suite of test cases requires exactly those files
#    with exactly those names. 
#   
#
#   To test your game_dict module, invoke it on the
#   command line:
#      python3  game_dict.py    (in MacOS), or
#      python  game_dict.py     (in Windows)
#
#######################################################


if __name__ == "__main__":
    # This code executes only if we execute game_dict.py by itself,
    # not if we import it into boggler.py
    from test_harness import testEQ
    word_dict = read(open("shortdict.txt"))
    # shortdict contains "alpha", "beta","delta", "gamma", "omega"
    testEQ("First word in dictionary (alpha)", search("alpha", word_dict), WORD)
    testEQ("Last word in dictionary (omega)", search("omega", word_dict), WORD)
    testEQ("Within dictionary (beta)", search("beta", word_dict), WORD)
    testEQ("Within dictionary (delta)", search("delta", word_dict), WORD)
    testEQ("Within dictionary (gamma)", search("gamma", word_dict), WORD)
    testEQ("Prefix of first word (al)", search("al", word_dict), PREFIX)
    testEQ("Prefix of last word (om)", search("om", word_dict), PREFIX)
    testEQ("Prefix of interior word (bet)", search("bet", word_dict),PREFIX)
    testEQ("Prefix of interior word (gam)", search("gam", word_dict),PREFIX)
    testEQ("Prefix of interior word (del)", search("del", word_dict),PREFIX)
    testEQ("Before any word (aardvark)", search("aardvark", word_dict), NO_MATCH)
    testEQ("After all words (zephyr)", search("zephyr", word_dict), NO_MATCH)
    testEQ("Interior non-word (axe)", search("axe", word_dict), NO_MATCH)
    testEQ("Interior non-word (carrot)", search("carrot", word_dict), NO_MATCH)
    testEQ("Interior non-word (hagiography)",
        search("hagiography", word_dict), NO_MATCH)
    # Try again with only words of length at least 5
    # Now beta should be absent
    word_dict = read(open("shortdict.txt"), min_length=5)
    testEQ("First word in dictionary (alpha)", search("alpha", word_dict), WORD)
    testEQ("Last word in dictionary (omega)", search("omega", word_dict), WORD)
    testEQ("Short word omitted (beta)", search("beta", word_dict), NO_MATCH)
    word_dict = read(open("dict.txt"))  # Long dictioanry
    testEQ("Can I find farm in long dictonary?", search("farm", word_dict), WORD)
    testEQ("Can I find bead in long dictionary?", search("bead", word_dict), WORD) 
    #Asserts add by Patrick and Dana to test binary search algorithm
    word_dict = read(open("sowpods.txt"), min_length=3)
    testEQ("Searching word/prefix in sowpods.txt (al)", search("al", word_dict), PREFIX)
    testEQ("Searching word/prefix in sowpods.txt (alp)", search("alp", word_dict), WORD) 
    testEQ("Searching word/prefix in sowpods.txt (alph)", search("alph", word_dict), PREFIX) 
    testEQ("Searching word/prefix in sowpods.txt (alpha)", search("alpha", word_dict), WORD)
    testEQ("Searching word/prefix in sowpods.txt (alphb)", search("alphb", word_dict), NO_MATCH)

    
    
