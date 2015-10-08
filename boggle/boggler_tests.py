import boggler
from boggle_board import BoggleBoard
import game_dict



if __name__ == '__main__':
    board = BoggleBoard('thfaatrtcouswhms')
    assert board.get_char(1, 2) == 'r'
    board.mark_taken(1, 2)
    assert board.in_use[1][2] == True
    board.unmark_taken(1, 2)
    assert board.in_use[1][2] == False
    assert board.available(1, 2)
    board2 = BoggleBoard('thezzzzzzzzzzzzz')
    results = []
    assert boggler.find_words(board2, 1, 1, '', results) == ['the']
    assert boggler.score('word') == 1
    assert boggler.score('aquittal') == 5
    assert game_dict.read(shortdict.txt, 3) == ['alpha', 'beta', 'delta', 'gamma', 'omega']
    assert 'can\'t' not in game_dict.reat(dict.txt, 3)
    assert search('alpha') == 'WORD'
    assert search('alph') == 'PREFIX'
    assert search('alskdaf') == 'NO_MATCH'
    assert search('') == 'PREFIX'