balls = ['r', 'r', 'b', 'b,']


def ballgame(balls):
    random.shuffle(balls)

    return (balls, balls.pop())
    
ballgame(balls)

balls



def ballgame(num_red, num_blue):
balls = ['r']*num_red + ['b']*num_blue
    random.shuffle(balls)

    return (balls, balls.pop())
    
ballgame(10,10)


def ballgame(num_red, num_blue, select_k):
balls = ['r']*num_red + ['b']*num_blue
res = []
    for k in range(select_k):
	    random.shuffle(balls)
		res.append(balls.pop())
		print('ratio of blue to red in sack', balls.count('b')/balls.count('r'))
    assert len(balls) + len(res) == num_red + num_blue
    return ("balls = ", balls, "result = ", res)
    
ballgame(10,10, 5)






