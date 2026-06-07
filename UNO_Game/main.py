import os

from deck import Deck
from player import Player
from card import Card

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_cards_side_by_side(cards):
    rendered_cards = []

    for card in cards:
        rendered_cards.append(str(card).split("\n"))

    for line_number in range(7):
        line = ""

        for card_lines in rendered_cards:
            line += card_lines[line_number] + "  "

        print(line)


def print_hand(player):
    print(f"{player.name}'s hand:")

    print_cards_side_by_side(player.hand)

    for i in range(len(player.hand)):
        print(f"     [{i}]     ", end="  ")

    print()


def get_card_choice(player):
    while True:
        try:
            choice = int(input("Choose a card index: "))

            if 0 <= choice < len(player.hand):
                return choice
            else:
                print("That card index is not in your hand.")

        except ValueError:
            print("Please enter a valid number.")

def player_turn(player, deck, last_top_card,round):

    if round == 1:
        for i in range(5):
            player.draw_card(deck)
    round += 1

    if last_top_card.value == 100:
        top_card = deck.draw()
    else:
        top_card = last_top_card

    input("Press Enter to clear the screen and start your turn...")
    clear_screen()

    print("Top card:")
    print(top_card)

    print_hand(player)

    choice = get_card_choice(player)
    chosen_card = player.hand[choice]

    print("You chose:")
    print(chosen_card)

    if chosen_card.can_play_on(top_card):

        top_card = player.play_card(choice)

        print("New top card:")
        print(chosen_card)
        last_top_card = chosen_card

    else:
        print("You cannot play this card.")
        print("You need to draw a card.")

        player.draw_card(deck)
        last_top_card = top_card

        print("Your hand after drawing:")
        print_hand(player)
    
    return round, last_top_card


# Game initialization and start
deck = Deck()
last_top_card = Card(color='White',value=100)
round1 = 1
round2 = 1
player1 = Player("Player 1")
player2 = Player("Player 2")

while True:
    print(f'This is round {round1}:')
    print('--------------------------')
    round1, last_top_card = player_turn(player1,deck,last_top_card,round1)
    round2, last_top_card = player_turn(player2,deck,last_top_card,round2)

    if player1.has_won():
        print("player 1 has won")
        break
    elif player2.has_won():
        print("player 2 has won")
        break
    else:
        print("no one wins yet...")        



