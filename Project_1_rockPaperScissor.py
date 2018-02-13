# http://www.codeskulptor.org/#user41_wpWHc0mX6B_3.py

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

from random import randrange

# helper functions

def name_to_number(name):
    name_list = ['rock', 'Spock', 'paper','lizard', 'scissors']
    for i in range(5):
        if name_list[i]==name:
            return i


def number_to_name(number):
    name_list = ['rock', 'Spock', 'paper','lizard', 'scissors']
    return name_list[number]

def rpsls(player_choice): 
    player_num = name_to_number(player_choice)
    print "Player chooses", player_choice
    
    comp_num = randrange(5)
    print "Computer chooses", number_to_name(comp_num)
    
    if player_num == comp_num: print "Player and computer tie!\n"
    elif player_num == (comp_num+1)%5 or player_num == (comp_num+2)%5:
        print "Player wins!\n"
    else:
        print "Computer wins!\n"
    return 
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


