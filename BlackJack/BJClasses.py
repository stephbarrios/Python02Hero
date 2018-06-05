
class Player:
    #hit function
    def hitOrStop():
        card_total = player_cardOne + player_cardTwo
        while True:
            print('Your total hand is {}'.format(card_total))
            player_turn = input('Would you like to hit or stop? 1 for hit, 2 for stop: ')

            if int(player_turn) == 1:
                card_total += newCard
            elif int(player_turn) == 2:
                print('You chose to stop - the dealer will now play.')
                break
   
    #value function
    #checkBankroll function
    pass

class Dealer:
    #hit, until sum > player's value or until = 21
    #setup (takes in deck; facedown = 2nd card)
    #reveal
    pass

class Deck:
    #randomized/shuffled
    #num. of cards (52)
    #drawCard
    pass

class Card:
    #values
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    #suits (each suit contains 13 cards- Ace through King)
    pass
