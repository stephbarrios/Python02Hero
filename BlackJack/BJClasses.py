
class Player:
    #hit function
    def hitOrStop():
        card_total = player_cardOne + player_cardTwo
        while True:
            print('Your total hand is {}'.format(card_total))
            player_turn = input('Would you like to hit or stop? 1 for hit, 2 for stop: ')

            if int(player_turn) == 1:
                card_total += newCard
                if card_total = 21:
                    print("Player wins! :)")
                elif card_total > 21:
                    print("You've BUSTED :( Dealer wins")
                    break
                elif card_total < 21:
                    continue
            elif int(player_turn) == 2:
                print('You chose to stop - the dealer will now play.')
                break

    #value function
        #^do we need this since we have hitOrStop func already

    #checkBankroll function
    def checkBankroll():
        #when and where to set bankRoll
        betAmount = input('How much do you want to bet? ')
        while True:
            if int(betAmount) > bankRoll:
                print('Sorry, you cannot bet more than what is in your bankroll')
            elif int(betAmount) <= bankRoll:
                bankRoll -= betAmount
                print('You bet {} tokens. You have {} token left in your bankroll.'.format(betAmount,bankRoll))

class Dealer:
    #hit, until sum > player's value or until = 21
    def dealer_turn():
        card_total = dealer_cardOne + dealer_cardTwo
        while True:
            if card_total < 21: #or player.card_total < dealer.card_total
                print("Dealer hits")
                card_total += newCard
                print('Your total hand is {}'.format(card_total))
            elif card_total = 21:
                print('21! BlackJack!')
            elif card_total > 21:
                print("It's a bust!! :(  Player wins!"))


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
