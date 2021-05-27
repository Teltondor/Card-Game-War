import time

import deck

player_1_score = 0
player_2_score = 0
continue_playing = True

while continue_playing:
    mainDeck = deck.create_deck()  # creates the first version of the deck

    player1hand = deck.deal_hand(3, mainDeck)  # deals the first players hand from the deck
    mainDeck = deck.remove_cards(mainDeck, player1hand)

    player2hand = deck.deal_hand(3, mainDeck)  # deals the second players hand from the deck
    mainDeck = deck.remove_cards(mainDeck, player2hand)

    print("Player 1 will pick a card first")
    deck.reveal_hand(player1hand)  # this shows the 1st player their hand, and prompts them to pick a card from it
    player1choice = deck.pick_card(player1hand)
    player1hand = deck.remove_cards(player1hand, player1choice)
    print("")

    print("Player 2 will now pick a card")
    deck.reveal_hand(player2hand)  # this shows the 2nd player their hand, and prompts them to pick a card from it
    player2choice = deck.pick_card(player2hand)
    player2hand = deck.remove_cards(player2hand, player2choice)
    print("")

    print(f'Player 1 picked {player1choice} and player 2 picked {player2choice}')  # summary of picks
    time.sleep(1)

    if deck.compare_cards(player1choice, player2choice) == player1choice:  # comparison of cards and win logic
        print("Player 1 won this round")
        player_1_score += 1
    if deck.compare_cards(player1choice, player2choice) == player2choice:
        print("Player 2 won this round")
        player_2_score += 1
    if deck.compare_cards(player1choice, player2choice) == "tie":
        print("Both cards are equivalent in value. This round is a tie.")
    time.sleep(1)

    print(f'Player 1 has {player_1_score} points and player 2 has {player_2_score} points')  # score update
    time.sleep(1)
    print("")

    continue_playing = deck.play_again()  # check on if player wants to continue
    print("")

deck.end_of_game(player_1_score, player_2_score)
