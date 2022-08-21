from time import sleep
import moduel as bj

wut_is = bj.Basic_Rules()
tods = bj.Dealer()
your = bj.Player()
running = True



def state_of_game(dealer_hand, player_hand):
    print("your_hand:")
    for card in player_hand:
        print(f'{wut_is.deck[card]}')
    print(f'Total Points: {wut_is.your_points(player_hand)}')
    print('-----------------------')
    print("Tod's hand:")
    for card in dealer_hand:
        if dealer_hand.index(card) == 0:
            print('?????????')
        else:
            print(f'{wut_is.deck[card]}')



def start_game():
    print('shufling the deck')
    sleep(1)
    print('.')
    tods.shufle()
    sleep(1)
    print('.')
    tods.shufle()
    sleep(1)
    print('.')
    tods.shufle()
    print('the deeler will now deel.')
    print('\n \n \n \n \n')
    your.take_deal(tods.deal())
    tods.take_deal(tods.deal())
    your.take_deal(tods.deal())
    tods.take_deal(tods.deal())



def try_again(player, tod):
    
    again = True
    while again == True:
        re2 = input('would you like to play again?')
        print('type "yes" or "no"')
        try:
            if re2.lower() == 'yes':
                player.reset()
                tod.reset()
                return True
            if re2.lower() == 'no':
                again = False
            else:
                print('try again')
        except:
            print('try again....')
    


def take_turn(turn_taker):
    a_turn = True

    while a_turn == True and turn_taker.bust == False:
        print('\n\n------------------')
        print('Hit or Pass? \n type 1 to hit, type 2 to pass')
        try:
            action = int(input())
            if action == 1:
                your.take_deal(tods.deal())
                state_of_game(tods.hand, your.hand)

                if wut_is.your_points(turn_taker.hand) == 'bust':
                    print('You bust')
                    turn_taker.bust = True
            
            if action == 2:
                state_of_game(tods.hand, your.hand)
                print('turn passed')
                a_turn = False
        except:
            print('try again...')



def tod_turn():
    try:
        while wut_is.your_points(tods.hand) < 17:
            tods.take_deal(tods.deal())
    except:
        pass
    state_of_game(tods.hand, your.hand)



def the_reveal(dealer_hand, player_hand):
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print("your_hand:")
    for card in player_hand:
        print(f'{wut_is.deck[card]}')
    print(f'Total Points: {wut_is.your_points(player_hand)}')
    print('-----------------------')
    print("Tod's hand:")
    for card in dealer_hand:
        print(f'{wut_is.deck[card]}')
    print(f'Total Points: {wut_is.your_points(dealer_hand)}')






print('Welcome! Take a seet, and play a hand.\n The game: Black jack')
print('\n \n \n ')
while running == True:
    re = input("Type 'quit' to exit, or 'start' to start a new game.\n").lower()
    if re == "start":
        start_game()
        state_of_game(tods.hand, your.hand)
        take_turn(your)
        if wut_is.your_points(your.hand) == 'bust':
            print('\n \n \n you lost :( \n \n ')
            if try_again(your, tods):
                continue
            else:
                running = False
        
        tod_turn()
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        the_reveal(tods.hand, your.hand)
        try:
            if wut_is.your_points(tods.hand) == 'bust' or wut_is.your_points(tods.hand) < wut_is.your_points(your.hand):
                print('You win!')
            else:
                print('You Lose :(')

            if try_again(your, tods):
                continue
            else:
                running = False
        except:
            print('You win!')
            try_again(tods.hand, your.hand)
    if re == "quit":
        break

print('\n \nThank you for palying!')

                    
            

