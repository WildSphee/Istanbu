"""
This script is to test a popular boardgame called istanbu.
You are a trader that goes around the stores in town to maximize your
profit, within these stores there is one with a gambling station. Rules
as follows:
    roll two random dice, return the money gained.
    according to istanbul rules, if the sum of two dice
    is equal to or higher than the bet value, you get 
    the bet value, otherwise you get two dollars
    if you bet high (10), if the sum of two dice is 12, you get 10 dollars
    but also higher chances to not hit the amount

In the game you also have an option power for you to choose ONE of
the follow perks whenever you roll two dice:
    1. you can change one of the dice to a 4
    2. you can reroll both dice

With that raises the question, what is the perfect bet value?


final results

without power:
    best value:7
    expected return: 4.92

with power:
    best value:8
    expected return: 7.13
    
"""

from collections import Counter
from random import randint

simulations = 100000
DICE_RANGE = [1,6]


def _roll_die() -> int:
    return randint(*DICE_RANGE)


def _vprint(text, verbose) -> None:
    if verbose:
        print(text)


def roll_two_die_get_money(bet_value:int) -> int:
    """
    roll two random dice, return the money gained.
    according to istanbul rules, if the sum of two dice
    is equal to or higher than the bet value, you get 
    the bet value, otherwise you get two dollars

    Args:
        bet_value (int): the value user bets on, if sum of dice is
            higher or equal you get the bet value, if not 2.
    Returns:
        int: the final value the user gets
    """
    res = _roll_die() + _roll_die()
    return bet_value if res >= bet_value else 2


def roll_two_die_but_you_also_got_powers(bet_value:int, verbose=False) -> int:
    """
    In the game you also have an option power to give you
    the follow perks whenever you roll two dice:
    1. you can change one of the dice to a 4
    2. you can reroll both dice
    As long as it reaches bet value, you get the money,
    Therefore this algorithm checks if it can satisfy with 1. alone
    if not then will go for option 2

    Args:
        bet_value (int): the value user bets on, if sum of dice is
            higher or equal you get the bet value, if not 2.
        verbose (bool): whether output will be displayed at the console
    Returns:
        int: the final value the user gets
    """

    res1 = _roll_die()
    res2 = _roll_die()
    _vprint(f"betting: {bet_value}\nfirst round results: {res1, res2}", verbose)

    if res1 >= 4 and res2 >= 4:
        res = res1 + res2
    else:
        res = max(res1, res2) + 4

    _vprint(f"Using strategy 1 res: {res}", verbose)
    if res < bet_value:
        _vprint(f"rerolling...", verbose)
        res = _roll_die() + _roll_die()
    
    value= bet_value if res >= bet_value else 2
    _vprint(f"final value {res}", verbose)
    _vprint(f"getting paid: {value=}\n*********************", verbose)

    return value


res = Counter()
for _ in range(simulations):
    for i in range(DICE_RANGE[0]*2, DICE_RANGE[1]*2 + 1):
        res[i] += roll_two_die_get_money(i)

print("When rolling two dice, their expected values are: ", res)

res = Counter()
for _ in range(simulations):
    for i in range(DICE_RANGE[0]*2, DICE_RANGE[1]*2 + 1):
        res[i] += roll_two_die_but_you_also_got_powers(i, False)

print("When rolling two dice with power, their expected values are: ", res)
