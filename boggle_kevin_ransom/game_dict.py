"""
game_dict: Game dictionary.

Authors:  Kevin and Ransom
Consulted in design: Michael Young, Thunder Shiviah, Allen Downey (for binary 
search method).

Differs from a spelling dictionary in that looking up a stringhas three possible 
outcomes:  
The string matches a word exactly, or it does not match exactly but is a prefix
of a word, or there is no word starting with that string.
"""

words = [ ]  

# Codes for result of search. These codes are referenced in boggler.py
WORD = 1
PREFIX = 2
NO_MATCH = 0

def read( file, min_length = 3 ):
    """Read the dictionary from a sorted list of words.
    Args:
    -----
        file: dictionary file (list of words, in alphabetical order), already open
        min_length: integer, minimum length of words to include in dictionary. 
                    Default length 3 is used here.
    Returns:  nothing   
    """
    global words 
    words = [ ]
    for line in file:
        if "-" not in line and "\'" not in line: #We don't want words with 
                                                 #numbers or punctuation, e.g. 
                                                 #'don't', 'catch-22'
            word_ = line.split()
            for item in word_:               
                if len(item) >= min_length:
                    words.append(item) 
    words = sorted(words)  # Sorting the list for use in binary search. 

    #assert read(["don't", "catch-22", "word"], min_length =3) == (["word"])

def search( prefix ):
    """Search for a prefix string in the dictionary using an iterative binary search
    method. Code adapted from Allen Downey's 'How to Think Like a Computer Scientist.' 
    Note that this iterative method utilizes a while loop.  We have tested several 
    versions of dictionaries and though this method has been successful, future 
    refactoring should consider iterative loops for simplification.    

    Args:
    -----
        str:  A string to look for in the dictionary
    Returns:
    --------
        code WORD if str exactly matches a word in the dictionary,
            PREFIX if str does not match a word exactly but is a prefix
                of a word in the dictionary, or
        NO_MATCH if str is not a prefix of any word in the dictionary
    """
    
    global words  # This is our dictionary.
    lower_bound = 0
    upper_bound = len(words)
    matches = []  #Collects prefixes in order for binary search to finish its  
                  #search of complete words.
    while True:   #See note above for future refactoring of while statement.
        if lower_bound == upper_bound: #If search region becomes empty, 
                                       #terminate loop.
            break
        half_index = (lower_bound + upper_bound) // 2 # Next probe should be in the 
                                                      # middle of prior search area.
        mid_item = words[half_index] # Fetch the word at the halfway position.          
        if mid_item == prefix: 
            return WORD
        if mid_item.startswith(prefix):             
            matches.append(prefix)
        if mid_item < prefix: #Use upper half of search area for next round.
            lower_bound = half_index + 1
        else:
            upper_bound = half_index #Use lower half of search area next time.  
    if len(matches) > 0:
        return PREFIX
    else: 
        return NO_MATCH
   
"""Test driver"""
   
if __name__ == "__main__":
    # This code executes only if we execute game_dict.py by itself,
    # not if we import it into boggler.py
    from test_harness import testEQ
    read(open("shortdict.txt"))
    # shortdict contains "alpha", "beta","delta", "gamma", "omega"
    testEQ("First word in dictionary (alpha)", search("alpha"), WORD)
    testEQ("Last word in dictionary (omega)", search("omega"), WORD)
    testEQ("Within dictionary (beta)", search("beta"), WORD)
    testEQ("Within dictionary (delta)", search("delta"), WORD)
    testEQ("Within dictionary (gamma)", search("gamma"), WORD)
    testEQ("Prefix of first word (al)", search("al"), PREFIX)
    testEQ("Prefix of last word (om)", search("om"), PREFIX)
    testEQ("Prefix of interior word (bet)", search("bet"),PREFIX)
    testEQ("Prefix of interior word (gam)", search("gam"),PREFIX)
    testEQ("Prefix of interior word (del)", search("del"),PREFIX)
    testEQ("Before any word (aardvark)", search("aardvark"), NO_MATCH)
    testEQ("After all words (zephyr)", search("zephyr"), NO_MATCH)
    testEQ("Interior non-word (axe)", search("axe"), NO_MATCH)
    testEQ("Interior non-word (carrot)", search("carrot"), NO_MATCH)
    testEQ("Interior non-word (hagiography)",
        search("hagiography"), NO_MATCH)
    # Try again with only words of length at least 5
    # Now beta should be absent
    read(open("shortdict.txt"), min_length=5)
    print("New dictionary: ", dict)
    testEQ("First word in dictionary (alpha)", search("alpha"), WORD)
    testEQ("Last word in dictionary (omega)", search("omega"), WORD)
    testEQ("Short word omitted (beta)", search("beta"), NO_MATCH)
    read(open("dict.txt"))  # Long dictioanry
    testEQ("Can I find farm in long dictonary?", search("farm"), WORD)
    testEQ("Can I find bead in long dictionary?", search("bead"), WORD) 