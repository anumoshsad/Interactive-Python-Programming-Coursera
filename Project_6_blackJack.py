# http://www.codeskulptor.org/#user42_nCmvg3w6oO_6.py

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        # create Hand object

    def __str__(self):
        return(' '.join(card.__str__() for card in self.cards))
            
        # return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)
        # add a card object to a hand

    def get_value(self):
        val = 0
        A = False
        for card in self.cards:
            val += VALUES[card.get_rank()]
            if card.get_rank()=='A':
                A = True
        if A == True and val+10<22:
            val+=10
        return val
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
            # draw a hand on the canvas, use the draw method for cards
        
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += 90
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))
            # create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        return(' '.join(card.__str__() for card in self.deck))	# return a string representing the deck
        


#define event handlers for buttons
def deal():
    global outcome, score, in_play, player, dealer, deck

    # your code goes here
    if in_play:
        outcome = 'You lose.'
        score-=1
        in_play = False
        
    else:    
        deck = Deck()
        deck.shuffle()
        player = Hand()
        dealer = Hand()
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        #print('Player: '+ player.__str__())
        #print('Dealer: '+ dealer.__str__())
        in_play = True
        outcome = ''

def hit():
    # replace with your code below
    global in_play, score, outcome 
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(deck.deal_card())
   
    # if busted, assign a message to outcome, update in_play and score
        if player.get_value()>21:
            outcome = "You went bust and lose."
            in_play = False
            score-=1

def stand():
    # replace with your code below
    global in_play, score, outcome
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while in_play and dealer.get_value()<17:
        dealer.add_card(deck.deal_card())
    # assign a message to outcome, update in_play and score
    if in_play:
        if dealer.get_value()>21:
            outcome = "Dealer went bust. You win."
            in_play = False
            score+=1
        else:
            if player.get_value()>dealer.get_value():
                outcome = 'You win.'
                in_play = False
                score +=1
            else:
                outcome = 'You lose.'
                in_play = False
                score -=1


# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome, score
    canvas.draw_text("Blackjack",(50, 100), 50, 'Aqua')
    canvas.draw_text("Score "+str(score),(400, 100), 30,'Black')
    canvas.draw_text("Dealer",(50, 150), 30,'Black')
    canvas.draw_text("Player",(50, 350), 30,'Black')
    canvas.draw_text(outcome,(200, 150), 30,'Black')
    if in_play:
        canvas.draw_text('Hit or Stand?',(200, 350), 30,'Black')
    else:
        canvas.draw_text('New Deal?',(200, 350), 30,'Black')
    player.draw(canvas, [50, 400])
    dealer.draw(canvas, [50, 200])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_SIZE, [86,249], CARD_SIZE)
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric