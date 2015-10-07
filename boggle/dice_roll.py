import random

def dice_sim(die_size, rolls):

    results = 0
    dice_sum = 0

    for i in range(0,rolls):                
        results = random.randint(1,die_size) 
        print("Die %d rolled %d." % (i +1,results)) 
        dice_sum += results                         
                                                    
                                                    
    print("Total of %d dice rolls is: %d" % (rolls, dice_sum))
	
    return None

dice_sim(6,2)

"""For each integer, ‘i’, in the range [0, ‘rolls’], give us a 
random integer (“random.randint(initial value,inclusive value)”) 
value from 1 to ‘die_size’ inclusive and print the result of each roll. 
Additionally, we would like to sum each roll result and store this sum 
in the variable ‘dice_sum’.
The “+=” is basically saying to add the value of the variable on the 
left side to the value on the right and store it in the variable on the 
left side."""