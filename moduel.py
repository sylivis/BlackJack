import random

class Basic_Rules:

    def __init__(self):
        self.deck= {}
        self.suit = {
                    'spade': [i for i in range(1, 14)], 
                    'club': [i for i in range(14, 27)],
                    'dimond': [i for i in  range(27, 40)],
                    'heart': [i for i in range(40, 53)]
                    }

        self.card_info = { 
                        'face':[11, 12, 13, 24, 25, 26, 37, 38, 39, 50, 51, 52],
                        'king':[13, 26, 39, 52],
                        'queen':[12, 25, 38, 51],
                        'jack':[11, 24, 37, 50], 
                        'ace':[1, 14, 27, 40]
                        }

        for i in range(1, 53):
            #spaid
            if i in self.suit['spade']:
                if i in self.card_info['face']:
                    if i in self.card_info['king']:
                        self.deck[i] = 'K of Spade'
                    if i in self.card_info['queen']:
                        self.deck[i] = 'Q of Spade'
                    if i in self.card_info['jack']:
                        self.deck[i] = 'J of Spade'
                if i in self.card_info['ace']:
                    self.deck[i] = 'A of Spade'
                elif i in range(2, 11):
                    self.deck[i] = f'{str(i)} of spaid'
            
            #club
            if i in self.suit['club']:
                if i in self.card_info['face']:
                    if i in self.card_info['king']:
                        self.deck[i] = 'K of club'
                    if i in self.card_info['queen']:
                        self.deck[i] = 'Q of club'
                    if i in self.card_info['jack']:
                        self.deck[i] = 'J of club'
                elif i in self.card_info['ace']:
                    self.deck[i] = 'A of club'
                elif i in range(15,24):
                    self.deck[i] = f'{str(i-13)} of club'
            
            #dimond
            if i in self.suit['dimond']:
                if i in self.card_info['face']:
                    if i in self.card_info['king']:
                        self.deck[i] = 'K of dimond'
                    if i in self.card_info['queen']:
                        self.deck[i] = 'Q of dimond'
                    if i in self.card_info['jack']:
                        self.deck[i] = 'J of dimond'
                elif i in self.card_info['ace']:
                    self.deck[i] = 'A of dimond'
                elif i in range(27, 37):
                    self.deck[i] = f'{str(i-26)} of dimond'

            #heart
            if i in self.suit['heart']:
                if i in self.card_info['face']:
                    if i in self.card_info['king']:
                        self.deck[i] = 'K of heart'
                    if i in self.card_info['queen']:
                        self.deck[i] = 'Q of heart'
                    if i in self.card_info['jack']:
                        self.deck[i] = 'J of heart'
                elif i in self.card_info['ace']:
                    self.deck[i] = 'A of heart'
                elif i in range(40,50):
                    self.deck[i] = f'{str(i-39)} of heart'
    
    def card_value(self, card):
        if card in self.card_info['face']:
            return 10
        if card in self.card_info['ace']:
            return 'ace'
        else: 
            return card - (13 * (card // 13))

    def your_points(self, hand):
        points = 0
        for card in hand:
            try:
                points += self.card_value(card)
                if points > 21:
                    return 'bust'
            except: 
                if points + 11 > 21:
                    points += 1
                else: 
                    points += 11

                if points > 21:
                    return 'bust'
        return points

class Dealer():

    def __init__(self):
        self.deck = [i for i in range(1, 53)]
        self.hand = []
        self.bust = False

    def shufle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)

    def take_deal(self, card):
        self.hand.insert(0, card)

    def reset(self):
        self.deck = [i for i in range(1, 53)]
        self.hand = []
        self.bust = False
    

class Player():

    def __init__(self):
        self.hand = []
        self.bust = False
    
    def take_deal(self, card):
        self.hand.insert(0, card)
    
    def reset(self):
        self.hand = []
        self.bust = False
    





    
            
    

    
        
        


        

