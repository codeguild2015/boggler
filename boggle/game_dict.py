"""
game_dict: Game dictionary.

Authors:  Patrick and Dana
Consulted in design: Cole, Thunder and the internet

Differs from a spelling dictionary in that looking up a string
has three possible outcomes:  The string matches a word exactly,
or it does not match exactly but is a prefix of a word, or there is
no word starting with that string.
"""
 

# Codes for result of search
WORD = 1
PREFIX = 2
NO_MATCH = 0

def read(file1, min_length = 3 ):
    """Read the dictionary from a sorted list of words.
    Args:
        file: dictionary file (list of words, in alphabetical order), already open
        min_length: integer, minimum length of words to
            include in dictionary. Useful for games in
            which short words don't count.  For example,
            in Boggle the limit is usually 3, but in
            some variations of Boggle only words of 4 or
            more letters count.
    Returns:  nothing
    """

    words = [ ]
    for line in file1:
        if len(line.strip()) >= min_length\
        and "-" not in line\
        and "'" not in line:
            words.append(line.strip().lower())
    words = sorted(words)  # Being sorted is essential for binary search
    return words        

def search(str1, lst):
    max = len(lst)
    min = 0
    if lst[max//2] == str1 or max <= 3:
        if str1 == lst[max//2]\
        or str1 == lst[min]\
        or str1 == lst[max-1]:
            return WORD
        elif lst[max//2].startswith(str1)\
        or lst[min].startswith(str1)\
        or lst[max-1].startswith(str1):      
            return PREFIX
        else:
            return NO_MATCH
    else:
        if str1 < lst[max//2]:
            return search(str1, lst[:max//2 + 1]) # +1 to be inclusive
        else:
            return search(str1, lst[max//2:])
       
# def search_double_loop(str1, lst):      
#     def is_word(str1, lst):
#         max = len(lst)
#         min = 0
#         if str1 == lst[max//2]:
#             return WORD
#         if max//2 == 0:
#             return NO_MATCH
#         else:
#             if str1 > lst[max//2]:
#                 return is_word(str1, lst[max//2:])
#             else:
#                 return is_word(str1, lst[:max//2])


#     def is_prefix(str1, lst):
#         max = len(lst)
#         min = 0
#         if lst[max//2].startswith(str1):
#             return PREFIX
#         if max//2 == 0:
#             return NO_MATCH
#         else:
#             if str1 > lst[max//2]:
#                 return is_prefix(str1, lst[max//2:])
#             else:
#                 return is_prefix(str1, lst[:max//2])
    
#     val = is_word(str1, lst)
#     if val == WORD:
#         return WORD
#     if val == NO_MATCH:
#         if is_prefix(str1, lst) == PREFIX:
#             return PREFIX
#         else: 
#             return NO_MATCH


 # def search_linear(str1, words ):
    
 #    """Search function: Searches dict.txt for prefix of words and returns prefix
 #     also searches dict.txt for words that can be used on boggle board.
    
 #    Parameters
 #    ---------
 #    Input:
 #    str1: Parameter assigned to find prefix's in the dict.txt
 #    words: Parameter assigned to find possible words that can be used on the boggle board.

 #    Output:
 #    WORD: Words to be used on boggle board based on the dict.txt.
 #    PREFIX: Identifies prefix in dict.
 #    NO_MATCH: Returns no math.
 #    """
 #     if str1 in words:
 #         return WORD
 #     else:
 #         for word in words:
 #             if word.startswith(str1):
 #                 return PREFIX
 #         return NO_MATCH


#     # FIXME: I suggest using a linear search first, checking for exact matches
#     # with == and then for partial matches with the "startswith" function, e.g.,
#     # words[i].startswith(prefix). 
#     # Once you get the whole program working, you can make it much, much faster
#     # using a binary search (which we will discuss in class). 
    
    
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
    #my asserts to test binary search algorithm
    word_dict = read(open("sowpods.txt"), min_length=3)
    testEQ("Words in sowpods.txt (al)", search("al", word_dict), PREFIX)
    testEQ("Words in sowpods.txt (alp)", search("alp", word_dict), WORD) 
    testEQ("Words in sowpods.txt (alph)", search("alph", word_dict), PREFIX) 
    testEQ("Words in sowpods.txt (alpha)", search("alpha", word_dict), WORD)
    testEQ("Words in sowpods.txt (alphb)", search("alphb", word_dict), NO_MATCH)

    
    