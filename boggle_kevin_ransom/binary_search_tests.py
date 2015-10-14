from game_dict import *

def search_test():
	# Tests dictionary with even number of items.
	read(['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot']) 
	assert search('alpha') == 1
	assert search ('cha') == 2
	print("Passed even-numbered dictionary!")

	# Tests dictionary with odd number of items.
	read(['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf']) 
	assert search('alpha') == 1
	assert search ('cha') == 2
	print("Passed odd-numbered dictionary!")

	read(['alpha']) # tests dictionary with length 1.
	assert search('alpha') == 1
	assert search('al') == 2
	assert search('bravo') == 0
	print("Passed single-item dictionary!")

	read([]) # tests empty dictionary
	assert search('alpha') == 0
	assert search('al') == 0
	assert search('bravo') == 0
	print("Passed single-item dictionary!")

if __name__ == "__main__":
	search_test()
