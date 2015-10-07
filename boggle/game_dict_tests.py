from game_dict import *
import game_dict 

from nose import with_setup


# print("dir at the start of test file is: ", dir())
# setup
def my_setup_function():
    print("in setup function")
    #global words
    words = []


# teardown
def my_teardown_function():
    print("in teardown function")
    global words
    words = []


# @with_setup(my_setup_function, my_teardown_function)
def test_read():

    global words
    file = ['hi']
    read(file, 3)
    print("words after assert 'hi': ", game_dict.words)
    assert words == []
    print("assertion passed!!!")

    file = ['his']
    read(file, 3)
    print("words after assert 'his': ", game_dict.words)
    #print("value of words in test file is: ", words)
    assert game_dict.words == ['his']
    print("assertion passed!!!")

    file = ['his-']
    read(file, 3)
    print("words after assert 'his-': ", game_dict.words)
    #print("value of words in test file is: ", words)
    assert game_dict.words == []
    print("assertion passed!!!")


def main():
    my_setup_function()
    test_read()
    my_teardown_function()

if __name__ == '__main__':
    main()
print("value of words outside of all functions is: ", words)