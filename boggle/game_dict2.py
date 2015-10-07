words = [ ]  

# Codes for result of search
WORD = 1
PREFIX = 2
NO_MATCH = 0

def read( file, min_length=3 ):
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
    global words
    words = [ ]
    for line in file:
        if len(line) >= 3 and "'" not in line and "-" not in line:
            words.append(line.strip())
		
    #FIXME: read the dictionary file into words.  Skip words that
    #   are too short or contain non-alphabetic characters
		    
    words = sorted(words)  # Being sorted is most important for binary search
	
    print(words)