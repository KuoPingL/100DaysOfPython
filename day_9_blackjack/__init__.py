############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import art
import random


def get_score_in_cards(cards):
    score = 0
    for card in cards:
        if card == 1:
            score += 11
        elif card < 11:
            score += card
        else:
            score += 10

    if score > 21 and 1 in cards:
        score -= (11 - 1)

    return score


def fill_in_dealer_cards(dealer_cards, cards):
    while get_score_in_cards(dealer_cards) < 17:
        dealer_cards.append(cards.pop())

    return dealer_cards


def display_final_cards_and_score(player_cards, dealer_cards, player_score, dealer_score):
    print(f"Your final hand: {player_cards}\n\tCurrent score: {player_score}\n")
    print(f"Dealer's final card: {dealer_cards}\n\tCurrent score: {dealer_score}\n")


def play_game():
    print(f"{art.logo}")

    cards = [*range(1, 14)]

    random.shuffle(cards)
    player_cards = []
    dealer_cards = []
    player_cards.append(cards.pop())
    dealer_cards.append(cards.pop())
    player_cards.append(cards.pop())
    dealer_cards.append(cards.pop())

    print(f"Your cards: {player_cards}\n\tCurrent score: {get_score_in_cards(player_cards)}\n")

    print(f"Dealer's first card: {dealer_cards[0]}\n\tCurrent score: {get_score_in_cards([dealer_cards[0]])}\n")

    while get_score_in_cards(player_cards) < 21 and input("Type 'y' to get another card, type 'n' to pass:") == 'y':
        player_cards.append(cards.pop())

        print(f"Your cards: {player_cards}\n\tCurrent score: {get_score_in_cards(player_cards)}\n")

        print(f"Dealer's first card: {dealer_cards[0]}\n\tCurrent score: {get_score_in_cards([dealer_cards[0]])}\n")

    player_score = get_score_in_cards(player_cards)

    if player_score > 21:
        print("You lose\n")
    else:
        dealer_cards = fill_in_dealer_cards(dealer_cards, cards)
        dealer_score = get_score_in_cards(dealer_cards)

        print(dealer_cards)
        display_final_cards_and_score(player_cards, dealer_cards, player_score, dealer_score)

        if player_score > dealer_score or dealer_score > 21:
            print("You win\n")
        elif player_score < dealer_score:
            print("You lose")
        else:
            print("Push")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    play_game()

# while shouldContinue:
#   print(f"{art.logo}")
#   cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#   random.shuffle(cards)
#   gameDone = False
#   playerCards = []
#   dealerCards = []
#   while not gameDone:
#     # draw cards
#     # check if userCards is empty
#     if not playerCards:
#       # first draw
#       playerCards.append(cards.pop())
#       dealerCards.append(cards.pop())
#       playerCards.append(cards.pop())
#       dealerCards.append(cards.pop())

#     else:
#       # continue draw
#       playerCards.append(cards.pop())

#     print(f"Your cards: {playerCards}\n\tCurrent score: {getScoreInCards(playerCards)}\n")

#     print(f"Dealer's first card: {dealerCards[0]}\n\tCurrent score: {getScoreInCards([dealerCards[0]])}\n")

#     if getScoreInCards(playerCards) > 21:
#       gameDone = True
#     else:
#       gameDone = input("Type 'y' to get another card, type 'n' to pass:") == 'n'

#   # gameDone

#   dealer_score = getScoreInCards(dealerCards)
#   player_score = getScoreInCards(playerCards)

#   print(f"Your final hand: {playerCards}\n\tCurrent score: {player_score}\n")

#   print(f"Dealer's final card: {dealerCards}\n\tCurrent score: {dealer_score}\n")

#   if player_score > 21:
#     print("You lose\n")
#   else:
#     while getScoreInCards(dealerCards) < 17:
#       dealerCards.append(cards.pop())
#     if player_score > dealer_score:
#       print("You win\n")
#     elif player_score < dealer_score:
#       print("You lose")
#     else:
#       print("Push")

#   shouldContinue = input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'n'



