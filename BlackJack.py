import random
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_event(event):
    logging.info(event)
def show_menu():
    # Displays the menu on startup.
    print("Welcome to Blackjack!")
    print("Please choose an option:")
    print("1. Start a new game")
    print("2. View instructions")
    print("3. Quit")
    choice = input("Enter your choice (1-3):")
    # Define a dictionary to act as a switch-case
    options = {
        '1': start_new_game,
        '2': view_instructions,
        '3': quit_game
    }
    # Call the function based on user's choice or print an error if the choice is invalid
    action = options.get(choice)
    if action:
        action()
    else:
        invalid_choice()
def invalid_choice():
    print("Invalid choice. Please enter a number between 1 and 3.")
    show_menu() # Show menu again for new input
def start_new_game():
    log_event("Starting a new game.")
    print("\nStarting a new game!")

    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()] # Deals two cards to the player
    dealer_hand = [deck.pop(), deck.pop()] # Deals two cards to the dealer
    # Display the player's hand
    print(f"\nYour hand: {player_hand} (value: {calculate_hand_value(player_hand)})")
    # Display the dealer's hand with one card hidden
    print(f"Dealer's hand: {dealer_hand[0]}, [hidden]")
    time.sleep(2) # Pause for 2 seconds

    # Players turn
    while True:
        action = get_player_action()
        if action == 'h': # User hits
            player_hand.append(deck.pop())
            print(f"\nYour hand: {player_hand} (value: {calculate_hand_value(player_hand)})")
            if calculate_hand_value(player_hand) > 21:
                print("You bust, Dealer wins.")
                log_event("Player busts. Dealer wins")
                break
        elif action == 's': # User stands
            print("You chose to stand!")
            break
    # Dealer's turn if player hans't busted   
    if calculate_hand_value(player_hand) <= 21:
        print(f"\nDealer's hand: {dealer_hand} (value: {calculate_hand_value(dealer_hand)})")
        time.sleep(2) # Pause for 2 seconds
        while calculate_hand_value(dealer_hand) <17:
            dealer_hand.append(deck.pop())
            print(f"Dealer draws a card. New hand: {dealer_hand} (value: {calculate_hand_value(dealer_hand)})")
            time.sleep(3) # Pause for 3 seconds

        # Determine the winner
        player_total = calculate_hand_value(player_hand)
        dealer_total = calculate_hand_value(dealer_hand)
        print("\nFinal Results:")
        print(f"Your hand: {player_hand} (value: {player_total})")
        print(f"Dealer's hand: {dealer_hand} (value: {dealer_total})")
        time.sleep(2) # pause for 2 seconds

        if dealer_total > 21:
            print("Dealer busts! You Win.")
            log_event("Dealer busts. Player wins")
        elif player_total > dealer_total:
            print("You win!")
            log_event("player wins.")
        elif player_total < dealer_total:
            print("Dealer wins!")
            log_event("Dealer wins.")
        else:
            print("Push, it's a tie!")
            log_event("Push, it's a tie!")
        time.sleep(3) # pause for 3 seconds

    show_menu()
def get_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please enter one of {valid_choices}")

def get_player_action():
    return get_choice("Do you want to hit or stand (H/S): ", ['h', 's'])

def view_instructions():
    # Displays the instructions
    print("\nBlackjack instructions:")
    print("1. The goal of the game is to get as close to 21 as possible without exceeding it.")
    print("2. Eeach player is dealt two cards initially.")
    print("3. You can choose to 'hit' (get another card) or stand (keep your current hand).")
    print("4. Numbered cards are worth their face value. Face cards are worth 10. Aces can be 1 or 11.")
    print("5. The dealer must hit until the sum of their cards are of total 17 or higher.")
    time.sleep(5) # Pause for 5 seconds
    show_menu() # Show the menu again after displaying instructions
def quit_game():
    print("Thank you for playing! Goodbye!")
    exit() # Exit the program
def create_deck():
    suits = ['♥', '♦', '♣', '♠']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck
def calculate_hand_value(hand):
    # Calculate the value of a hand of cards.
    if not hand:
        return 0 # Handle the empty hand edge case
    value = 0
    aces = 0
    for card in hand:
        rank, suit = card
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            aces += 1
            value += 11
        else:
            try:
                value += int(rank)
            except ValueError:
                print(f"Invalid card rank: {rank}")
                return 0
    # Adjust for aces
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def format_hand(hand):
    # Formats a hand for display
    return ', '.join([f"{rank}{suit}" if card != 'Hidden' else '[Hidden]' for card in hand for rank, suit in [card]])

if __name__ == "__main__":
    show_menu()