# Importing the random module so that I can shuffle the deck of cards at the beginning of the game
import random

## TODO: VALIDATION USING ENUMS
## TODO: Distinguish between 1 and 10
## TODO: Break larger functions down into smaller ones
## TODO: Add validation for where to pick card up from and if the discarded card is a valid card
## TODO: RUMMY situation

# A list of all the decks from the 4 suits in a deck of cards
deck = ["1S", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
        "1H", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",]


# An array which will lay all sets placed down by players 
sets = []


# Main game loop that calls relevant functions
def play_game():
    players_turn = 0

    players = get_information()
    deck, players, top_of_discard_pile = initial_set_up(players)  

    while True:  
        deck, players, top_of_discard_pile = player_turn(players_turn, players, deck, top_of_discard_pile)
        if len(players[players_turn][1]) == 0:
            print("*********************") 
            print(f"{players[players_turn][0]} has cards in their hand so have won the game")
            break
        players_turn = ((players_turn + 1) % (len(players)))


# Gets all players to be named and added to the players array
def get_information():
    players = []
    print("Please enter the number of players for this game")
    no_of_players = int(input("-> "))
    for i in range(no_of_players):
        print("Player ", (i+1),"please enter your name")
        name = input("-> ")
        players.append([name, [], False])
    return players


# Shuffles the deck, deals 7 cards to each player and flips the top card of the deck over to be the discard pile
def initial_set_up(players):
    random.shuffle(deck)

    for i in range(len(players)):
        player_hand = players[i][1]

        for j in range(7):
            player_hand.append(deck.pop(0))

        players[i][1] = player_hand


    top_of_discard_pile = deck.pop(0)

    return deck, players, top_of_discard_pile


# Outputs the cards in a player's hand in a readable, user-friendly way
def print_player_hand(cards):
    hand = ""
    for i in range(len(cards)):
        hand += cards[i] + "   "
    print("Current player's hand is:")
    print(hand)


# This function represents a standard player turn and allows the user to perform all relevant actions on their turn
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


# Removes the cards from a player's hand which form a set using the pop method
def remove_card_set_from_hand(hand, i, j, k):
    hand.pop(k)
    hand.pop(j)
    hand.pop(i)
    return hand


# Iterates over the cards in a player's
def check_for_sets(players, playerNo):
    hand = players[playerNo][1]
    for i in range(len(hand)):
        for j in range(i + 1, len(hand)):
            for k in range(j + 1, len(hand)):
                if (hand[i])[0] == (hand[j])[0] == (hand[k])[0]:
                    print("You have 3 of the same number")
                    card_set = [hand[i], hand[j], hand[k]]
                    print(format_card_set(card_set))
                    decision = input("Do you want to lay down this set of 3? (Y/N): ").upper()
                    if decision == "Y":
                        sets.append(card_set)
                        hand = remove_card_set_from_hand(hand, i, j, k)
                        check_for_sets(players, playerNo)
                        if players[playerNo][2] == False:
                            players[playerNo][2] = True
                        print_player_hand(hand)
    return hand


# Returns a formatted string which represents all cards in a card set
def format_card_set(card_set):
    card_set_string = ""
    for i in range(len(card_set)):
        card_set_string += card_set[i] 
        card_set_string += " "
    return card_set_string


# Allows the user to lay a card from their hand onto a corresponding set
def lay_card_on_set(hand):
    set_no = int(input(f"Which set do you want to lay on? "))
    card_set = sets[set_no-1]
    card = input(f"Which card do you want to lay on set {set_no}? ")
    if (card_set[0])[0] == (card_set[1])[0] == (card_set[2])[0] == card[0]:
        card_set.append(card)
        sets[set_no-1] = card_set
        hand.remove(card)
        print(f"{card} added to set {set_no}")
    return hand

        
# Outputs all the existing global sets and asks the user if they want to lay down on a set
def lay_on_sets(player):
    print()
    print("* EXISTING GLOBAL SETS *")
    for i in range(1, len(sets)+1):
        print(i,") ",format_card_set(sets[i-1]))
    print()
    decision = input("Do you want to lay down on a set? (Y/N): ").upper()
    if decision == "Y":
        print()
        print_player_hand(player[1])
        player[1] = lay_card_on_set(player[1])
        lay_on_sets(player)
    return player

# --- MAIN ---

play_game()



# https://www.w3schools.com/python/ref_random_shuffle.asp
# https://www.w3schools.com/python/ref_list_pop.asp
# https://www.w3schools.com/python/ref_list_remove.asp