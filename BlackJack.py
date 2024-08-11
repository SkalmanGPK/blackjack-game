import random
def show_menu():
    #displays the menu on startup.
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
    # call the function based on user's choice or print an error if the choice is invalid
    action = options.get(choice, invalid_choice)
    action()
def invalid_choice():
    print("Invalid choice. Please enter a number between 1 and 3.")
    show_menu() #Show menu again for new input
def start_new_game():
    print("\nStarting a new game!")
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()] #deals two cards to the player
    dealer_hand = [deck.pop(), deck.pop()] #deals two cards to the dealer
    # Display the player's hand
    print(f"\nYour hand: {player_hand} (value: {calculate_hand_value(player_hand)})")
    # Display the dealer's hand with one card hidden
    print(f"Dealer's hand: {dealer_hand[0]}, [hidden]")
    # Players turn
    while True:
        action = input("Do you want to hit or stand (H/S): ").lower()
        if action == 'h': # user hits
            player_hand.append(deck.pop())
            print(f"\nYour hand: {player_hand} (value: {calculate_hand_value(player_hand)})")
            if calculate_hand_value(player_hand) > 21:
                print("You bust, Dealer wins.")
                break
        elif action == 's': #user stands
            print("You chose to stand!")
            break
        else: # error handling
            print("Invalid choice. please enter 'h' to hit or 's' to stand.")
    if calculate_hand_value(player_hand) <= 21:
        print(f"\nDealer's hand: {dealer_hand} (value: {calculate_hand_value(dealer_hand)})")
        while calculate_hand_value(dealer_hand) <17:
            dealer_hand.append(deck.pop())
            print(f"Dealer draws a card. New hand: {dealer_hand} (value: {calculate_hand_value(dealer_hand)})")

        # Determine the winner
        player_total = calculate_hand_value(player_hand)
        dealer_total = calculate_hand_value(dealer_hand)
        print("\nFinal Results:")
        print(f"Your hand: {player_hand} (value: {player_total})")
        print(f"Dealer's hand: {dealer_hand} (value: {Dealer_total})")

        if dealer_total > 21:
            print("Dealer busts! You Win.")
        elif player_total > dealer_total:
            print("You win!")
        elif player_total < dealer_total:
            print("Dealer wins!")
        else:
            print("Push, it's a tie!")
    show_menu()
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
def calculate_hand_value(hand):
    #Calculate the value of a hand of cards.
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
            value += int(rank)
    #adjust for aces
    while value > 21 and aces:
        value -=10
        aces -= 1
    return value


if __name__ == "__main__":
    show_menu()