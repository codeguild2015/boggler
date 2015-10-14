from game_dict import *

words = ["abaci"]
assert search("aba") == PREFIX
assert search("abs") == WORD
assert search("abc") == NO_MATCH