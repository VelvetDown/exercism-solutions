"""Functions for calculating steps in exchanging currency."""



def exchange_money(budget, exchange_rate):

    exchanged_budget = budget / exchange_rate
    return exchanged_budget

def get_change(budget, exchanging_value):

    change = budget - exchanging_value
    return change

def get_value_of_bills(denomination, number_of_bills):

    value_of_bills = denomination * number_of_bills
    return value_of_bills


def get_number_of_bills(amount, denomination):

    number_of_bills = int(amount / denomination)
    return number_of_bills


def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    whole = amount / denomination
    whole = int(whole)
    leftover = amount - (denomination * whole)
    return leftover

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    exchange_fee = exchange_rate + (exchange_rate * (spread / 100))
    number_of_bills = int((budget / exchange_fee) / denomination)
    total_result = denomination * number_of_bills
    return total_result