# Importing the random module so that I can shuffle the deck of cards at the beginning of the game
import random


# A list of all the decks from the 4 suits in a deck of cards
deck = ["1S", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
        "1H", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",]


sets = []


def play_game():
    players_turn = 0

    players = get_information()
    deck, players, top_of_discard_pile = initial_set_up(players)  

    while True:  
        deck, players, top_of_discard_pile = player_turn(players_turn, players, deck, top_of_discard_pile)
        players_turn = ((players_turn + 1) % (len(players)))


def get_information():
    players = []
    print("Please enter the number of players for this game")
    no_of_players = int(input("-> "))
    for i in range(no_of_players):
        print("Player ", (i+1),"please enter your name")
        name = input("-> ")
        players.append([name, [], False])
    return players


def initial_set_up(players):
    random.shuffle(deck)
    '''
    for i in range(len(players)):
        player_hand = players[i][1]

        for j in range(7):
            player_hand.append(deck.pop(0))

        players[i][1] = player_hand'''

    players[0][1] = ["5S", "5H", "5C", "5D", "8S", "9S"]

    top_of_discard_pile = deck.pop(0)

    return deck, players, top_of_discard_pile


def print_player_hand(cards):
    hand = ""
    for i in range(len(cards)):
        hand += cards[i] + "   "
    print("Current player's hand is:")
    print(hand)


# add validation for where to pick card up from and if the discarded card is a valid card
def player_turn(playerNo, players, deck, discard):
    name = players[playerNo][0]
    hand = players[playerNo][1]

    print()
    print("It is",name,"'s turn")
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

    check_for_sets(players, playerNo)

    players[playerNo] = lay_on_sets(players[playerNo])

    print("You must now choose a card to discard")
    discard = input("-> ")
    
    for i in range(len(hand)):
        if hand[i] == discard:
            hand.remove(discard)
            break

    players[playerNo] = [name, hand]

    return deck, players, discard


def remove_card_set_from_hand(hand, i, j, k):
    hand.pop(k)
    hand.pop(j)
    hand.pop(i)
    return hand


# TODO: distinguish between 1 and 10
def check_for_sets(players, playerNo):
    hand = players[playerNo][1]
    for i in range(len(hand)):
        for j in range(i + 1, len(hand)):
            for k in range(j + 1, len(hand)):
                if (hand[i])[0] == (hand[j])[0] == (hand[k])[0]:
                    print("You have 3 of the same number")
                    card_set = [hand[i], hand[j], hand[k]]
                    print_card_set(card_set)
                    decision = input("Do you want to lay down this set of 3? (Y/N): ").upper()
                    if decision == "Y":
                        sets.append(card_set)
                        hand = remove_card_set_from_hand(hand, i, j, k)
                        check_for_sets(players, playerNo)
                        if players[playerNo][2] == False:
                            players[playerNo][2] = True
                        print_player_hand(hand)
    return hand


def print_card_set(card_set):
    print(card_set[0] + " " + card_set[1] + " " + card_set[2])


def lay_card_on_set(hand, card):
    for i in range(len(sets)):
        card_set = sets[i]
        if (card_set[0])[0] == (card_set[1])[0] == (card_set[2])[0] == card[0]:
            decision = input(f"Do you want to lay {card} down on a set? (Y/N): ")
            if decision == "Y":
                card_set.append(card)
                sets[i] = card_set
                hand.remove(card)

        

def lay_on_sets(player):
    print()
    for i in range(len(sets)):
        print(i, ") ", sets[i])
    print()
    decision = input("Do you want to lay down on a set? (Y/N): ").upper()
    if decision == "Y":
        print()
        print_player_hand(player[1])
        card = input("Which card do you want to lay down? ")
        lay_card_on_set(player[1], card)
    return player


play_game()



# https://www.w3schools.com/python/ref_random_shuffle.asp
# https://www.w3schools.com/python/ref_list_pop.asp
# https://www.w3schools.com/python/ref_list_remove.asp