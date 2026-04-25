"""Functions to help play and score a game of blackjack."""


def value_of_card(card):
    """Determine the scoring value of a card."""

    face_cards = ['j', 'q', 'k']
    
    if card.lower() in face_cards:
        value = 10
    elif card.lower() == 'a':
        value = 1
    elif card in "23456789" or card == "10":
        value = int(card)

    return value 

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    
    if card_one_value < card_two_value:
        higher = card_two
    elif card_one_value > card_two_value:
        higher = card_one
    elif card_one_value == card_two_value:
        higher = card_one, card_two
    
    return higher


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card."""

    if card_one.lower() == 'a':
        card_one = 11
    else:
        card_one = value_of_card(card_one)
    if card_two.lower() == 'a':
        card_two = 11
    else:
        card_two = value_of_card(card_two)

    if (card_one + card_two + 11) <= 21:
        ace = 11
    else:
        ace = 1

    return ace

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""

    if card_one == 'A':
        card_one = 11
    elif card_one in ['J', 'Q', 'K']:
        card_one = 10
    else:
        card_one = int(card_one)
        
    if card_two == 'A':
        card_two = 11
    elif card_two in ['J', 'Q', 'K']:
        card_two = 10
    else:
        card_two = int(card_two)
        
    if (card_one + card_two) == 21:
        is_bj = True
    else:
        is_bj = False

    return is_bj
    

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""

    if value_of_card(card_one) == value_of_card(card_two):
        can_split = True
    else:
        can_split = False

    return can_split 

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    if (value_of_card(card_one) + value_of_card(card_two)) in range(9, 12):
        can_double = True
    else:
        can_double = False

    return can_double