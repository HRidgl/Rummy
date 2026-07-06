import random

deck = ["1S", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
        "1H", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",]


def play_game():
    deck, player_hand = initial_set_up()  
    print_player_hand(player_hand)  


def initial_set_up():
    player_hand = []

    random.shuffle(deck)

    for i in range(7):
        player_hand.append(deck.pop(0))

    return deck, player_hand


def print_player_hand(cards):
    hand = ""
    for i in range(len(cards)):
        hand += cards[i] + "   "
    print(hand)


play_game()



# https://www.w3schools.com/python/ref_random_shuffle.asp
# https://www.w3schools.com/python/ref_list_pop.asp