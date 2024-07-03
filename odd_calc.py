import random
from collections import Counter

# Define the values of the cards
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def calculate_hand_value(hand):
    value = sum(card_values[card] for card in hand)
    # Adjust for aces
    aces = hand.count('A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def blackjack_odds(player_hand, dealer_showing, num_decks=8):
    # Original deck of cards
    original_deck = Counter(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4 * num_decks)
    # Calculate the player's hand value
    player_value = calculate_hand_value(player_hand)
    
    # If player has a blackjack
    if player_value == 21:
        return 100.0
    
    # Simulate the dealer's hand
    outcomes = {'win': 0, 'lose': 0, 'push': 0}
    simulations = 10000
    
    for _ in range(simulations):
        # Create a fresh deck for each simulation
        deck = original_deck.copy()
        deck.subtract(player_hand + [dealer_showing])
        
        dealer_hand = [dealer_showing]
        while calculate_hand_value(dealer_hand) < 17:
            card = random.choice(list(deck.elements()))
            dealer_hand.append(card)
            deck.subtract([card])
        
        dealer_value = calculate_hand_value(dealer_hand)
        
        if dealer_value > 21 or dealer_value < player_value:
            outcomes['win'] += 1
        elif dealer_value > player_value:
            outcomes['lose'] += 1
        else:
            outcomes['push'] += 1
    
    win_rate = (outcomes['win'] / simulations) * 100
    return win_rate

# Example usage
player_hand = ['A', '7']  # Example player hand
dealer_showing = '6'      # Example dealer showing card

odds = blackjack_odds(player_hand, dealer_showing, num_decks=8)
print(f'Odds of winning: {odds:.2f}%')
