"""Functions used in preparing Guido's gorgeous lasagna."""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(minutes_baked):
    """Calculate the bake time remaining."""
    return EXPECTED_BAKE_TIME - minutes_baked

PREPARATION_TIME = 2

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes 
    based on the number of layers (1 layer = 2 minutes)"""
    return number_of_layers * PREPARATION_TIME
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time elapsed on 
    kitchen baking the lasana"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
