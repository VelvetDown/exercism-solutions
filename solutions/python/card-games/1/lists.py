"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers."""
    rounds = [number, number+1, number+2]
    return rounds

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers."""
    all_rounds = rounds_1 + rounds_2
    return all_rounds

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number."""
    contains_round = number in rounds
    return contains_round

def card_average(hand):
    """Calculate and returns the average card value from the list."""
    return sum(hand)/len(hand)

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average."""
    hand.sort()
    if ((hand[0] + hand[-1]) / 2) == card_average(hand) or hand[(len(hand) // 2)] == card_average(hand):
        is_average = True
    else:
        is_average = False
    return is_average

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values)."""
    evens = hand[::2]
    odds = hand[1::2]

    if not evens or not odds:
        return False

    return sum(evens)/len(evens) == sum(odds)/len(odds)

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2."""
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
