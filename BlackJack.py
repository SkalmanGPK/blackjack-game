import random
def show_menu():
    #displays the menu on startup.
    print("Welcome to Blackjack!")
    print("Please choose an option:")
    print("1. Start a new game")
    print("2. View instructions")
    print("3. Quit")
    choice = input("Enter your choice (1-3):")

def start_new_game():
    print("\nStarting a new game!")

    play_blackjack()
def view_instructions():
    #displays the instructions
    print("\nBlackjack instructions:")
    print("1. The goal of the game is to get as close to 21 as possible without exceeding it.")
    print("2. Eeach player is dealt two cards initially.")
    print("3. You can choose to 'hit' (get another card) or stand (keep your current hand).")
    print("4. Numbered cards are worth their face value. Face cards are worth 10. Aces can be 1 or 11.")
    print("5. The dealer must hit until the sum of their cards are of total 17 or higher.")
    show_menu() #show the menu again after displaying instructions
def quit_game():
    print("Thank you for playing! Goodbye!")
    exit() #Exit the program
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck
