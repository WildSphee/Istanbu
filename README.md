# Istanbu

This script to test a popular boardgame called istanbu.
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
```
without power:
    best value:7
    expected return: 4.92

with power:
    best value:8
    expected return: 7.13
    
