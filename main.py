import random

deck = ["1S", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
        "1H", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",]


def play_game():
    deck, player_hand, top_of_discard_pile = initial_set_up()  
    print_player_hand(player_hand)  
    deck, player_hand, top_of_discard_pile = player_turn(1, player_hand, deck, top_of_discard_pile)


def initial_set_up():
    player_hand = []

    random.shuffle(deck)

    for i in range(7):
        player_hand.append(deck.pop(0))

    top_of_discard_pile = deck.pop(0)

    return deck, player_hand, top_of_discard_pile


def print_player_hand(cards):
    hand = ""
    for i in range(len(cards)):
        hand += cards[i] + "   "
    print("Current player's hand is:")
    print(hand)


# add validation for where to pick card up from and if the discarded card is a valid card
def player_turn(playerNo, hand, deck, discard):
    print()
    print("It is player ", playerNo,"'s turn")
    print_player_hand(hand)
    print("You must either take a card from the top of the deck or the card on the top of the discard pile")
    print("The current card on top of the discard pile is ", discard)
    print("DECK or DISCARD PILE?")

    choice = input("-> ").upper()
    if choice == "DECK":
        hand.append(deck.pop(0))
    elif choice == "DISCARD PILE":
        hand.append(discard)
    else:
        print("INVALID OPTION")

    print("Card added to hand")
    print_player_hand(hand)
    print("You must now choose a card to discard")
    discard = input("-> ")

    return deck, hand, discard



play_game()



# https://www.w3schools.com/python/ref_random_shuffle.asp
# https://www.w3schools.com/python/ref_list_pop.asp