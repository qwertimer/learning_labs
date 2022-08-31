"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    print(remaining_time)
    return remaining_time



def preparation_time_in_minutes(layers: int) -> int:
    """Calculates preperation time in minutes

    :param layers: int - amount of layers in the lasagne
    :return: int - preparation time for cake

    Function that takes the amount of layers in the lasagne and converts that into minutes to prepare.
    """
    prep_time = layers*PREPARATION_TIME
    return prep_time

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculates the elapsed time in minutes

    :param number_of_layers: int - number of layers in cake.
    :param elapsed_bake_time: int - number of minutes passed in the oven
    :return: int - elapsed time in minutes

    Function takes two arguments the number of layers of the lasagne and the minutes passed in the oven.
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    #bake_time = bake_time_remaining(elapsed_bake_time)
    
    total_time = elapsed_bake_time + prep_time
    return total_time




