import random
import sys

INSTRUCTIONS = """
  (H)it
  (S)tand
  """
 # to create a card deck with 52 cards 
cards_number = ["K","Q", "J","10","9","8","7","6","5","4","3","2","A"]
cards_type = ["Heart", "Spades", "Diamonds", "Clubs"]
card_deck = []
for i in cards_number: 
 for x in cards_type:
  card_deck.append(i + " of " + x)

random.shuffle(card_deck)
 
def card_value(v):
    """returns value for a given card"""
    if v[:1] in ("K","Q","J"):
        return 10
    elif v[:1] in ("A"):
        return 11
    else: 
        return int(v[:2])

def deal_card(hand, type):
    """to deal a new card and show the new card"""
    card = card_deck.pop()
    hand.append(card)
    print "{} was dealt to the {}.".format(card, type)

def my_sort_key(x):
    """create a customize sort function to sort hand list, so that when "A" is in hand, "A" goes to the end"""
    if x == "A":
        return 0
    else:
        return -1
        
def hand_value(hand):
    """to show hand value"""
    hand_value = 0
    hand.sort(key=my_sort_key)
    for card in hand:
        if card == "A":
	        if hand_value >= 11: 
	            hand_value += 1
	        else: 
	            hand_value += 11
        else:
	        hand_value += card_value(card)
    return hand_value

def hand_value_test():
    """to test the accuracy of "A"'s value from 11 to 1"""
    got = hand_value(["A", "Q", "10"])
    assert got == 21, "got {}".format(got)

def print_dealer_hand(dealer_hand):
    print "Dealer has {} in hand. ".format(hand_value(dealer_hand))
    
def print_player_hand(player_hand):
    print "Player has {} in hand. ".format(hand_value(player_hand))

def ask_input(options):
    """to ask player for a valid option: hit or stand"""
    player_answer = raw_input("> ").capitalize()
    while player_answer not in options:
        player_answer = raw_input("> ").capitalize()
    return player_answer
    
def continue_game():
    print "Would you like to play again? "
    ask_player = raw_input("> ").capitalize()
    if ask_player == "Y":
        play_game()
    elif ask_player == "N":
        print "Bye, see you around!"
        sys.exit()
    else:
        print "Invalid option. Please pick Y or N"
        continue_game()

def play_game():
    """To start the game."""
    player_hand = []
    dealer_hand = []
    print "Welcome to Blackjack!"
    print
    
    deal_card(player_hand, "player")
    deal_card(player_hand, "player")
    deal_card(dealer_hand, "dealer")
    print 
    print_player_hand(player_hand)
    print_dealer_hand(dealer_hand)

    print INSTRUCTIONS
    
    choice = ask_input(["H","S"])
    while choice == "H":
        deal_card(player_hand, "player")
        print_player_hand(player_hand)
        if hand_value(player_hand) > 21:
            print
            print "Busted!"
            print
            continue_game()
        else:
            choice = ask_input(["H","S"])
    if hand_value(player_hand) == 21:
        print "Blackjack! You win!"
    if hand_value(player_hand) > 21:
        print "Busted"
        continue_game()
    assert(choice == "S")
    while hand_value(dealer_hand) <= 17:
        deal_card(dealer_hand,"dealer")
        print_dealer_hand(dealer_hand)
        print
    if hand_value(dealer_hand) > hand_value(player_hand) and hand_value(dealer_hand) <= 21:
        print "Dealer wins!"
    elif hand_value(dealer_hand) < hand_value(player_hand) or hand_value(dealer_hand) > 21:
        print "Player wins!"
    else:
        print "It's a tie!"
    continue_game() 

hand_value_test()

play_game()    
