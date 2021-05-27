import random
import time


def create_deck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')
    return deck


# returns the hand that is drawn
def deal_hand(num_of_cards, deck_to_use):
    player_hand = []
    for i in range(0, num_of_cards):
        drawn_card = random.choice(deck_to_use)
        deck_to_use.remove(drawn_card)
        player_hand.append(drawn_card)
    return player_hand


# returns the result of subtracting a player hand from the original deck
def remove_cards(large_set, smaller_set):
    large = set(large_set)
    small = set(smaller_set)
    new_set = list(large-small)
    return new_set


def reveal_hand(player_hand):
    count = 0
    print("Here are your cards:")
    for card in player_hand:
        count += 1
        print(f"{card} ----- {count}")
        time.sleep(0.5)


def pick_card(hand):
    user_choice = int(input("Pick a card by entering the number corresponding with your choice (1-3):"))
    user_choice -= 1
    return hand[user_choice]


def compare_cards(card1, card2):
    firstChar1 = card1[0]
    firstChar2 = card2[0]
    score_list = ["2","3","4","5","6","7","8","9","1","J","Q","K","A"]
    first_card_index = score_list.index(firstChar1)
    second_card_index = score_list.index(firstChar2)
    if first_card_index > second_card_index:
        return card1
    if second_card_index > first_card_index:
        return card2
    if first_card_index == second_card_index:
        return "tie"


def play_again():
    answered = False
    while not answered:
        response = input('Would you like to play another round (y/n) ?: ')
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Invalid response")
            continue


def end_of_game(score_player1, score_player2):
    if score_player1 > score_player2:
        print("Player 1 has WON")
        print(f'The final score has Player 1 winning with {score_player1} points to {score_player2}')
    elif score_player2 > score_player1:
        print("Player 2 has WON")
        print(f'The final score has Player 2 winning with {score_player2} points to {score_player1}')
    else:
        print(f"The game ended in a {score_player1} - {score_player2} draw")
    print("Thanks for playing!")
