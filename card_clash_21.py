import random
# Global Configurations
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
}

def create_deck():
    """Returns a list of 52 tuples representing a standard deck: (rank, suit)"""
    # Creates all 52 cards in the deck
    deck = []
    for i in suits:
        for j in ranks:
            deck.append((j, i))
    
    return deck

def shuffle_deck(deck):
    """Shuffles the deck list in-place."""
    # Randomly shuffles the deck created in create_deck(), using the random module
    random.shuffle(deck)

def deal_card(deck):
    """Removes and returns the top card from the deck."""
    # Removes top card from deck that was generated previously, and returns it
    return deck.pop()

def calculate_score(hand):
    """
    Calculates the total value of cards in a hand.
    Requirement: If the score is over 21 and the hand contains an Ace, 
    reduce the score by 10 until the score is <= 21 or no Aces remain.
    """
    # Keeps track of the score and number of aces using variables, along with logic/protection against aces
    score = 0
    aces = 0
    for rank, suit in hand:
        score = score + values[rank]
        if rank == "Ace":
            aces = aces + 1
    
    while score > 21 and aces > 0:
        score = score - 10
        aces = aces - 1
    return score

def show_hand(player_name, hand, hide_first_card=False):
    """Prints the formatted hand and current score for the user."""
    # Display's the current player, score, and if they have a hidden card or not, along with what cards exactly they have
    print(player_name + "'s hand: ")
    if hide_first_card:
        print("Hidden")
        for rank, suit in hand[1:]:
            print(rank + " of " + suit)
        print("Score: " + str(calculate_score(hand[1:])) + ", along with hidden card")
    else:
        for rank, suit in hand:
            print(rank + " of " + suit)
        print("Score: " + str(calculate_score(hand)))

def play_game():
    """Main game loop managing turns, user input, and winner logic."""
    # Defines variables
    deck = create_deck()
    shuffle_deck(deck)
    player_hand = []
    dealer_hand = []
    
    # Deals the initial two cards per player
    for i in range(2):
        player_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))
    
    # Shows both the Dealer's and Player's hands
    show_hand("Dealer", dealer_hand, hide_first_card=True)
    show_hand("Player", player_hand)
    
    # Input whether the Player wants to hit or stand
    while calculate_score(player_hand) < 21:
        choice = input("Hit or Stand: ").strip().lower()
        if choice == "stand":
            break
        elif choice == "hit":
            player_hand.append(deal_card(deck))
            show_hand("Player", player_hand)
            if calculate_score(player_hand) > 21: # Sends message if the player ends up busting
                print("The Player has bust, Dealer wins.")
                return
        else:
            print("Please enter either 'Hit' or 'Stand'.")
    
    # Shows Dealer's hand, now that the player has gone
    show_hand("Dealer", dealer_hand)
    
    # Adds AI for Dealer, making them stand once they reach or exceed a total score of 17
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
        show_hand("Dealer", dealer_hand)
    
    # Recalculates and defines both Player and Dealer scores
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    # The possible game endings, other than the Player busting as defined above
    if dealer_score > 21:
        print("The Dealer has bust, Player wins.")
    elif player_score > dealer_score:
        print("The Player has won.")
    elif dealer_score > player_score:
        print("The Dealer has won.")
    else:
        print("The game has tied.")

if __name__ == "__main__":
    play_game()



