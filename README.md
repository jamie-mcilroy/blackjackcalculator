# Blackjack Odds Calculator

This Python script calculates the odds of winning in Blackjack based on the player's hand and the dealer's showing card. The script uses basic strategy and statistical simulations to estimate the odds.

## Features

- Calculates the value of a player's hand, adjusting for Aces.
- Simulates multiple rounds of Blackjack to estimate the probability of winning.
- Supports multiple decks (default is 8 decks, common in online casinos).
- Easy to use and modify for different scenarios.

## Requirements

- Python 3.x
- Collections module (part of the Python Standard Library)
- Random module (part of the Python Standard Library)

## Installation

1. Clone the repository or download the script.

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv blackjack
    ```

3. Activate the virtual environment:

    - On Windows:
      ```bash
      blackjack\Scripts\activate
      ```

    - On macOS and Linux:
      ```bash
      source blackjack/bin/activate
      ```

4. Install any necessary packages (none required for this script as it uses standard libraries):

    ```bash
    pip install -r requirements.txt  # This step is not necessary as no external packages are required
    ```

## Usage

1. Open the script (`odd_calc.py`) in your preferred Python IDE or text editor.

2. Modify the `player_hand` and `dealer_showing` variables with the appropriate cards. For example:

    ```python
    player_hand = ['A', '7']  # Example player hand
    dealer_showing = '6'      # Example dealer showing card
    ```

3. Run the script:

    ```bash
    python odd_calc.py
    ```

4. The script will output the estimated odds of winning based on the provided hands.

    ```bash
    Odds of winning: XX.XX%
    ```

## Example

```python
player_hand = ['A', '7']  # Example player hand
dealer_showing = '6'      # Example dealer showing card

odds = blackjack_odds(player_hand, dealer_showing, num_decks=8)
print(f'Odds of winning: {odds:.2f}%')


License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Feel free to submit issues and enhancement requests.

Acknowledgements
Python Software Foundation
Blackjack rules and strategies from various sources